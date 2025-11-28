# SDD Specs – Repository Constitution

This document governs how this repository evolves. It encodes the
spec-driven development (SDD) workflow and guardrails for **specs only**:
there is no implementation code here.

## Principles

- Specifications, profiles, and bundles in this repo are the **single source of truth** for the behaviours they describe. Downstream implementations, tasks, and tests in other repos must follow these specs.
- Keep this repository **implementation-neutral and technology-agnostic**. Language- and stack-specific choices belong in profiles or downstream repos, not in core specs.
- Clarify ambiguity first. For each spec unit, use its local `open-questions.md` file to record open questions before making non-trivial changes.
- When a medium- or high-impact question is resolved, first update the governing spec’s normative artefacts (`spec.yaml`, supporting bundles, and any normative sections in `spec.md`), then clean up the spec’s `open-questions.md` so it contains only active questions.
- Keep increments small and verifiable: prefer focused changes to a single spec unit or catalog entry at a time, with a clear intent captured in commit messages or session notes.
- Governance artefacts in this repo are: this constitution, `docs/repo-vision.md`, `docs/sdd-principles.md`, `docs/style-guide.md`, `docs/authoring-guidelines.md`, and per-spec `open-questions.md` files.

## Roles

- Spec maintainers: own spec architecture, versions, and compatibility.
- Contributors (including agents): propose spec and catalog changes aligned with these principles and the SDD workflow.

## Clarification Gate

Before making non-trivial changes to a spec unit (new requirements, semantics, or breaking changes):

- Read the existing spec unit (`spec.yaml`, `spec.md`, examples, bundles) and relevant docs under `docs/`.
- Check the spec’s local `open-questions.md` file; if one does not exist yet, create it from the template in `specs/_template-spec-unit/open-questions.md`.
- If ambiguity remains, add a new row to that spec’s `open-questions.md` and pause for clarification rather than guessing semantics.
- Do not “paper over” ambiguities in narrative text; resolve them in the normative artefacts.

## Quality for Specs

- For new or changed behaviour, enumerate success, validation, and failure branches in the spec or examples as appropriate for the domain (protocols, APIs, algorithms, components, etc.).
- Keep spec metadata (`spec.yaml`), narrative (`spec.md`), and any supporting bundles (for example profile or conformance bundles) aligned: no conflicting meanings across artefacts.
- When a spec serves as the normative source for other repos, clearly document external dependencies and expectations so consumers can implement consistent quality gates on their side.

## Gates

- Use the **Spec Analysis Gate** (`docs/spec-analysis-gate.md`) before accepting substantial changes to a spec unit or bundle. This gate focuses on spec completeness, ambiguity, and cross-artefact alignment.
- This repository does **not** define an Implementation Drift Gate or CI build gate; those belong in implementation repos that consume these specs.

