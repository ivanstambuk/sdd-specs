# PLACEHOLDER_TITLE

> Spec ID: `sdd.<domain>.<area>.<name>`

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
  referenced from `spec.yaml` or from those bundles.

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

PLACEHOLDER_OVERVIEW_TEXT

## Concepts

- PLACEHOLDER_CONCEPT_1
- PLACEHOLDER_CONCEPT_2

## Behavior and Interfaces (optional)

Describe the externally observable behavior of this spec unit using structured
prose, state diagrams, or pseudo-code as appropriate. For example:

- For protocols or APIs: endpoints, messages, state transitions, and error
  semantics.
- For libraries or algorithms: inputs, outputs, error conditions, and key
  invariants.

This section should align with the behavior and operations captured in
`spec.yaml` but avoid language-specific details or library names.

## Conformance Model (optional)

If this spec unit defines conformance, describe it here. For example:

- What entities can claim conformance (for example, libraries, services,
  profiles, artefacts)?
- Which parts of the spec must be satisfied for behavioral conformance?
- Whether there is any notion of schema-level or artefact-level conformance
  (for example, for machine-readable bundles), and what it means.

Conformance definitions should reference a concrete spec version (for example,
“conformant to `<spec-id>` version X.Y.Z”) and should not depend on process
documents or repository policies.

## Examples and Walkthroughs (optional)

Describe one or more examples or walkthroughs that exercise the behavior of
this spec unit (for example: typical flows, API calls, protocol traces, or
references to entries in `examples/vectors.yaml` if present).
