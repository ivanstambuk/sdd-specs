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
