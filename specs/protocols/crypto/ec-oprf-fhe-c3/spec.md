# EC-OPRF + FHE Password Breach Checks (Unit `ec-oprf-fhe-c3`)

> Spec ID: `sdd.crypto.password-breach.ec-oprf-fhe-c3`


## 1. Scope and Overview

This specification defines an implementation-agnostic unit for password breach
checks using two protocol families:

- An elliptic-curve oblivious pseudorandom function (EC-OPRF) with k-anonymous
  encrypted buckets.
- An optional fully homomorphic encryption (FHE) path using the BFV scheme for
  masked membership checks over encrypted password digests.

The spec is written for language-agnostic implementations. It defines "what" the
algorithms and HTTP APIs MUST do, not "how" a specific library or codebase
implements them.

### 1.1 Audience and Purpose

This spec unit is optimized for large language model (LLM) agents and automated
conformance tools rather than human readers. Its layered structure, explicit
IDs (REQ/FR/NFR), and cross-references are intentionally verbose to make
machine processing and code generation easier. Structural complexity and
redundancy are therefore intentional design choices, not issues to be reduced.

## 2. Notation and Conventions

- "MUST", "SHOULD", and "MAY" are used as in RFC 2119.
- All byte strings are sequences of octets.
- `hex` refers to lowercase hexadecimal without `0x` prefix unless stated
  otherwise.
- Base64url is as in RFC 4648, without padding, unless specified.

Requirement identifiers use the prefix `REQ-` and are intended for machine
consumption by conformance tools.

For each requirement in `profile-core.yaml`:
- `level: must` corresponds to normative "MUST"/"SHALL" semantics.
- `level: should` corresponds to normative "SHOULD" semantics and SHALL NOT be
  phrased as "MUST"/"SHALL" in the requirement text.

This unit is defined at the HTTP+JSON level and assumes that deployments
expose the profiled endpoints over HTTPS (or an equivalent transport with
confidentiality and integrity). Authentication and transport-level mechanisms
such as mTLS are deployment-specific and out of scope for this profile; they
MUST NOT change the on-the-wire request and response contracts defined here.

## 3. EC-OPRF Algorithm Overview

Normative EC-OPRF requirements for this unit are defined in `profile-core.yaml`
under the `requirements` section (identifiers `REQ-OPRF-*`). This section gives
an overview of the intended behavior and points to the relevant requirement IDs.

### 3.1 Curve and Hash-to-Curve

The EC-OPRF ciphersuite for this unit operates over the NIST P-256 curve
(`secp256r1`) as the prime-order group (REQ-OPRF-001). Inputs are mapped to
curve points using the RFC 9380 `P256_XMD:SHA-256_SSWU_RO` hash-to-curve
suite (REQ-OPRF-002). Each logical input type—password SHA-1 digest, password
SHA-256 digest, username+password SHA-256 digest—uses its own domain-separation
tag when invoking hash-to-curve (REQ-OPRF-003).

### 3.2 Inputs, Canonicalization, and Blinding

For password-only checks, the unit distinguishes at least two inputs:
`sha1_p = SHA-1(password)` and `sha256_p = SHA-256(password)` (REQ-OPRF-010).
For username+password checks, the username is canonicalized using Unicode NFKD,
dropping combining marks with category `Mn`, applying casefolding, and
stripping ASCII whitespace from both ends before concatenation with the UTF-8
password bytes (REQ-OPRF-014); the resulting bytes feed `sha256_up` as
SHA-256(canonicalized_username || password) (REQ-OPRF-010).

For each digest `d`, the client computes a hash-to-curve point
`M = H2C(d, DST)` (REQ-OPRF-011), chooses a random non-zero scalar `r` in
`[1, n-1]` (REQ-OPRF-012), and forms a blinded point `B = r · M` encoded as a
SEC1 compressed point for transport (REQ-OPRF-013).

### 3.3 Server Evaluation, Unblinding, and Constant-Time Behavior

The server holds a secret scalar `sk` that acts as the OPRF key (REQ-OPRF-020).
Upon receiving a blinded point `B`, it computes `Yc = sk · B` and returns `Yc`
as a SEC1 compressed point (REQ-OPRF-021). The client decodes `Yc`, computes
the modular inverse `r^{-1}`, and derives the unblinded OPRF output
`Y = r^{-1} · Yc` (REQ-OPRF-022), which is deterministic and pseudorandom from
the adversary’s perspective (REQ-OPRF-023).

Scalar operations, inversions, and point deserialization in the OPRF flow are
expected to avoid secret-dependent branching and memory access to provide
constant-time behavior where practical (REQ-OPRF-040).

### 3.4 Key Derivation and Symmetric Encryption

Clients derive symmetric keys from OPRF outputs using HKDF with SHA-256,
parameterized by salt and info values published via the metadata endpoint
(REQ-OPRF-030). The derived keys have AES-128-GCM key size (REQ-OPRF-031) and
are used to encrypt fixed-size breach-entry payloads. Ciphertexts are protected
using AES-GCM with 12-byte IVs and authentication tags of at least 16 bytes
(REQ-OPRF-032). Additional Authenticated Data (AAD) binds the bucket index and
an AEAD label via the format
`I2OSP(len(label), 2) || label || I2OSP(bucket_idx, w)` (REQ-OPRF-033).

## 4. K-Anonymous Encrypted Buckets

Normative bucket requirements are expressed as `REQ-BUCKET-*` entries in
`profile-core.yaml`.

### 4.1 Bucket Indexing

Bucket indices are derived from hash-to-curve points, not from the OPRF
outputs. For each logical input, clients and servers compute
`H = SHA-256(SEC1_compressed(M))` and take the high-order `NUM_BUCKET_BITS`
bits of `H` as `bucket_idx` (REQ-BUCKET-001). The value of `NUM_BUCKET_BITS` is
published in metadata and used consistently on both sides (REQ-BUCKET-002),
producing HIBP-style k-anonymous buckets that are independent of the OPRF key.

### 4.2 Bucket Construction

Each bucket groups encrypted entries with a fixed plaintext size
for the underlying digest payload plus dummy entries (REQ-BUCKET-010). Buckets
are padded with dummy entries up to a target `pad_to` value configured or
advertised via metadata (REQ-BUCKET-011). If the number of real entries would
exceed `pad_to`, the server treats this as an error and withholds the true
bucket cardinality from the standard API (REQ-BUCKET-012). The AEAD plaintext
for each encrypted bucket entry is a fixed-length digest
`SHA-256(entry_label || digest)` where `entry_label` is derived from
`entry.label_hex` in metadata and `digest` is the password-derived digest for
the logical input mode (`sha1_p`, `sha256_p`, or `sha256_up`); the plaintext
length equals `entry.plaintext_bytes` and is 32 bytes when
`entry.algorithm == "SHA-256"` (REQ-BUCKET-015).

### 4.3 Bucket Encoding

Within a bucket, each encrypted entry is encoded as hex of
`IV || ciphertext || tag` with a 12-byte IV (REQ-BUCKET-020). Bucket responses
return an array of such hex strings in the `entries` field (REQ-BUCKET-021).

## 5. HTTP API — EC-OPRF and Buckets

Normative HTTP requirements are defined as `REQ-API-*` entries, and error
handling uses RFC 9457 Problem Details (REQ-API-ERR-001). Problem Details
responses include a non-sensitive `trace_id` field extension when a trace
identifier is available so that clients and operators can correlate errors
with server-side logs (REQ-API-ERR-TRACE-ID, NFR-OBSERVABILITY-TRACE-001).

### 5.1 Metadata Endpoint

The `GET /v1/metadata` endpoint publishes suite configuration:
an opaque `suite_id` that commits to public parameters and OPRF key, an `oprf`
section that describes curve and point formats, a `buckets` section with
`num_bucket_bits` and prefix formatting, and `kdf`/`aead` sections sufficient
for configuring HKDF and AES-GCM (REQ-API-META-001). Clients retrieve this
metadata before using other endpoints and bind their configuration to the
published `suite_id` (REQ-API-META-002). Conforming clients validate metadata
fields such as `aead.algorithm`, `aead.iv_bytes`, `aead.aad_format`,
`aead.aad_bucket_index_bytes`, digest labels, and `num_bucket_bits` against
the profiled invariants before accepting or using a suite, and treat malformed
or inconsistent metadata as a hard configuration error that prevents OPRF,
bucket, or FHE requests under that suite (REQ-CLI-META-001,
REQ-CLI-META-002, REQ-CLI-META-003, NFR-METADATA-GUARD-001). Clients MAY use
conditional GETs (for example with If-None-Match) to obtain 304 responses when
metadata is unchanged, but are not required to do so; issuing plain GET
requests and treating each 200 response as fresh metadata is conformant for
this profile. This unit does not define a HEAD /v1/metadata endpoint; servers
MAY reject such requests (for example with 405) without affecting conformance.
Deployments MAY enforce authentication on `/v1/metadata` using the same
mechanisms as for the evaluate and bucket endpoints; clients that receive 401
or 403 on `/v1/metadata` SHALL treat these as authentication or authorization
errors per REQ-CLI-AUTH-ERRORS-001 and SHALL NOT attempt evaluate, bucket, or
FHE requests until a subsequent metadata fetch succeeds.

### 5.1.1 Metadata JSON schema (normative)

The body of a successful `GET /v1/metadata` response SHALL be a single JSON
object with the following required top-level fields. Additional top-level
fields are permitted as extensions but are ignored by this profile.

```json
{
  "schema_version": "<major>[.<minor>]",
  "suite_id": "<opaque base64url-no-padding identifier>",
  "api_versions": ["v1"],
  "suite": {
    "version": "v1",
    "hash_to_curve_suite": "P256_XMD:SHA-256_SSWU_RO",
    "hash_to_curve_domain_separation_tag_hex": "<hex>"
  },
  "oprf": {
    "available": true,
    "scheme": "EC-OPRF",
    "curve": "secp256r1",
    "request_point_format": "sec1-compressed-hex",
    "response_point_format": "sec1-compressed-hex"
  },
  "kdf": {
    "hkdf_info": "<ASCII string>",
    "hkdf_salt_hex": "<hex>"
  },
  "aead": {
    "algorithm": "AES-128-GCM",
    "iv_bytes": 12,
    "aad_label_hex": "<hex>",
    "aad_format": "I2OSP(len(label),2)||label||I2OSP(bucket_idx,bucket_index_bytes)",
    "aad_bucket_index_bytes": 3
  },
  "entry": {
    "type": "digest",
    "algorithm": "SHA-256",
    "label_hex": "<hex>",
    "plaintext_bytes": 32
  },
  "buckets": {
    "num_bucket_bits": 20,
    "prefix_format": "hex",
    "prefix_digits": 5,
    "prefix_case": "upper"
  },
  "fhe_bfv": {
    "available": true,
    "scheme": "BFV",
    "parameter_set_id": "BFV-32768-2148728833-9x[60,50,50,50,50,50,50,50,60]",
    "max_context_bytes": 65536,
    "max_ciphertext_bytes": 65536
  },
  "endpoints": {
    "oprf_evaluate": "/v1/oprf/evaluate",
    "bucket_entries": "/v1/buckets"
  }
}
```

The example values above are illustrative; the normative constraints are:

- `schema_version` is a string of the form `"<major>"` or `"<major>.<minor>"`
  where `<major>` and `<minor>` are non-negative decimal integers. For this
  profile, servers MUST publish a `schema_version` whose major component is
  `"1"`. Clients MUST parse the major component and treat any metadata whose
  `schema_version` is missing or whose major component is not `"1"` as an
  unsupported schema version and therefore invalid (REQ-CLI-META-001). When
  the major component is `"1"`, clients MUST accept any minor component value
  (including omission) and MAY log or warn on unfamiliar minors, but SHALL NOT
  reject metadata solely due to the minor component.
- `suite_id` is an opaque identifier computed as specified by REQ-KEY-004.
  Clients MUST NOT infer structure beyond equality comparison and suite
  binding.
- `api_versions` MUST be an array of strings and MUST include `"v1"`;
  clients that implement only this profile SHALL treat metadata that does not
  advertise `"v1"` as unsupported. When `api_versions` contains additional
  entries (for example `"v2"`), v1-only clients SHALL continue to use the `/v1`
  endpoints and MUST ignore other advertised API versions, though they MAY
  surface their presence for informational purposes.
- `suite.version` SHALL be `"v1"` for this profile and
  `suite.hash_to_curve_suite` SHALL be `"P256_XMD:SHA-256_SSWU_RO"`;
  `suite.hash_to_curve_domain_separation_tag_hex` SHALL be a lowercase hex
  string encoding the hash-to-curve domain separation tag used for EC-OPRF
  inputs.
- The `oprf`, `kdf`, `aead`, `entry`, and `buckets` objects SHALL contain
  values that satisfy the invariants in `REQ-OPRF-*`, `REQ-BUCKET-*`,
  `REQ-OPRF-030`, `REQ-OPRF-031`, `REQ-OPRF-032`, `REQ-OPRF-033`,
  `REQ-OPRF-034`, `REQ-CLI-META-002`, `REQ-CLI-META-003`, and
  `REQ-CLI-META-004`. In particular:
  - `oprf.scheme` MUST be `"EC-OPRF"`, `oprf.curve` MUST be `"secp256r1"`,
    and both `oprf.request_point_format` and `oprf.response_point_format`
    MUST be `"sec1-compressed-hex"` (REQ-OPRF-001, REQ-CLI-META-004).
  - `aead.algorithm` MUST be `"AES-128-GCM"`, `aead.iv_bytes` MUST be `12`,
    `aead.aad_format` MUST equal the profiled AAD contract string above, and
    `aead.aad_bucket_index_bytes` MUST equal `ceil(num_bucket_bits / 8)`.
  - `entry.algorithm` MUST be `"SHA-256"` and `entry.plaintext_bytes` MUST be
    `32`.
- When the `oprf-plus-fhe` profile is implemented, the `fhe_bfv` object MUST
  be present. Its `available` field SHALL be a boolean indicating whether the
  FHE BFV evaluate route is configured for this suite. Its `scheme` field
  SHALL be `"BFV"`. Its `parameter_set_id` field SHALL equal the `id` of one
  of the `bfv_parameter_sets` entries in `profile-core.yaml`; this value
  identifies the BFV parameter set that servers expect clients to use when
  constructing contexts (REQ-API-META-FHE-001). The `max_context_bytes` and
  `max_ciphertext_bytes` fields SHALL publish the maximum allowed sizes in
  bytes for the decoded BFV context and ciphertext payloads enforced by
  REQ-FHE-021. Clients that use the FHE route SHALL derive their BFV contexts
  and payload bounds from this `fhe_bfv` section and SHALL treat missing or
  unknown values as hard configuration errors (REQ-CLI-META-FHE-001).
- The `endpoints` object SHALL at least contain string-valued
  `oprf_evaluate` and `bucket_entries` fields giving the relative paths for
  the EC-OPRF evaluate endpoint and bucket retrieval endpoint for this
  profile. Additional keys (for example for FHE or other protocol families)
  MAY be present and MUST be ignored by generic clients that do not
  understand them. Nested objects within `suite`, `oprf`, `kdf`, `aead`,
  `entry`, `buckets`, and `fhe_bfv` MAY likewise include additional fields
  for deployment-specific extensions; conforming clients MUST ignore unknown
  fields in these objects unless explicitly profiled by this unit.

The following tables summarize the required and optional fields for the main
metadata sections. Fields not listed in a table are considered optional
extensions that clients MUST ignore unless explicitly profiled by this unit.

`oprf` object:

| field                   | type    | status   |
|-------------------------|---------|----------|
| `available`             | bool    | required |
| `scheme`                | string  | required |
| `curve`                 | string  | required |
| `request_point_format`  | string  | required |
| `response_point_format` | string  | required |

`kdf` object:

| field            | type    | status   |
|------------------|---------|----------|
| `hkdf_info`      | string  | required |
| `hkdf_salt_hex`  | string  | required |

`aead` object:

| field                    | type    | status   |
|--------------------------|---------|----------|
| `algorithm`              | string  | required |
| `iv_bytes`               | integer | required |
| `aad_label_hex`          | string  | required |
| `aad_format`             | string  | required |
| `aad_bucket_index_bytes` | integer | required |

`entry` object:

| field             | type    | status   |
|-------------------|---------|----------|
| `type`            | string  | required |
| `algorithm`       | string  | required |
| `label_hex`       | string  | required |
| `plaintext_bytes` | integer | required |

`buckets` object:

| field            | type    | status   |
|------------------|---------|----------|
| `num_bucket_bits`| integer | required |
| `prefix_format`  | string  | required |
| `prefix_digits`  | integer | required |
| `prefix_case`    | string  | required |

`fhe_bfv` object (oprf-plus-fhe profile only):

| field                | type    | status   |
|----------------------|---------|----------|
| `available`          | bool    | required |
| `scheme`             | string  | required |
| `parameter_set_id`   | string  | required |
| `max_context_bytes`  | integer | required |
| `max_ciphertext_bytes` | integer | required |
  Deployments that require authentication MAY also publish additional auth-
  related endpoints or metadata, but such extensions MUST NOT reuse or
  conflict with the ProblemTypes registered for this unit and SHOULD use the
  dedicated auth ProblemTypes when returning RFC 9457 Problem Details (see
  REQ-AUTH-ERROR-CONTRACT-001, REQ-API-ERR-AUTH-UNAUTHORIZED,
  REQ-API-ERR-AUTH-FORBIDDEN).

### 5.2 OPRF Evaluate

The OPRF evaluate endpoint is `POST /v1/oprf/evaluate` (REQ-API-OPRF-001).
Requests carry a JSON body with three fields `B_sha1_p`, `B_sha256_p`, and
`B_sha256_up`, each a SEC1 compressed point encoded in lowercase hex
(REQ-API-OPRF-002). Clients include `X-Suite-Id` set to the current `suite_id`;
missing or mismatched suite identifiers lead to 428/412 responses
(REQ-API-OPRF-003). Successful responses use HTTP 200 and are JSON objects
containing evaluated points in fields `Yc_sha1`, `Yc_sha256`, and
`Yc_sha256_up` corresponding to the logical input digests `sha1_p`,
`sha256_p`, and `sha256_up`, each a SEC1 compressed point in lowercase hex
(REQ-API-OPRF-004).

### 5.3 Buckets

Bucket retrieval uses `GET /v1/buckets` with three query parameters `sha1`,
`sha256`, and `sha256_up`, each a fixed-length hexadecimal prefix of the
corresponding logical digest (`sha1_p`, `sha256_p`, or `sha256_up`) (REQ-BUCKET-001,
REQ-API-BKT-001). The prefix length in hex digits SHALL equal
`buckets.prefix_digits`, and implementations SHALL ensure that
`buckets.prefix_digits == ceil(num_bucket_bits / 4)` so that the prefix
encodes the high-order `num_bucket_bits` bits of the digest. Parameter values
MUST consist only of characters `0-9`, `a-f`, or `A-F`; servers MUST accept
either case and MAY normalize internally. The response is a JSON object with
an `entries` array of encoded bucket entries (REQ-API-BKT-001). Successful
GET responses use HTTP 200. `HEAD /v1/buckets` uses HTTP 200 or 304 with the
same caching headers as GET and never returns a body on success
(REQ-API-BKT-002). 
Both methods set `Cache-Control`, `ETag`, and `Vary: X-Suite-Id` to support
safe caching partitioned by suite (REQ-API-BKT-003). Invalid prefixes and
missing or mismatched `X-Suite-Id` values are mapped to 400/428/412 errors
(REQ-API-BKT-004).

## 6. FHE BFV Membership Check (Optional)

This section provides an overview of the optional BFV FHE path. Normative
requirements are captured as `REQ-FHE-*` entries in `profile-core.yaml`.

### 6.1 Semantics and Parameters

The FHE route implements a BFV scheme over integers (REQ-FHE-001). The server
accepts a client-provided BFV context and ciphertext, validates parameters
against an allowed policy, and then treats them as opaque byte strings
(REQ-FHE-002, REQ-FHE-020). The intended result semantics are masked equality:
when the client decrypts the result ciphertext, a match yields plaintext 0 and
a non-match yields a random non-zero element (REQ-FHE-003). Evaluation uses
deterministic padding to a fixed `pad_to` and performs constant-work operations
across buckets (REQ-FHE-004, REQ-FHE-022).

The parameter policy is expected to ensure at least 128-bit classical security
for RLWE-based BFV (REQ-FHE-040). This unit defines one mandatory parameter set
`BFV-32768-2148728833-9x[60,50,50,50,50,50,50,50,60]` (poly degree 32768,
plain modulus 2148728833, and a nine-prime coefficient-modulus ladder with bit
sizes [60, 50, 50, 50, 50, 50, 50, 50, 60]) which conforming servers MUST
support (REQ-FHE-020, see `bfv_parameter_sets` in `profile-core.yaml`). Additional
parameter sets MAY be offered, but clients SHOULD treat this default as the
interoperable baseline unless otherwise negotiated.
Metadata for FHE is published via the `fhe_bfv` object in `/v1/metadata`,
including the BFV `parameter_set_id` and maximum allowed context and ciphertext
sizes. Clients derive their BFV configuration from this metadata rather than
from hard-coded parameters (REQ-API-META-FHE-001, REQ-CLI-META-FHE-001).

### 6.2 HTTP API

The FHE evaluate endpoint is `POST /v1/fhe/evaluate` when the
`fhe-bfv-membership` feature is enabled (REQ-FHE-010). Requests carry JSON
fields `hash_algorithm`, `bucket_prefix_hex`, `context_b64`, and
`ciphertext_b64` (REQ-FHE-011). The `hash_algorithm` field SHALL be one of
`"sha1"`, `"sha256"`, or `"sha256_up"` and selects the corresponding logical
input type defined for EC-OPRF when deriving bucket prefixes and residues
(REQ-FHE-014, REQ-OPRF-010, REQ-OPRF-014). Clients include `X-Suite-Id` and the server
enforces the same suite binding rules as for the OPRF route (REQ-FHE-012).
Responses return a JSON object containing a single `ciphertext_b64` field
holding the result ciphertext (REQ-FHE-013).

For each `hash_algorithm` value, the FHE route reuses the exact digest
construction and, where applicable, username canonicalization rules from the
EC-OPRF flow in §3.2. Specifically, `"sha1"` uses `sha1_p = SHA-1(password)`,
`"sha256"` uses `sha256_p = SHA-256(password)`, and `"sha256_up"` uses
`sha256_up = SHA-256(canonicalized_username || password)` with
canonicalized_username computed as in REQ-OPRF-014. The FHE path does not
introduce a distinct digest or hash-to-curve scheme; it profiles these same
logical inputs for homomorphic evaluation (REQ-FHE-014, REQ-OPRF-010,
REQ-OPRF-011, REQ-OPRF-014).

### 6.3 Validation, Limits, and Interoperability

The server validates the BFV scheme, polynomial degree, plain modulus,
coefficient-modulus ladder, and presence of relinearization keys against an
allowed policy (REQ-FHE-020). It enforces maximum sizes for `context_b64` and
`ciphertext_b64` to defend against resource exhaustion (REQ-FHE-021). The
maximum decoded sizes in bytes are published via the `max_context_bytes` and
`max_ciphertext_bytes` fields in `fhe_bfv` metadata so that clients can avoid
constructing oversized payloads (REQ-API-META-FHE-001, REQ-CLI-META-FHE-001).
Buckets that would exceed FHE `pad_to` thresholds result in 503 responses
without revealing the true bucket size (REQ-FHE-022,
REQ-API-ERR-FHE-BUCKET-EXCEEDS-PAD).

Ciphertexts are treated as opaque by the API: this unit does not define a
normative BFV wire format and does not promise cross-library ciphertext
compatibility (REQ-FHE-030, REQ-FHE-031).

FHE-specific error conditions map to a small, fixed set of Problem Details
types. When the FHE feature is disabled or the engine is unavailable, servers
use `urn:problem:fhe:unavailable` (REQ-API-ERR-FHE-UNAVAILABLE). Pad-to-limit
violations for the FHE bucket path use
`urn:problem:fhe:bucket-exceeds-pad-target`
(REQ-API-ERR-FHE-BUCKET-EXCEEDS-PAD). Failures to assemble residues or fetch
upstream bucket data use `urn:problem:fhe:upstream-unavailable`
(REQ-API-ERR-FHE-UPSTREAM-UNAVAILABLE). Invalid prefixes, contexts,
ciphertexts, and size violations use the dedicated FHE input-validation types
from the ErrorModel (REQ-API-ERR-FHE-INVALID-PREFIX,
REQ-API-ERR-FHE-INVALID-CONTEXT, REQ-API-ERR-FHE-INVALID-CIPHERTEXT,
REQ-API-ERR-FHE-CONTEXT-TOO-LARGE, REQ-API-ERR-FHE-CIPHERTEXT-TOO-LARGE), and
implementations SHALL NOT introduce alternative ProblemTypes for these
conditions. Clients interpret a 0 plaintext as "match" and non-zero as "no
match" as long as BFV decryption succeeds and the plaintext lies within the
expected modulus and slot structure (REQ-FHE-003). Decryption failures or
plaintexts outside the expected BFV domain SHALL be surfaced as errors rather
than "no match" results and SHOULD be distinguished in telemetry from both
successful "match"/"no match" outcomes and generic availability failures.

### 6.4 FHE client behavior checklist (normative)

This subsection restates existing normative requirements for FHE clients as a
compact checklist; it does not introduce behavior beyond the `REQ-*` items in
`profile-core.yaml`.

When implementing a conformant FHE client for this unit, at minimum:

1. **Fetch and validate metadata:** Clients call `GET /v1/metadata`, validate
   the global schema and the `fhe_bfv` object (including `scheme`,
   `parameter_set_id`, `max_context_bytes`, and `max_ciphertext_bytes`),
   ignore unknown fields, and treat unsupported schema versions or
   malformed/missing required fields as hard configuration errors that forbid
   FHE use under that suite (REQ-API-META-001, REQ-API-META-003,
   REQ-API-META-FHE-001, REQ-CLI-META-001, REQ-CLI-META-002,
   REQ-CLI-META-003, REQ-CLI-META-004, REQ-CLI-META-IGNORE-UNKNOWN,
   REQ-CLI-META-FHE-001).
2. **Bind to suite_id and origin:** Clients bind BFV configuration to the
   `suite_id` and deployment origin from metadata, scope that binding to a
   single origin, and include `X-Suite-Id` on all `POST /v1/fhe/evaluate`
   requests; 428/412 responses are treated as rotation signals that trigger a
   metadata refetch and at most one retry, never as breach results
   (REQ-API-META-002, REQ-FHE-012, REQ-KEY-001, REQ-KEY-003, REQ-KEY-004,
   REQ-KEY-005, NFR-SUITE-BINDING-001).
3. **Derive logical inputs and bucket prefixes:** Clients derive `sha1_p`,
   `sha256_p`, and `sha256_up` using the canonical digest and username
   canonicalization rules from §3.2 and set `hash_algorithm` to `"sha1"`,
   `"sha256"`, or `"sha256_up"` accordingly; bucket prefixes are computed
   using the same digest-to-prefix mapping and metadata parameters
   (`num_bucket_bits`, `prefix_digits`) as for the bucket API
   (REQ-OPRF-010, REQ-OPRF-014, REQ-FHE-014, REQ-BUCKET-001).
4. **Construct BFV context and ciphertext from metadata:** Clients that use the
   FHE BFV evaluate route derive BFV contexts and ciphertext shapes from the
   `fhe_bfv` section of `/v1/metadata`, verify that `fhe_bfv.scheme` equals
   `"BFV"` and that `fhe_bfv.parameter_set_id` matches a known BFV parameter
   set, and treat missing or unknown `parameter_set_id`, `max_context_bytes`,
   or `max_ciphertext_bytes` values as hard configuration errors that prevent
   use of the FHE route under that suite (REQ-API-META-FHE-001,
   REQ-FHE-020, REQ-FHE-021, REQ-CLI-META-FHE-001).
5. **Form FHE requests correctly:** Clients send `POST /v1/fhe/evaluate` with
   a JSON body containing `hash_algorithm`, `bucket_prefix_hex`,
   `context_b64`, and `ciphertext_b64`, encode `context_b64` and
   `ciphertext_b64` using base64url, and include `X-Suite-Id` bound to
   metadata; they expect a 200 response with a single `ciphertext_b64` field
   on success and RFC 9457 Problem Details on 4xx/5xx per the error model
   (REQ-FHE-010, REQ-FHE-011, REQ-FHE-012, REQ-FHE-013, REQ-API-ERR-001,
   REQ-API-ERR-FHE-UNAVAILABLE, REQ-API-ERR-FHE-BUCKET-EXCEEDS-PAD,
   REQ-API-ERR-FHE-UPSTREAM-UNAVAILABLE, REQ-API-ERR-FHE-INVALID-PREFIX,
   REQ-API-ERR-FHE-INVALID-CONTEXT, REQ-API-ERR-FHE-INVALID-CIPHERTEXT,
   REQ-API-ERR-FHE-CONTEXT-TOO-LARGE, REQ-API-ERR-FHE-CIPHERTEXT-TOO-LARGE).
6. **Interpret decrypted results safely:** For successful responses, clients
   decrypt the returned ciphertext in the BFV context implied by metadata and
   treat plaintext 0 as "match" and any non-zero plaintext within the expected
   modulus and slot structure as "no match"; decryption failures or plaintexts
   outside the expected BFV domain are surfaced as errors, not as "no match",
   and are distinguished in telemetry from both successful outcomes and
   generic availability failures (REQ-FHE-003).
7. **Handle auth, rate limits, and 5xx consistently:** Clients treat 401/403
   (including on `/v1/metadata`) as authentication or authorization errors
   rather than breach results, honor `Retry-After` and backoff semantics on
   429 from the FHE endpoint, and treat 5xx responses as transient errors that
   may be retried subject to local policies; in all of these cases, clients
   MUST NOT treat the password as "not breached" solely because an FHE request
   failed (REQ-CLI-AUTH-ERRORS-001, REQ-API-RATE-LIMIT-CLI-001,
   REQ-RESILIENCE-5XX-001).

## 7. Key Management and Suite Binding

This section summarizes how OPRF key material, suite identifiers, and client
behavior during rotations fit together. Normative requirements are defined as
`REQ-OPRF-*`, `REQ-API-META-*`, `REQ-API-OPRF-*`, `REQ-API-BKT-*`,
`REQ-API-ERR-*`, and `REQ-KEY-*` in `profile-core.yaml`.

### 7.1 Server OPRF Key and Suite Epochs

The server holds a long-lived OPRF private key `sk` for the active suite
(REQ-OPRF-020, REQ-KEY-001). The metadata endpoint publishes an opaque
`suite_id` that commits to the public parameters and the OPRF key epoch and is
stable across restarts while those values are unchanged (REQ-API-META-001,
REQ-KEY-002). When the OPRF key or suite parameters that affect bucket
encryptability change, the server rotates to a new `suite_id` (REQ-KEY-002).
Suite parameters that affect encryptability include the hash-to-curve
domain-separation tags, HKDF salt and info values, AEAD AAD labels, IV
derivation labels, and the bucket index width used in AAD
(REQ-OPRF-033, REQ-OPRF-034, REQ-BUCKET-013).
The uniqueness and stability guarantees for suite_id are scoped to a single
deployment origin (for example a given base URL or service cluster). Clients
MUST treat suite_id values obtained from different origins as unrelated even
if the strings collide and MUST NOT attempt to reuse metadata or suite-bound
configurations across origins based solely on suite_id equality.

### 7.2 Client Binding and Rotation Behavior

Clients fetch `/v1/metadata` before calling evaluate or bucket endpoints and
bind their configuration (curve parameters, bucket parameters, KDF/AEAD
parameters) to the published `suite_id` (REQ-API-META-002,
NFR-SUITE-BINDING-001). All evaluate and bucket requests carry
`X-Suite-Id: <suite_id>`; missing or mismatched values produce 428/412 Problem
Details responses using the registered ProblemTypes (REQ-API-OPRF-003,
REQ-API-ERR-OPRF-SUITE-ID-REQUIRED, REQ-API-ERR-OPRF-SUITE-ID-MISMATCH).

Upon receiving a 428 Precondition Required or 412 Precondition Failed due to a
suite mismatch, conforming clients refetch `/v1/metadata`, update their bound
suite configuration, and retry the request at most once (REQ-KEY-003,
REQ-API-RATE-LIMIT-CLI-001). Clients MUST NOT treat 428/412 as definitive
"not breached" results; they indicate configuration drift rather than password
status.

The canonical construction of `suite_id` is defined in REQ-KEY-004: servers
serialize a JSON object containing the hash-to-curve DST, KDF info and salt,
AEAD algorithm, IV length, AEAD label, bucket index width, entry digest
algorithm and label, and a SEC1-compressed OPRF public key commitment with
keys sorted lexicographically and no extra whitespace; they then compute
`suite_id = base64url_no_padding(SHA-256(canonical_json_bytes))`. FHE and OPE
parameters are explicitly excluded from this binding so that FHE-only or
OPE-only parameter tuning does not change `suite_id`.

### 7.3 Caching and Epoch Partitioning

Bucket responses include `Cache-Control`, `ETag`, and `Vary: X-Suite-Id`
headers to permit caches to partition responses by suite and avoid mixing data
across key epochs (REQ-API-BKT-003, NFR-CACHING-001, NFR-KEY-ROTATION-001). A
key rotation or suite bump that changes `suite_id` naturally leads to disjoint
cache keys when intermediaries include the full request URL and `X-Suite-Id`
in their cache key construction, as illustrated by this unit's caching
recipes. Metadata responses include Cache-Control directives that prevent
intermediaries from serving stale `/v1/metadata` across rotations
(REQ-API-META-003).

### 7.4 FHE Considerations

For the FHE route, the server validates client-provided BFV contexts and
ciphertexts but otherwise treats them as opaque byte strings
(REQ-FHE-002, REQ-FHE-020, REQ-FHE-030). The long-lived secrecy of BFV
decryption keys is managed client-side; server-side key rotation for the OPRF
does not require an FHE key lifecycle on the server. However, OPRF key
rotation can change deterministic padding residues and evaluation masks used
for constant-work FHE evaluation, which are implicitly bound to `suite_id`
through the same suite binding rules (REQ-FHE-012, NFR-CONSTANT-WORK-001,
NFR-SUITE-BINDING-001).

### 7.5 Tracing and Correlation (Informative)

Conforming implementations support structured observability by propagating a
trace identifier across logs and error responses. When a valid W3C Trace
Context `traceparent` header is present on a request, the server reuses its
`trace-id`; otherwise it generates a new 32-hex `trace_id` per request and
includes it in the logging context. Error responses using Problem Details
include the same `trace_id` in an extension field for correlation, and
responses echo a `traceparent` header with the request `trace-id` and a fresh
`span-id` where appropriate (NFR-OBSERVABILITY-TRACE-001).

## 8. Client Integration Walkthrough (Informative)

This section gives an end-to-end client integration walkthrough for the
profiles in this unit. It is informative and defers all normative behavior to
the requirement sets in `profile-core.yaml`, particularly
`REQ-OPRF-*`, `REQ-BUCKET-*`, `REQ-API-*`, `REQ-FHE-*`, the functional
requirements (FRs), and the non-functional requirements (NFRs).

### 8.1 Step 1: Fetch and Bind Metadata

Clients begin by calling `GET /v1/metadata` to obtain the suite configuration:
an opaque `suite_id`, OPRF parameters, bucket parameters (including
`num_bucket_bits` and prefix formatting), and KDF/AEAD parameters sufficient to
configure hash-to-curve, HKDF, and AES-GCM (REQ-API-META-001). Clients bind
their local configuration to this `suite_id` and MUST include it in
`X-Suite-Id` on subsequent OPRF evaluate, bucket, and FHE evaluate requests
(REQ-API-META-002, REQ-API-OPRF-003, REQ-FHE-012, NFR-SUITE-BINDING-001).

### 8.2 Step 2: Compute Digests and Bucket Prefixes

For each password, clients compute three logical inputs:

- `sha1_p = SHA-1(password)` and `sha256_p = SHA-256(password)` for
  password-only checks.
- `sha256_up = SHA-256(canonicalized_username || password)` for
  username+password checks, where the username is canonicalized via Unicode
  NFKD, removal of combining marks with category `Mn`, casefolding, and
  stripping of ASCII whitespace (REQ-OPRF-010, REQ-OPRF-014).

Bucket indices are derived from hash-to-curve points, not from the OPRF
outputs. For each logical input, clients compute
`H = SHA-256(SEC1_compressed(M))` for the corresponding point `M` and take the
high-order `NUM_BUCKET_BITS` bits as `bucket_idx` (REQ-BUCKET-001). The value
of `NUM_BUCKET_BITS` and any prefix encoding (for example fixed-width hex
digits) are obtained from metadata and MUST be used consistently by both
clients and servers (REQ-BUCKET-002, REQ-API-BKT-001).

### 8.3 Step 3: EC-OPRF Evaluate and Key Derivation

For each digest input, the client computes a curve point
`M = H2C(d, DST)` using the configured hash-to-curve suite and domain
separation tags (REQ-OPRF-001, REQ-OPRF-002, REQ-OPRF-003, REQ-OPRF-011). It
then samples a random non-zero scalar `r` in `[1, n-1]` and forms a blinded
point `B = r · M` encoded as a SEC1 compressed point (REQ-OPRF-012,
REQ-OPRF-013).

The client sends `POST /v1/oprf/evaluate` with a JSON body containing blinded
points `B_sha1_p`, `B_sha256_p`, and `B_sha256_up` and the `X-Suite-Id` header
bound to metadata (REQ-API-OPRF-001, REQ-API-OPRF-002, REQ-API-OPRF-003). The
server responds with evaluated points `Yc_sha1`, `Yc_sha256`, and
`Yc_sha256_up` as SEC1 compressed hex strings
(REQ-OPRF-020, REQ-OPRF-021, REQ-API-OPRF-004). The client decodes each
evaluated point, computes `r^{-1} mod n` for the corresponding blind, and
derives unblinded OPRF outputs `Y_* = r^{-1} · Yc_*` (REQ-OPRF-022,
REQ-OPRF-023).

Derived OPRF outputs are converted into symmetric keys via HKDF with SHA-256
using the `salt` and `info` values from metadata (REQ-OPRF-030). The resulting
keys are suitable for AES-128-GCM (REQ-OPRF-031) and are used to decrypt
bucket entries as described below.

### 8.4 Step 4: Bucket Retrieval and Local Decryption

Clients construct bucket query parameters `sha1`, `sha256`, and `sha256_up`
from the computed `bucket_idx` values and the `buckets.prefix_digits` field in
metadata and issue `GET /v1/buckets` (or `HEAD /v1/buckets` for cache
validation) with the `X-Suite-Id` header (REQ-API-BKT-001, REQ-API-BKT-002,
REQ-API-BKT-003).
Successful responses return a JSON object with an `entries` array of encoded
bucket entries, each representing `hex(IV || ciphertext || tag)` where `IV` is
12 bytes (REQ-BUCKET-010, REQ-BUCKET-011, REQ-BUCKET-020,
REQ-BUCKET-021, REQ-OPRF-032).

For each logical input mode, the client derives Additional Authenticated Data
`AAD = I2OSP(len(label), 2) || label || I2OSP(bucket_idx, w)` using the label
and width `w` advertised in metadata (REQ-OPRF-033, REQ-BUCKET-013) and
decrypts each entry with the corresponding AES-GCM key and AAD. It then
performs constant-time comparisons between decrypted payloads and locally
computed reference values for each digest to decide whether a breach match
exists, using the canonical plaintext digest construction defined for the
entry payload (`SHA-256(entry_label || digest)` as described in §4.2,
REQ-BUCKET-015).
Within a given `suite_id` epoch, bucket contents and ordering SHOULD be stable
for the same bucket index except when an intentional rotation or dataset
update occurs (REQ-BUCKET-014, NFR-BUCKET-STABILITY-001).

Invalid bucket prefixes and missing or mismatched `X-Suite-Id` headers result
in Problem Details errors as specified in the error model
(`REQ-API-ERR-BUCKET-INVALID-PREFIX`,
`REQ-API-ERR-OPRF-SUITE-ID-REQUIRED`,
`REQ-API-ERR-OPRF-SUITE-ID-MISMATCH`).

### 8.5 Step 5: Optional FHE Flow

When the `fhe-bfv-membership` feature is enabled, clients MAY use the BFV FHE
route as an alternative to local bucket decryption. The client chooses a
supported `hash_algorithm`, computes the corresponding bucket prefix, and
constructs a BFV context and ciphertext according to the advertised parameter
policy (REQ-FHE-001, REQ-FHE-011, REQ-FHE-020). It then sends
`POST /v1/fhe/evaluate` with fields `hash_algorithm`, `bucket_prefix_hex`,
`context_b64`, and `ciphertext_b64` and includes `X-Suite-Id`, which is
validated using the same suite binding semantics as the OPRF route
(REQ-FHE-010, REQ-FHE-011, REQ-FHE-012).

The server evaluates the encrypted membership check over a deterministically
padded bucket using constant-work operations, returns a result ciphertext in
`ciphertext_b64`, and enforces context and ciphertext size limits to defend
against abuse (REQ-FHE-003, REQ-FHE-004, REQ-FHE-013, REQ-FHE-021,
REQ-FHE-022, NFR-CONSTANT-WORK-001). Upon decryption, the client interprets a
plaintext of 0 as "match" and a non-zero plaintext as "no match"
(REQ-FHE-003).

Clients SHOULD handle Problem Details errors from the FHE route analogously to
the OPRF and bucket endpoints, including treating HTTP 429 Too Many Requests
and 5xx responses as transient per the non-functional requirements
(`REQ-API-RATE-LIMIT-001`, `REQ-API-RATE-LIMIT-CLI-001`,
`NFR-RESILIENCE-5XX-001`).

## 9. Functional Requirements (FR index)

Higher-level functional requirements for this unit are defined in
`profile-core.yaml` under `functional_requirements`. They group the low-level
`REQ-*` items into implementation-facing capabilities. The current FR IDs are:
`FR-OPRF-API-001`, `FR-METADATA-001`, `FR-BUCKETS-API-001`, and
`FR-FHE-API-001`; see the YAML bundle for their normative definitions.

## 10. Non-Functional Requirements (NFR index)

Non-functional requirements are likewise modeled only in `profile-core.yaml`
under `non_functional_requirements`. They capture behavioral guarantees such as
constant-work evaluation, caching semantics, suite binding, opaque ciphertext
handling, constant-time OPRF behavior, rate limiting, logging/privacy, and
5xx resilience. The current NFR IDs include
`NFR-CONSTANT-WORK-001`, `NFR-CACHING-001`, `NFR-SUITE-BINDING-001`,
`NFR-OPAQUE-CIPHERTEXT-001`, `NFR-OPRF-CONSTANT-TIME-001`,
`NFR-RATE-LIMIT-001`, `NFR-LOGGING-PRIVACY-001`, `NFR-RESILIENCE-5XX-001`,
`NFR-KEY-ROTATION-001`, `NFR-BUCKET-STABILITY-001`, and
`NFR-OBSERVABILITY-TRACE-001`.

## 11. Fixtures (Informative)

Concrete HTTP-shape fixtures for this unit are provided in `fixtures.yaml` and
are referenced from `spec.yaml` under `normative_bundles.fixture_shapes` and
from `conformance.yaml` as `fixture_shapes`. They are explicitly marked
`role: http-shape-only` and `normative: false` and are intended to drive
endpoint and payload-shape testing only; cryptographic correctness MUST be
validated separately using external RFC vectors and implementation-level tests.
