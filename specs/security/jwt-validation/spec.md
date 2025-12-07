# JWT Validation

> Spec ID: `sdd.security.jwt.validation`

This Markdown file is the human-readable companion to `spec.yaml`. It should
explain the intent, background, and behavior of the spec unit in
implementation-neutral language. Treat `spec.yaml` (and any referenced
machine-readable bundles) as normative and this file as narrative.

Before authoring or updating this spec unit, consult the repository-level
authoring docs (for example, `docs/specs-constitution.md`,
`docs/authoring-guidelines.md`, and `docs/style-guide.md`) to ensure that this
spec follows the shared conventions and gates.

## Normative Sources & Reading Order

The normative sources for this spec unit are:

- `spec.yaml` (canonical machine-readable definition).
- Any supporting bundles or schemas referenced from `spec.yaml` (for example,
  profile or conformance bundles, JSON Schemas, or other machine-readable
  artifacts).
- External standards (for example, RFCs, FIPS documents, or other specs)
  referenced from `spec.yaml` or from those bundles. For this spec, they
  include at least:
  - RFC 7519 (JSON Web Token – JWT).
  - RFC 7515 (JSON Web Signature – JWS).
  - RFC 7517 (JSON Web Key – JWK).
  - RFC 7518 (JSON Web Algorithms – JWA).

Suggested reading order:

1. Start with `spec.yaml` to understand the spec unit’s ID, scope, lifecycle,
   and any referenced bundles or external standards.
2. If present, read any referenced machine-readable bundles to see the full
   behavioral model, constraints, or profiles.
3. Use this `spec.md` file for overview, concepts, narrative behavior, and
   rationale; it should not introduce behavior that is absent from the
   machine-readable sources above.

Any disagreement between narrative text in this Markdown file and the
machine-readable sources listed above MUST be resolved in favor of the
machine-readable sources and external standards.

## Files in This Spec Unit

This directory typically contains:

- `spec.yaml` – SDD-style metadata and canonical machine-readable definition
  for this spec unit (including its ID, lifecycle, dependencies, and pointers
  to any bundles or external standards).
- `spec.md` – this human-readable overview and navigation document.
- `open-questions.md` – a scratchpad for currently open questions about this
  spec unit; it must contain only open questions and is not an archive.
- `decision-log.md` (optional) – a non-normative log of resolved questions and
  design decisions, with stable local IDs (for example, `D-001`); normative
  behavior remains defined by `spec.yaml` and any referenced bundles.
- `examples/` (optional) – example files such as `examples/vectors.yaml`
  or walkthroughs.
- `profiles/` (optional) – profile or binding definitions that specialize this
  spec for particular environments or use cases.
- `targets/` (optional) – language/stack-specific implementation target
  descriptors (for code generation or implementation planning).
- `visuals/` (optional) – non-normative AI image prompts and visualization
  guidance (`visuals/prompts.md`).

## Overview

This spec unit defines an implementation-neutral contract for validating JSON
Web Tokens (JWTs) against a caller-supplied policy and key material. It is
written as a `library-api` so that multiple implementations can offer a
compatible `validate_jwt`-style surface without committing to a particular
language, framework, or transport.

In later iterations, this spec is also intended to anchor:

- conformance and drift-detection tooling that can exercise manual
  implementations and produce human-readable audit reports, and
- structured claim extraction flows that allow callers to obtain decoded
  claims with or without full validation, subject to clearly documented risk
  and policy.

For version `0.1.0`, all three facets—validation, claim extraction, and the
conformance/audit harness—are intentionally defined under this single spec
ID. Future versions MAY revise this arrangement (for example, by introducing
a dedicated audit spec or profile), but such a change would be treated as a
separate, explicit evolution of the spec rather than a silent restructuring.

While there are unresolved medium- or high-impact topics for this spec unit,
they are tracked in `open-questions.md` and may evolve across versions. Once
a question is resolved, its outcome is captured in the normative artefacts
and the corresponding row is removed from that file.

## Concepts

- JWT validation: treating a JWT as a structured object (header, claims, and
  signature/MAC) that is checked against keys and policy.
- Claim extraction: decoding and returning claims (with appropriate tagging)
  regardless of whether full validation succeeds, subject to policy, including
  whether claims may be returned on validation failure.
 - Key material and selection: representing one or more verification keys in
  `key_material` and selecting an appropriate key (for example, using
  header.kid and algorithm constraints) before attempting signature or MAC
  verification.

## Behavior and Interfaces

This spec models three related operations over JWTs. These operations are
defined as **conceptual, normative abstractions** for the purposes of this
spec and its conformance model, not as a required concrete public API
signature in any particular language or framework:

- `validate_jwt` – validate a compact JWT against supplied policy and keys.
- `extract_claims` – decode a JWT and return a tagged view of header and
  claims, with or without full validation.
- `run_conformance_audit` – execute validation and claim-extraction scenarios
  against an implementation and produce a structured audit report.

Implementations MAY expose different public API shapes (for example, method
names, parameter ordering, or transports) as long as there is a clear,
documented mapping from their API to these conceptual operations when claiming
conformance to the corresponding classes in `conformance.yaml`. Brownfield
systems can use thin adapters to satisfy these operation contracts for
conformance and testing without changing their existing external interfaces.

### Result model – `validation_result`

Implementations return a `validation_result` object for validation-oriented
operations. It has a compact but expressive shape:

- `status` – primary outcome of validation. Expected values include:
  - `valid`
  - `rejected-expired`
  - `rejected-not-yet-valid`
  - `rejected-signature`
  - `rejected-audience`
  - `rejected-issuer`
  - `rejected-policy`
  - `rejected-malformed`
  - `indeterminate`
- `reason_codes` – zero or more machine-readable reason codes such as
  `expired`, `audience-mismatch`, or `issuer-mismatch`. Multiple entries are
  allowed when several checks fail.
- `message` – optional human-readable explanation. It is intended for logs
  and diagnostics, not for programmatic branching.
- `applied_policy` – optional summary of the validation policy that was
  effectively applied (for example, references to policy IDs or profiles).
- `raw_without_signature` – optional compact JWT representation consisting
  only of the header and payload segments
  (`<base64url(header)>.<base64url(payload)>`), without any signature or MAC
  segment. This field exists to support logging and diagnostics and MUST NOT
  be used as an authorization artefact.

The `status` field carries the primary failure mode (for example,
`rejected-audience`), while `reason_codes` can enumerate multiple contributing
reasons. A consumer that needs to distinguish specific failures can either
branch on `status` or look for particular entries in `reason_codes`.

This spec **does not define a formal, closed registry** of `reason_codes`.
Instead, it provides a small set of **RECOMMENDED** example code strings to
encourage convergence (for example, `expired`, `audience-mismatch`,
`issuer-mismatch`, `kid-not-found`, `kid-ambiguous`,
`signature-verification-failed`, `claims-only-mode`), but implementations MAY
use different or additional code values. Interoperability and conformance rely
primarily on `status`; consumers SHOULD treat `reason_codes` as structured
diagnostic hints unless a tighter vocabulary is defined in an ecosystem- or
profile-specific binding.

Normatively, implementations MUST map common failure categories to status
values as follows (example `reason_codes` are RECOMMENDED but not exhaustive):

- **Expired tokens** – when `exp` is expired relative to the validation
  clock after applying any configured `clock.leeway_seconds`, implementations
  MUST use `rejected-expired` and SHOULD include a reason code such as
  `expired`. Formally, a token is expired if
  `now_epoch_seconds >= exp - leeway_seconds` when `exp` is required and present.
- **Not-yet-valid tokens** – when `nbf`/`iat` checks indicate that the token
  is not yet valid (after leeway), implementations MUST use
  `rejected-not-yet-valid` and SHOULD include a reason code such as
  `not-yet-valid`. Formally, a token is not-yet-valid if
  `now_epoch_seconds < nbf - leeway_seconds` when `nbf` is required and present.
- **Signature or MAC failure** – when a signature or MAC does not verify
  under supported algorithms and available `key_material` (for example, wrong
  key or corrupted signature), implementations MUST use `rejected-signature`
  and SHOULD include a reason code such as `signature-verification-failed`.
- **Audience mismatch** – when audience requirements derived from
  `validation_policy.expected_audience` are not satisfied by the `aud` claim
  (for example, missing an expected audience), implementations MUST use
  `rejected-audience` and SHOULD include a reason code such as
  `audience-mismatch`.
- **Issuer mismatch** – when issuer requirements derived from
  `validation_policy.expected_issuer` are not satisfied by the `iss` claim
  (for example, issuer not in an allowed set), implementations MUST use
  `rejected-issuer` and SHOULD include a reason code such as
  `issuer-mismatch`.
- **Policy violations** – when tokens violate structural or semantic policy
  requirements (for example, missing required claims, claim type mismatches,
  forbidden `alg: none`, algorithms not allowed by policy, invalid or
  conflicting profiles, invalid time relationships like `nbf > exp`, or
  invalid clock configuration), implementations MUST use `rejected-policy`
  and SHOULD include reason codes that reflect the specific violation (such
  as `missing-required-claim`, `claim-type-mismatch`, `alg-none-disallowed`,
  `algorithm-not-allowed`, `invalid-profile`, or `invalid-clock-config`).
- **Malformed tokens** – when compact serialization or payload decoding
  fails (for example, wrong number of segments, invalid base64url, non-JSON
  payload, or invalid UTF-8 where required), implementations MUST use
  `rejected-malformed`.
- **Indeterminate outcomes** – when the implementation cannot conclusively
  determine success or failure under policy (for example, missing or
  ambiguous keys such as `kid` not found or ambiguous across keys, operation
  in claims-only mode without full validation, or other cases where
  `key_material` or policy are insufficient to decide), implementations MUST
  use `indeterminate` and SHOULD include reason codes that describe the
  source of uncertainty (such as `kid-not-found`, `kid-ambiguous`, or
  `claims-only-mode`). Callers MUST treat `indeterminate` as non-valid for
  authorization decisions; it is never equivalent to `valid`.

### Key material and kid handling

`key_material` represents the keys and any associated metadata used to
verify JWT signatures or MACs. This spec does not prescribe a concrete data
format for `key_material`, but it does require some minimal behavior:

- Implementations MUST support `key_material` that contains multiple
  verification keys (for example, a keyset with identifiers and algorithm
  metadata).
- When a JWT header contains a `kid` value, implementations MUST attempt key
  selection based on that `kid` together with any applicable algorithm or
  usage constraints expressed in `key_material`.
- If `kid` is present but no suitable key in `key_material` can be selected
  for verification, implementations MUST treat the outcome as indeterminate
  (for example, with a reason code such as `kid-not-found`) rather than as a
  definitive signature failure.
- If `kid` is present and maps ambiguously to more than one suitable key,
  implementations MUST treat the outcome as indeterminate (for example, with
  a reason code such as `kid-ambiguous`).
- Once a specific key has been selected and a verification attempt is made
  with that key, a failing verification MUST be reported as
  `rejected-signature`, not `indeterminate`.

Conforming implementations MUST support at least one key source type for
populating or resolving `key_material` from the following set:

- static or in-memory keysets configured locally (for example, via
  configuration or code), or
- HTTPS JWKS endpoints, or
- JWKS resolution via OIDC metadata.

Implementations MAY support more than one of these source types, and for each
supported source type they MUST support multiple configured instances (for
example, multiple static keys, multiple JWKS URLs, or multiple OIDC issuers).

This requirement to support at least one concrete key source type is an
intentional design choice for the base spec. The goal is to ensure that
conforming implementations are useful in common JWT deployment models (for
example, OIDC-style JWKS) while still allowing purely static or offline
deployments to satisfy the requirement via local keysets. Additional or more
opinionated key source requirements MAY be introduced by environment- or
ecosystem-specific profiles and bindings, but they build on top of this
baseline rather than replacing it with a purely abstract key_material handle.

For conformance and test harnesses, this spec defines a canonical binding:

- Conformance vectors reference key sets via a `key_set_id`.
- Each referenced key set is defined as a static JWK set (for example,
  `static_jwks.keys` in `conformance-vectors.yaml`) using standard JOSE JWK
  fields such as `kty`, `kid`, `alg`, and `k` for symmetric keys.
Implementations or adapters map this static representation into their
internal `key_material` structures when running conformance plans.

### Claims model – `claims_view`

Claim extraction and introspection use a `claims_view` object. It provides a
decoded view over header and payload together with validation tags:

- `header` – decoded header fields keyed by header name. Each field is
  represented as:
  - `value` – decoded value of the header field.
  - `validation_status` – one of `validated`, `partially_validated`,
    `unvalidated`.
  - `checked` – optional boolean flag indicating whether any validation
    checks were executed for this field.
  - `reason_codes` – optional list of reason codes explaining why a field is
    not fully validated.
- `claims` – decoded payload claims keyed by claim name. Each claim follows
  the same structure as header fields:
  - `value` – decoded value (string, number, boolean, array, or object).
  - `validation_status` – one of `validated`, `partially_validated`,
    `unvalidated`.
  - `checked` – optional boolean flag indicating whether any validation
    checks were executed for this claim.
  - `reason_codes` – optional list of reason codes for non-validated or
    partially validated claims.

Semantics of `validation_status`:

- `validated` – all mandatory checks for this field or claim have been
  performed and passed under the current `validation_policy`, profiles, and
  `key_material`.
- `partially_validated` – some checks ran and passed but others did not run
  or remain inconclusive (for example, a profile covers only part of the
  claim’s semantics, or full validation was skipped in a claims-only mode).
- `unvalidated` – no checks were performed for this field or claim or checks
  failed.

When `validation_status != validated`, implementations MUST either:

- provide a non-empty `reason_codes` list that explains why the field or
  claim is not fully validated; or
- use a binding/profile-level mechanism (for example, an explicit `checked`
  flag set to false) to document that the field or claim was deliberately
  left unvalidated.

This is intended to make it easier for callers and conformance tooling to
distinguish between \"never checked\" and \"checked but failed or remained
inconclusive\" cases.

The spec does not prescribe any particular set of claim names or token types.
Instead, callers express requirements through `validation_policy` and any
external profiles or templates they define. Typical usage includes:

- Defining, outside this spec, one or more claim profiles (for example,
  “access token profile A”) that specify which claims are required, their
  expected shapes, and any value constraints.
- Passing a `validation_policy` that references such a profile and may add
  additional constraints (for example, acceptable audiences).
- Interpreting `claims_view` based on those external profiles. This spec only
  requires that the library return decoded values and clear validation tags.

Normatively, this spec only names a small, generic set of optional keys under
`validation_policy`:

- `algorithms` – describes which algorithm identifiers are acceptable for a
  given validation call via `algorithms.allowed`. Identifiers MUST be JOSE
  `alg` names (for example, `HS256`, `RS256`) and callers SHOULD pin a small,
  explicit set. If no allowed algorithms are provided (and no profile
  supplies them), or if requested algorithms are incompatible with the
  selected key type, validators MUST fail with `rejected-policy`, not
  `indeterminate`.
- `clock` – carries time-related parameters such as
  `clock.now_epoch_seconds` (the reference time for checks) and
  `clock.leeway_seconds` for skew-tolerant checks. Time-based behaviour is
  defined in terms of these values.
- `expected_audience` / `expected_issuer` – express audience and issuer
  expectations for this invocation. Audience and issuer mismatch mappings
  derive from these fields.
- `profile_id` / `profile_refs` – may reference external claim profiles or
  bundles defined by the consumer.

All other policy fields remain implementation-defined. This is an intentional
design choice for this spec: it standardises only a minimal, generic policy
shape and explicitly does **not** define a full JWT policy language. Future
versions MAY introduce additional optional keys, but they are expected to
preserve the pattern that detailed claim semantics live in external profiles
or bundles, not directly in `validation_policy`. Implementations MAY reflect
both the generic keys above and any additional fields in `applied_policy` and
`audit_report` artefacts without this spec assigning ecosystem-specific
semantics to them.

In real deployments, callers SHOULD avoid hard-coding detailed claim and
policy semantics directly into application code. Instead, they SHOULD define
one or more local policy profiles or bundles (for example, per-issuer or
per-application profiles) outside this spec and reference them from
`validation_policy.profile_id` or `validation_policy.profile_refs`. A
deployment that claims conformance to this spec is expected to maintain such
local profiles as the primary source of truth for its JWT requirements.

Non-normative example (illustrative only):

- A consumer defines, in its own configuration, an access-token-oriented
  profile:

  ```yaml
  # Not part of this spec; example only
  access-token-profile-A:
    required_claims:
      sub:
        type: string
      aud:
        type: array-of-string
      scope:
        type: string
  ```

- A call to `validate_jwt` then supplies:

  ```yaml
  validation_policy:
    profile_id: "access-token-profile-A"
    expected_audience: ["example-client"]
    clock:
      leeway_seconds: 30
  ```

In this example, the meaning of `profile_id`, `required_claims`, and related
fields is defined by the consumer’s own configuration or bundles, not by this
spec. The JWT Validation spec only requires that the implementation apply the
supplied policy consistently and reflect its effect in `validation_result`
  and `claims_view`.

### Malformed tokens

Implementations MUST treat syntactically malformed inputs as valid, in-scope
inputs to the operations in this spec. A `jwt_token` that is not a
syntactically valid compact JWT (for example, wrong number of segments,
invalid base64url encoding, or non-JSON payload) MUST result in:

- `validation_result.status: rejected-malformed`, and
- an omitted or empty `claims_view`.

This applies equally to `validate_jwt` and `extract_claims`. Callers MAY rely
on this behavior rather than attempting to pre-parse or pre-validate JWTs
themselves. The `jwt-malformed` example vector in `examples/vectors.yaml`
illustrates this case.

When `validation_policy.claims.allow_on_failure` is `false` or absent and
validation fails, implementations are expected to omit or empty `claims_view`
(subject to any narrow diagnostic allowances defined in profiles). When
`validation_policy.claims.allow_on_failure` is `true`, implementations MAY
return a populated `claims_view` even on failure. In that case:

- all fields MUST be tagged as `unvalidated` or at most `partially_validated`,
  and
- callers MUST treat these values as diagnostic or informational only, not as
  authoritative inputs to security decisions or as a source of validated
  claims for downstream authorization logic. Profiles that opt into
  claims-on-failure behaviour MAY further restrict which failure modes are
  eligible to return claims_view, but they MUST NOT weaken this
  diagnostics-only requirement.

### Operation summaries

- `validate_jwt(jwt_token, validation_policy, key_material)`:
  - On success:
    - `validation_result.status` is `valid`.
    - `claims_view` SHOULD reflect claims that have been fully validated
      according to `validation_policy` and available `key_material`.
  - On failure:
    - If `jwt_token` is syntactically malformed, `validation_result.status`
      is `rejected-malformed` and `claims_view` is omitted or empty.
    - `validation_result.status` indicates the primary failure mode.
    - `validation_result.reason_codes` MAY contain multiple codes when several
      checks fail.
    - `claims_view` MAY be omitted, empty, or populated with tagged claims,
      depending on `validation_policy.claims.allow_on_failure` and any
      applicable profiles.
- `extract_claims(jwt_token, validation_policy)`:
  - Always attempts to decode header and payload when the token is
    syntactically valid.
  - Tags each field in `claims_view` according to which checks were
    performed and which succeeded.
  - When full validation (including signature/MAC verification and the
    policy checks required for `validate_jwt`) is not performed for an
    invocation, it MUST set `validation_result.status` to `indeterminate`
    and SHOULD include a reason code such as `claims-only-mode` (except for
    malformed-token cases, which still use `rejected-malformed`).
  - May return an empty or omitted `claims_view` on failure when
    `validation_policy.claims.allow_on_failure` is `false` or absent.

Both operations MUST clearly distinguish `validated` fields from
`unvalidated` or `partially_validated` ones so that callers can make policy
decisions without guessing.

## Conformance Model

This spec defines conformance in terms of classes and plans that can be used
by libraries or services that implement JWT validation and claim extraction.
The machine-readable source of truth is `conformance.yaml`, referenced from
`spec.yaml` under `normative_bundles`.

### Conformance classes

At minimum, this spec recognizes the following conformance classes:

- `jwt-validator-core` – implements `validate_jwt` with the structured
  `validation_result` model and basic handling of time-based and structural
  requirements.
- `jwt-validator-claims` – satisfies `jwt-validator-core` and additionally
  implements `extract_claims` with `claims_view` tagging for header and
  payload fields.
- `jwt-validator-audit` – supports `run_conformance_audit` and produces
  structured `audit_report` artefacts suitable for manual review and
  automated drift detection.

Implementations may claim conformance to one or more classes. At minimum, a
library that claims conformance to this spec SHOULD implement
`jwt-validator-core`. Support for `jwt-validator-claims` and
`jwt-validator-audit` is optional and layered: implementations that claim
those classes MUST satisfy the corresponding requirements in
`conformance.yaml`, but they are not required for a basic, validation-only
library. In practice, a minimal library might only target
`jwt-validator-core`, while a more comprehensive validator targets all
three.

### Audit reports – `audit_report`

The `run_conformance_audit` operation produces an `audit_report` object. It
is intended to be reproducible for a given implementation version,
conformance plan, and key material.

Key sections of `audit_report` include:

- `implementation` – identifies the implementation under test, including at
  least an `id` and `version`.
- `spec_version` – states which spec version the implementation claims to
  conform to (for example, `sdd.security.jwt.validation@0.1.0`).
- `plan_id` – identifies the conformance plan or vector set used for the
  run.
- `summary` – provides an overall `status` in {`pass`, `fail`,
  `indeterminate`} together with aggregate `vector_counts` (total, passed,
  failed, indeterminate, and drift-detected).
- `vectors` – contains per-vector outcomes, each with:
  - `id` – referencing a vector from a plan or examples file.
  - `status` – `pass`, `fail`, `indeterminate`, or `drift`.
  - `expected` – high-level expected outcome (for example, expected
    `validation_result.status` and key reason codes).
  - `observed` – corresponding outcome observed from the implementation.
  - `notes` – optional narrative detail.
- `drift_indicators` – optional high-level summaries of behavioural drift
  across groups of vectors.
- `extensions` – optional extension area for implementation- or
  deployment-specific fields; contents are non-normative.

This structure is intended to be **portable across independent
implementations** that claim the `jwt-validator-audit` class: the fields
above form a small, normative core schema that conformance tooling can rely
on when comparing or aggregating audit runs. Implementations MAY add fields
under `extensions` without affecting conformance, provided they do not
contradict the normative fields above.

Conformance claims SHOULD reference both the spec and conformance class, for
example: “Conformant to `sdd.security.jwt.validation@0.1.0`, class
`jwt-validator-core`.”

## Examples and Walkthroughs (optional)

`conformance-vectors.yaml` contains normative conformance vectors that
exercise the result model and conformance classes. For example:

- `jwt-valid-basic` – a structurally valid, correctly signed JWT that
  satisfies a simple policy and yields `validation_result.status: valid`.
- `jwt-valid-basic-claims-view-tags` – extends the basic-valid scenario by
  additionally asserting `claims_view` tagging for core header fields and
  payload claims (for example, `alg`, `typ`, `iss`, `sub`, `aud`, `exp`,
  `iat` all tagged as `validated`) under successful validation.
- `jwt-expired` – a correctly signed JWT that fails due to an `exp` in the
  past and yields `validation_result.status: rejected-expired`.
- `jwt-invalid-signature` – a structurally valid JWT whose signature or MAC
  does not verify, yielding `validation_result.status: rejected-signature`.
- `jwt-wrong-audience` – a structurally valid, correctly signed JWT whose
  `aud` claim does not satisfy the policy and yields
  `validation_result.status: rejected-audience`.
- `jwt-claims-on-failure-allowed` – demonstrates that when
  `validation_policy.claims.allow_on_failure` is true, an implementation may
  return `claims_view` on validation failure, tagging fields as unvalidated
  and optionally including `raw_without_signature` for diagnostics.
- `jwt-claims-on-failure-disallowed` – demonstrates that when
  `validation_policy.claims.allow_on_failure` is false or absent, claims are
  omitted or emptied on failure, even though the token is still available to
  the implementation for local logging.

Unlike earlier schematic examples, the conformance vectors in
`conformance-vectors.yaml` use concrete compact JWT strings signed with
static test keys and an explicit `clock.now_epoch_seconds`. Conformance
plans in `conformance.yaml` are defined in terms of these concrete vectors so
that independent implementations can run the same tests and compare
behaviour deterministically.
