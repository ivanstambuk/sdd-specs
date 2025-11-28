# Contributing

- Do not add implementation code, tasks, or tickets to this repository.
- When creating a new spec unit, copy `specs/_template-spec-unit/` and treat
  the resulting `spec.yaml` as canonical.
- Keep catalogs in `catalog/` in sync when adding specs, profiles, or bundles,
  using the `*.template.yaml` files as reference.
- Run `./tools/validate-specs.sh` and `./tools/validate-bundles.sh` before
  opening a change.
