# Spec Analysis Gate – SDD Specs

Use this checklist for each spec unit or bundle before accepting substantial changes (new semantics, new requirements, or breaking changes).

## Inputs

- Spec unit directory under `specs/` (including `spec.yaml`, `spec.md`, and any examples/bundles).
- Any referenced bundles under `bundles/` or within the spec directory.
- The spec’s local `open-questions.md` file.
- Repository docs: `docs/specs-constitution.md`, `docs/repo-vision.md`, `docs/sdd-principles.md`, `docs/style-guide.md`, `docs/authoring-guidelines.md`.

---

## Analysis Gate (Pre-Change)

Run this section **before** finalising changes to the spec.

1. **Specification completeness**
   - [ ] The intent, scope, and key behaviours of the spec unit are described in `spec.md` (Overview/Concepts/Behavior sections as appropriate).
   - [ ] `spec.yaml` contains a clear ID, title, status, and domain, and any required fields from `schemas/spec.schema.yaml` are populated.
   - [ ] Supporting bundles (if any) referenced from `spec.yaml` exist and are linked correctly.

2. **Open questions review (Clarification Gate)**
   - [ ] The spec has a local `open-questions.md` file using the repository template.
   - [ ] No blocking `Open` entries remain in that file for the change being made. If any exist, pause and obtain clarification before proceeding.
   - [ ] For medium- and high-impact questions, planned resolutions are captured as edits to normative sections in `spec.yaml`, bundles, or `spec.md`.

3. **Cross-artefact alignment**
   - [ ] Narrative text in `spec.md` matches the normative semantics in `spec.yaml` and any referenced bundles; there are no contradictions.
   - [ ] Examples, test vectors, or walkthroughs (if present) are consistent with the main spec and clearly marked informative vs normative.
   - [ ] Catalog entries under `catalog/` that reference this spec (if any) use the correct ID, path, and status.

4. **Constitution compliance**
   - [ ] The change respects `docs/specs-constitution.md` and `docs/sdd-principles.md` (spec-first, implementation-neutral, ambiguity clarified before change).
   - [ ] No implementation-specific details (framework names, build commands, environment-specific configs) have leaked into this repository’s specs.

Only proceed when every checkbox is satisfied or explicitly deferred with owner approval recorded outside this repository (for example in an implementation repo’s plan or ADR).
