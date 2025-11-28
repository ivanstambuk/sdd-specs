# Agent Consumption & Repository Maintenance (Non-Normative)

This document is **non-normative**. It gives process-level guidance for:

- AI/LLM and code-generation agents that consume ProfileSchema-based specs in this repository, and
- human maintainers who edit specs and operate CI and tooling.

Behavioral and conformance requirements remain defined only by each spec unit’s
`spec.yaml`, its normative profile documents (such as `profile-spec.md`), and
any associated bundles (`profile-core.yaml`, `conformance.yaml`); this file
must not be treated as a source of normative cryptographic requirements.

## 1. Agent Consumption Guide (Tool Pipeline)

For ProfileSchema-based profiles such as the TurboSHAKE / KT / HopMAC profile:

- Agents should treat the ProfileSchema bundle (`profile-core.yaml`) and the
  conformance bundle (`conformance.yaml`) as the **canonical machine-readable
  sources** for:
  - types and notation,
  - `Constraints` (parameter ranges, defaults, error categories),
  - API Contracts and Algorithm definitions,
  - Error Model / Context* blocks,
  - FR/NFR tables and `ConformanceCriteria`,
  - structural metadata (`SpecIndex`, `ExternalSpecs`, `ExternalTestSuites`,
    `ExternalTestVectors`, `ProfileSchemaMeta`, `ProfileSchemaInvariants`,
    `IdTypes`, `ImplementationChecklist`).
- Markdown profile documents such as
  `specs/protocols/crypto/turboshake-kt-hopmac-rfc9861-profile/profile-spec.md`
  are the **human-readable index and commentary**:
  - YAML snippets and tables in those files are views over the bundles.
  - If a snippet disagrees with the bundles, agents should treat the bundles as
    canonical and the snippet as a spec bug to be fixed.
- A typical agent pipeline for a ProfileSchema-based profile is:
  1. Load `profile-core.yaml` and validate it against the repository schemas.
  2. Load `conformance.yaml` and any external test-vector indices referenced by
     the ProfileSchema.
  3. Build an internal model of:
     - `Constraints` for all relevant parameters,
     - API Contracts and Algorithms for each primitive/context,
     - Error categories and context lifetime/independence rules,
     - FR/NFR entries and `ConformanceCriteria`.
  4. Use that model to generate implementations and tests in the target
     language(s), treating:
     - `Constraints` + API/Algorithm + Error Model as the **behavioral core**,
     - FR/NFR tables as the **obligation index** (what must be implemented and
       tested for each primitive),
     - `ConformanceCriteria` as the machine-readable definition of what it
       means to “claim profile conformance”.
  5. Optionally, consult profile-specific “How an Agent Uses This Specification”
     or “LLM Implementation Contract” sections inside `profile-spec.md` for
     additional implementation-planning guidance. Those sections are advisory
     only and must not override the behavioral core or bundles.

### Reading Order Hints

When working on the TurboSHAKE / KT / HopMAC profile, an agent-friendly reading
order is:

1. `profile-core.yaml` – ProfileSchema bundle (types, constraints, APIs,
   algorithms, Error Model, FR/NFR, conformance criteria).
2. `conformance.yaml` – conformance and test-vector bundle.
3. `profile-spec.md` – normative profile text for humans and agents:
   - Scope & Goals,
   - the normative profile sections through “Test Vectors & Conformance”,
   - FR/NFR tables.
4. `spec.yaml` / `spec.md` – spec-unit metadata and high-level narrative.
5. Non-normative design notes such as
   `specs/protocols/profile-design-notes.md` for deeper rationale.

Agents remain **advisory consumers** in this repository: conformance is defined
for implementations only. Agent pipelines should be designed so that any human
implementation that satisfies the behavioral core and conformance criteria is
equally conformant, regardless of whether it was produced by an agent.

## 2. Repository Maintenance & CI (ProfileSchema-Based Specs)

This section summarizes recommended maintenance practices for spec units that
use ProfileSchema bundles (for example, the TurboSHAKE / KT / HopMAC profile).
It is aligned with the repo-level docs under `docs/` (especially
`specs-constitution.md`, `repo-vision.md`, and `spec-analysis-gate.md`).

- **Source of truth for normative changes.**
  - Treat the ProfileSchema bundle (`profile-core.yaml`) as the canonical
    normative artifact for behavioral core and indices.
  - When a normative fact changes (parameter bounds, error semantics, API
    contracts, algorithms, Error Model, FR/NFR, conformance criteria), update
    the ProfileSchema first, then adjust derived views (`profile-spec.md`,
    `conformance.yaml`, checklists) to match.
- **Editing pattern.**
  - Prefer structured edits to the YAML bundles (via agents or careful manual
    edits) over free-form Markdown changes.
  - Use `profile-spec.md` to keep the human-readable narrative in sync with the
    bundles; avoid introducing behavior only in prose.
  - Keep `spec.yaml` and `spec.md` consistent with the bundles and with the
    repository-wide authoring guidelines and style guide.
- **Textual fixes.**
  - Humans may apply local textual fixes directly in `profile-spec.md` (typos,
    clarifications, paragraph moves) as long as:
    - they do not introduce new behavioral requirements, and
    - they do not contradict the ProfileSchema or conformance bundles.
  - If a textual change reveals that the ProfileSchema is incomplete or
    inconsistent, update the bundle and re-align the prose.
- **CI and validation.**
  - Before finalizing changes, maintainers are encouraged to run:
    - `./tools/validate-specs.sh` (structural/spec-schema checks),
    - `./tools/validate-bundles.sh` (bundle-schema checks).
  - For ProfileSchema-based specs, CI or local tooling should also:
    - evaluate `ProfileSchemaInvariants` and `ProfileSchemaInvariantsRole`
      against `profile-core.yaml`,
    - ensure that FR/NFR tables and indices match the canonical IDs and
      constraints in the bundle,
    - keep `conformance.yaml` consistent with the ProfileSchema’s
      `ExternalTestSuites` / `ExternalTestVectors` and any local test-vector
      definitions.
- **Scope boundaries.**
  - Keep this repository focused on specifications and bundles only:
    - do not add implementation code, build systems, or runtime configs here;
      those belong in downstream implementation repos.
  - Use `open-questions.md` in each spec unit as a temporary scratchpad for
    unresolved questions, and clear it once decisions are reflected in
    normative artifacts, per `specs-constitution.md`.

These practices are meant to make ProfileSchema-based specs easy to maintain and
safe to consume by both humans and agents, without turning the profile text
itself into a process or CI manual.

