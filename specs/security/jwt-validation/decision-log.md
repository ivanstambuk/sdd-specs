# Decision Log – JWT Validation

This file is **non-normative**. It records resolved design questions and
decisions for this spec unit, together with short rationales and stable local
IDs. It complements, but does not replace, the normative artefacts:

- `spec.yaml`
- `spec.md`
- Any supporting bundles or schemas referenced from `spec.yaml`

Normative behavior and conformance remain defined solely by those artefacts
and by the external standards they reference. This file exists to help future
readers understand **why** specific choices were made.

## How to use this log

- Each decision entry gets a local ID `D-xxx` (for example, `D-001`), scoped to
  this spec unit.
- Normative specs may refer to these IDs in non-critical commentary (for
  example, “see decision D-001 for rationale”), but must not depend on this
  file to define behavior.
- When a decision is revised in a later version of the spec:
  - Add a new entry with a new ID describing the updated decision.
  - Keep the previous entry, marking it as superseded and pointing to the new
    ID.

## Decisions

- D-001 – Scope and ID for JWT Validation

  - Summary: The `sdd.security.jwt.validation` spec unit covers three related
    facets under a single ID: (1) core JWT validation against keys and policy,
    (2) claim extraction, including the ability to obtain tagged claims even
    when full validation does not succeed, and (3) a conformance/audit mode
    suitable for detecting drift in manual implementations via structured
    reports.
  - Rationale: Keeping these facets together under one spec ID simplifies
    validator generation, clarifies the relationship between validation and
    conformance tooling, and ensures that claim extraction semantics are
    specified alongside validation policy rather than in a separate spec.
    For version `0.1.0`, this combined scope is an explicit governance choice;
    any future split (for example, moving the audit harness into a dedicated
    spec unit or profile) would be treated as a new spec unit or a
    non-backwards-compatible evolution rather than a silent restructuring.

- D-002 – Result model and audit structure

  - Summary: The spec adopts a compact `validation_result` model with a small
    enumerated `status` field (for example, `valid`, `rejected-expired`,
    `rejected-audience`) backed by a `reason_codes` list for additional
    detail, and a `claims_view` that tags each header field and claim as
    `validated`, `partially_validated`, or `unvalidated`. Audit reports
    (`audit_report`) use a structured but extensible shape with core fields
    for implementation identity, spec version, plan ID, summary, per-vector
    results, and optional drift indicators and extensions.
  - Rationale: This balances expressiveness with implementability: callers
    can branch on a small set of stable statuses and reason codes, while
    implementations can provide enough structure for conformance tooling and
    drift detection without modelling a full per-check graph. The model
    remains agnostic to specific ecosystems such as OIDC, allowing claim
    profiles and token types to be defined externally.

- D-003 – Structure of validation_policy

  - Summary: The spec defines `validation_policy` as a structured object with
    a small set of optional, generic keys (`algorithms`, `clock`,
    `profile_id`, and `profile_refs`) and leaves all other fields
    implementation-defined. The named keys cover common concerns such as
    acceptable algorithms, basic clock configuration (for example,
    `leeway_seconds`), and references to external claim profiles or bundles.
  - Rationale: This provides a minimal amount of cross-implementation
    structure for tooling and conformance without introducing a full policy
    language or baking in ecosystem-specific semantics. Consumers remain free
    to define their own claim profiles and additional policy fields in
    downstream configuration or bundles.

- D-004 – Key material sources and baseline requirement

  - Summary: The spec treats `key_material` as an abstract handle for
    verification keys but **deliberately** requires that conforming
    implementations support at least one concrete key source type from a
    small list (static or in-memory keysets, HTTPS JWKS endpoints, or JWKS
    resolution via OIDC metadata). Implementations MAY support multiple such
    source types and multiple configured instances for each.
  - Rationale: This anchors the spec in real-world JWT deployment models
    (especially JWKS- and OIDC-style ecosystems) while still allowing purely
    static or offline deployments to conform via local keysets. The structure
    of `key_material` remains implementation-defined so that different
    environments can map their own key management representations to the
    abstract handle, and more opinionated or environment-specific key source
    requirements can be defined in separate profiles or bindings without
    weakening this baseline.

- D-005 – Reason code vocabulary and stability

  - Summary: The spec defines `validation_result.reason_codes` as an optional,
    machine-readable list of diagnostic strings with **RECOMMENDED but not
    mandatory** example values (such as `expired`, `audience-mismatch`,
    `issuer-mismatch`, `kid-not-found`, `kid-ambiguous`,
    `signature-verification-failed`, and `claims-only-mode`). It does not
    establish a closed or strictly normative global registry of code values;
    interoperability and conformance rely primarily on the `status` field.
  - Rationale: This allows implementations and ecosystems to converge on
    useful, semi-standard names where practical while preserving flexibility
    for local extensions and existing deployments. Cross-implementation tools
    can branch reliably on `status` and optionally recognise common
    reason-code strings when present, and ecosystem-specific profiles or
    bindings remain free to tighten or extend the vocabulary without having to
    revise the core spec.

- D-006 – Audit surface scope and portability

  - Summary: The spec treats `run_conformance_audit` and `audit_report` as a
    normative, cross-implementation audit surface for the `jwt-validator-audit`
    class. The core fields of `audit_report` (implementation identity,
    spec_version, plan_id, summary, per-vector outcomes, drift_indicators) form
    a small, stable schema that independent implementations and tooling stacks
    are expected to share, while an `extensions` area remains non-normative and
    deployment-specific.
  - Rationale: This enables meaningful comparison and aggregation of audit runs
    across different implementations without preventing local ecosystems from
    adding their own diagnostic detail. Conformance tooling can rely on the
    core schema when evaluating `jwt-validator-audit` implementations, and
    future evolution can add optional fields or profile-specific extensions
    without breaking the baseline audit format.

- D-007 – Claims-on-failure behaviour and diagnostics-only scope

  - Summary: The spec allows `claims_view` to be returned on validation
    failure only under the control of `validation_policy.claims.allow_on_failure`
    and only with all returned fields tagged as `unvalidated` or
    `partially_validated`. Any claims_view produced on failure is explicitly
    scoped to diagnostic or informational use and MUST NOT be treated as
    providing validated inputs for security or authorization decisions. Profiles
    may further restrict which failure modes are eligible to return
    claims_view, but they may not relax the diagnostics-only constraint.
  - Rationale: This preserves useful debugging and observability behaviour for
    deployments that need to inspect failing tokens while reducing the risk of
    security foot-guns. Tagging and diagnostics-only semantics make it clear
    that these values cannot be used as a substitute for successful validation,
    and ecosystem-specific profiles remain free to tighten, but not weaken, the
    base guarantees.

- D-008 – Deterministic conformance vectors bundle

  - Summary: The spec introduces a normative `conformance-vectors.yaml` bundle
    referenced from `spec.yaml` and `conformance.yaml`. This bundle defines
    concrete JWT compact strings, a fixed validation clock instant, and
    canonical key_material sets for conformance. Conformance plans in
    `conformance.yaml` now reference these vector IDs rather than schematic
    examples, covering core statuses (valid and various rejection modes) plus
    key edge cases such as kid-not-found and kid-ambiguous.
  - Rationale: Moving from schematic vectors to a normative, concrete vector
    bundle makes conformance executable and deterministic across independent
    implementations. Different libraries run the same tests against the same
    signed tokens, clock instant, and key sets, which addresses the criticism
    that two implementations could previously \"pass\" while exercising
    different behaviours and token shapes.

- D-009 – Validation clock injection and time boundary semantics

  - Summary: The spec now standardises `validation_policy.clock.now_epoch_seconds`
    as the reference time for all time-based checks and adopts explicit,
    fail-closed inequalities for exp/nbf (with leeway). Boundary conditions
    such as exp == now and nbf == now are made precise, and missing or
    ill-typed time claims that are required by policy or profile are treated
    as `rejected-policy` rather than being left to implementation discretion.
    Conformance vectors exercise both non-boundary and boundary cases as well
    as leeway behaviour.
  - Rationale: Time semantics are a frequent source of subtle drift between
    implementations. Making the validation clock explicit and formalising the
    inequalities closes ambiguity around equality cases and leeway handling.
    Tying missing/ill-typed required time claims to a clear policy error
    improves safety and makes conformance tooling capable of detecting
    off-by-one and skew-related divergence.

- D-010 – JOSE algorithm identifiers and allowlist enforcement

  - Summary: Algorithm identifiers in `validation_policy.algorithms.allowed`
    are now required to use JOSE `alg` names (such as `HS256`, `RS256`), with
    an explicit expectation that callers pin a small allowlist. If no allowed
    algorithms are specified (and no profile supplies them), or if the
    configured algorithms are incompatible with the selected key type,
    validators MUST treat this as a policy error and return `rejected-policy`
    (for example, using reason codes like `alg-none-disallowed` or
    `algorithm-not-allowed`). Conformance vectors cover disallowed `alg: none`
    and mismatched algorithms relative to the allowlist.
  - Rationale: Treating algorithm identifiers as implementation-defined was
    incompatible with portable conformance and created room for dangerous
    negotiation behaviours. Anchoring on JOSE `alg` names and requiring
    explicit allowlists makes implementations more interoperable and safer,
    while still allowing ecosystem-specific profiles to introduce additional
    algorithms in a controlled way.

- D-011 – Audience and issuer policy keys and mismatch statuses

  - Summary: The spec now standardises `validation_policy.expected_audience`
    (array of acceptable audiences) and `validation_policy.expected_issuer`
    (single expected issuer identifier) as optional policy keys. The
    `rejected-audience` and `rejected-issuer` statuses are normatively tied
    to these fields, and conformance vectors exercise both wrong-audience and
    wrong-issuer cases under pinned policy. This aligns the status vocabulary
    with explicit, portable policy knobs rather than leaving the inputs
    implicit or implementation-defined.
  - Rationale: Previously, the spec defined audience/issuer mismatch statuses
    without standardising how callers expressed those expectations. This made
    cross-implementation conformance for `rejected-audience` and
    `rejected-issuer` fragile. Introducing explicit expected_audience and
    expected_issuer fields provides a simple, generic mechanism that profiles
    and bindings can build on while keeping the core spec ecosystem-agnostic.

- D-012 – Canonical static_jwks binding and indeterminate outcomes

  - Summary: While `key_material` remains abstract for production use, the
    conformance vector bundle now defines a canonical `static_jwks`-based
    binding and a notion of `key_set_id` that identifies specific JWK sets.
    Dedicated key sets cover both the single-key case and an ambiguous kid
    scenario. Vectors exercise kid-not-found and kid-ambiguous cases, which
    are required to yield `validation_result.status: indeterminate` with
    appropriate reason codes. The spec also clarifies that callers MUST treat
    `indeterminate` as non-valid for authorization decisions and introduces a
    claims-only-mode vector where `indeterminate` is used to represent
    decoding without full validation.
  - Rationale: A purely abstract key_material handle was insufficient for
    portable conformance, especially for multi-key and kid-handling semantics.
    Providing a concrete, minimal JWK-based binding for test vectors lets
    conformance tooling and adapters agree on key shapes without constraining
    production deployments. Strengthening the `indeterminate` semantics and
    exercising them in vectors addresses known foot-guns around tri-state
    validation outcomes and claims-only inspection modes.

- D-013 – Claims_view tagging semantics and diagnostics

  - Summary: The spec now gives precise semantics for `claims_view` tag
    values: `validated` means all mandatory checks for a field/claim have
    been performed and passed under the current policy, profiles, and keys;
    `partially_validated` means some checks ran and passed but others did not
    run or remain inconclusive; `unvalidated` means no checks were performed
    or checks failed. Implementations are encouraged to populate
    `reason_codes` whenever a field or claim is not fully validated, and the
    conformance vector set includes scenarios (such as profile-driven missing
    claims and type mismatches) that are expected to surface as
    `rejected-policy` with appropriate reason codes.
  - Rationale: Without clear semantics, the tri-state tagging model risked
    divergent interpretations across implementations and made it harder for
    consumers and tooling to understand which data was actually trustworthy.
    Tightening these definitions improves both safety and interoperability
    while preserving flexibility for profiles to define what \"mandatory
    checks\" mean for specific claims and token types.

- D-015 – Focused audit depth and claims_view coverage (Q-013)

  - Summary: In response to GPT‑5 Pro's result/audit-depth critique, the
    spec introduces a small, focused expansion of conformance coverage rather
    than a broad new test harness. The `claims-and-failure-modes` plan now
    includes an additional vector (`jwt-valid-basic-claims-view-tags`) that
    asserts `claims_view` tagging for core header and payload fields under a
    successful validation scenario, while `audit_report` structure and
    `summary.vector_counts` semantics remain fully specified in `spec.yaml`
    and exercised via the existing `audit-smoke-test` plan. Deeper coverage
    for edge cases such as duplicate JSON keys is intentionally deferred to
    future iterations or ecosystem-specific bindings.
  - Rationale: This targeted expansion raises the floor on interoperability
    for claim-level tagging and audit summaries without significantly
    increasing the complexity of the conformance suite. It provides a clear,
    concrete example for implementers and tooling to align on, while leaving
    room for future specs or bindings to introduce more exhaustive audit
    depth where needed.

- D-014 – Scope of the P2 schema-precision pass (Q-012)

  - Summary: For version `0.1.0`, the P2 schema-precision work for
    `sdd.security.jwt.validation` is deliberately limited to tightening
    `spec.yaml` itself: key inputs/outputs (such as `jwt_token`,
    `validation_policy`, `key_material`, `validation_result`, `claims_view`,
    and `audit_report`) now have explicit required/optional/nullability
    guidance expressed directly in their constraints. Per-claim and per-header
    entries in `claims_view` also state which fields are required
    (`value`, `validation_status`) and which are optional
    (`checked`, `reason_codes`). Dedicated JSON Schema or OpenAPI artefacts
    for the data model are intentionally deferred to a future iteration
    rather than being introduced in this version.
  - Rationale: Clarifying presence and nullability rules directly in
    `spec.yaml` strengthens the machine-readable contract and addresses the
    most practical aspects of GPT‑5 Pro’s schema-precision critique without
    over-extending the scope of this spec unit. Keeping JSON Schema/OpenAPI
    artefacts out of the initial `0.1.0` release avoids locking in codegen or
    transport-specific shapes too early; downstream bindings and ecosystems
    remain free to derive schemas from the spec’s abstractions as needed,
    provided they stay faithful to the normative structure defined here.
