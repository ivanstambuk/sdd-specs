# SDD Specs

This repository contains SDD-style specifications, implementation profiles, and
bundles. It is intentionally spec-only: no tasks, no tickets, no implementation
code. At this stage it ships **templates only** so you can create new specs and
bundles from a clean starting point.

Key directories:

- `specs/` – spec-unit templates and, later, concrete spec units.
- `catalog/` – templates for indices of specs, profiles, and bundles.
- `schemas/` – JSON Schemas for specs, profiles, and bundles.
- `bundles/` – templates (and later concrete files) for bundles.
- `tools/` – validation and linting helpers.

To start a new spec, copy `specs/_template-spec-unit/` to your desired location
under `specs/` and replace placeholder values. For a new bundle, copy
`bundles/bundle.template.yaml`.

To enable local commit message linting and pre-commit checks, install `gitlint`
and optionally `gitleaks`, then configure Git to use the provided hooks:

```bash
git config core.hooksPath githooks
```

With hooks enabled:

- `githooks/commit-msg` runs `gitlint` using `.gitlint`.
- `githooks/pre-commit` runs `tools/validate-specs.sh`,
  `tools/validate-bundles.sh`, and (if installed) `gitleaks protect` against
  staged changes.
