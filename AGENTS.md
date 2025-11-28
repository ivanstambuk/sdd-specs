# Codex / AI Agent Guide

This repository is **spec-only**. It contains SDD-style specifications,
profiles, bundles, and supporting schemas/scripts – **no implementation code,
no tickets, no tasks**.

The goal for any AI agent working here is to:

- Help authors create and maintain high-quality specs.
- Keep indices and schemas in sync with added/changed specs, profiles, and bundles.
- Avoid turning this repo into an application codebase.

## Repository Layout

- `specs/` – spec-unit templates and concrete spec units (each unit is a directory with `spec.yaml` + `spec.md` and optional `examples/`, `profiles/`).
- `catalog/` – index YAMLs for specs, profiles, and bundles. Keep these consistent with the contents of `specs/` and `bundles/`.
- `bundles/` – bundle YAMLs composing specs + profiles.
- `schemas/` – JSON Schemas for specs, bundles, and profiles.
- `tools/` – helper scripts for validation and linting (can be extended, but should stay small and focused).
- `docs/` – repository vision, style guide, authoring guidelines, SDD principles, and this repo’s constitution and gates. Treat these as normative for writing specs.

## Editing Rules

- Do **not** add:
  - Application or library code.
  - Task trackers (issues in files), ticket backlogs, or project plans.
  - Build systems or runtime configs unrelated to spec validation.
- Prefer **small, local changes** that align with:
  - `docs/style-guide.md`
  - `docs/authoring-guidelines.md`
  - `docs/sdd-principles.md`
  - `CONTRIBUTING.md`
- When editing a spec unit:
  - Treat `spec.yaml` as the canonical, normative definition.
  - Keep `spec.md` in sync as a human-readable companion (no conflicting meaning).
  - Preserve implementation-neutral, technology-agnostic language.
- When adding a new spec unit:
  - Copy `specs/_template-spec-unit/` into an appropriate directory under `specs/`.
  - Replace all placeholder values in `spec.yaml`, `spec.md`, `open-questions.md`, and any example/profile files.
  - Update `catalog/specs-index.template.yaml` (or a concrete index file, once introduced) to reference the new spec.
- When adding a new profile:
  - Place it under the owning spec directory (e.g. `specs/.../<spec>/profiles/`).
  - Update the profiles index in `catalog/`.
- When adding a new bundle:
  - Start from `bundles/bundle.template.yaml`.
  - Keep includes consistent with `specs/` and profiles indices.
  - Update the bundles index in `catalog/`.

## Tools and Workflows

- Before finalizing changes that touch specs or bundles, prefer to run:
  - `./tools/validate-specs.sh`
  - `./tools/validate-bundles.sh`
- Local Git hooks (`githooks/`) can be enabled via
  `git config core.hooksPath githooks` in your clone:
  - `commit-msg` runs `gitlint` using `.gitlint` to enforce Conventional
    Commits-style messages.
  - `pre-commit` enforces basic file-size guards, runs spec/bundle validation
    scripts, and (optionally) runs `gitleaks` if installed.
- `tools/lint-specs.py` is currently a placeholder; extending it is welcome **only** to enforce spec style and structure (not to introduce implementation logic).
- If you introduce new helper scripts:
  - Keep them in `tools/`.
  - Keep dependencies minimal and portable (shell, Python standard library).
  - Document their usage in `README.md` or `docs/` if they are part of the normal workflow.

## Style and Naming Conventions

- Spec IDs must follow `schemas/spec.schema.yaml` (e.g. `sdd.<domain>.<area>.<name>`).
- Keep terminology consistent across files (refer to `docs/style-guide.md`).
- Prefer short, declarative sentences in `spec.md`.
- Use YAML keys and field names that align with existing templates and schemas.

## Clarification Gate and Open Questions

- Clarify ambiguity **before** making non-trivial changes to a spec unit.
- Each spec unit should have its own `open-questions.md` (seeded from
  `specs/_template-spec-unit/open-questions.md`):
  - Only **open** questions are allowed in that file.
  - When a question is resolved, update the spec’s normative artefacts
    (`spec.yaml`, supporting bundles, and/or normative sections in `spec.md`)
    and then delete the row from `open-questions.md`.
  - Do **not** treat `open-questions.md` as an archive; it is a scratchpad for
    live ambiguity only.
  - Question IDs (for example `Q-001`) are local to that spec unit and chat
    transcripts; do not reference them from catalogs or other global docs.
- When uncertainty remains after reading the spec and docs, add or update
  entries in the relevant `open-questions.md` and pause for clarification
  instead of guessing semantics.

## LLM Interaction Protocol

- For any non-trivial change to specs, bundles, profiles, schemas, or docs in
  this repo, the agent MUST follow a **two-phase interaction**:
  - **Phase 1 – Clarifications (questions only).**
    1. Restate the task briefly to confirm understanding.
    2. Ask numbered clarification questions (1., 2., 3.) and wait for the
       human’s answers; do not propose options, solutions, or implementation
       plans in this message, **except when reasonable options with pros/cons
       and a clear recommendation can already be presented.**
    3. For design/architecture topics, record at least one `Q-xxx` entry in the
       relevant spec unit’s `open-questions.md` before asking those questions;
       when that question is resolved and its outcome is captured in the spec’s
       normative artefacts (`spec.yaml`, supporting bundles, and/or normative
       sections in `spec.md`), remove the corresponding row from
       `open-questions.md` as part of the same slice of work.
  - **Phase 2 – Options & decision.**
    4. After the human has answered the clarification questions (when any are
       needed), present 2–4 options labelled A, B, C, … with short pros/cons,
       and explicitly ask the human to choose or refine.
    5. Only after the human confirms a choice may the agent draft or modify
       specs, profiles, bundles, schemas, or docs, and it MUST mention the
       relevant `Q-xxx` ID in its chat summary for that change (do not embed
       `Q-xxx` IDs in normative specs/docs; see the Clarification Gate above).

### Owner preference – options-first for design

- For medium/high-impact design/spec questions (spec structure, bundle
  composition, profile definitions, schema changes, cross-cutting conventions,
  etc.), the default preference for this repository’s maintainer is:
  - The agent SHOULD present 2–4 concrete options with pros/cons and a clear
    recommendation for each decision point, instead of sending a
    “questions-only” message when reasonable options are already apparent.
  - The agent MAY still ask short clarifying questions, but should avoid a
    separate “Phase 1 – questions only” message unless a blocking ambiguity
    makes options meaningless.
  - This options-first behaviour is a standing explicit override for design
    work in this repo and does not need to be restated by the human in each
    session.
- **Low-impact/self-serve changes.** Trivial, obviously mechanical edits
  (typos, purely local renames, formatting-only fixes) may be performed
  directly after restating the task, without a full two-phase exchange, unless
  the human explicitly asks to follow the two-phase protocol.
- **Explicit overrides.** If the human explicitly says to skip clarifications
  or options (for example, “skip questions, just propose options now” or “just
  implement X as described”), the agent may follow that instruction but should
  briefly acknowledge that it is deviating from the default two-phase protocol
  for this interaction.
- Large artifacts (specs, long docs) MUST be written to the filesystem and only
  summarised in chat, unless the human explicitly asks to see the full text.

## Spec Analysis Gate

- For substantial spec or bundle changes, consult
  `docs/spec-analysis-gate.md` and ensure the **Analysis Gate** checklist is
  satisfied (or explicitly deferred by a maintainer) before finalising the
  change.
- Focus of this gate:
  - Spec completeness in `spec.yaml` / `spec.md`.
  - Alignment between narrative text, normative bundles, and catalog entries.
  - No unresolved blocking open questions for the change in scope.

## Agent Persistence and Token Budget

- Assume a very large token and context budget for this project – think **billions of tokens available** and a **huge amount of context window left** for any given session. Do not prematurely truncate work, over-summarise, or stop early because you are worried about “running out of tokens”; within platform limits, prefer complete, fully verified solutions over minimal answers.
- Reuse prior context aggressively: read existing specs, bundles, and docs from this repo (and earlier messages in the session) instead of asking the human to restate information you can recover.
- Be **brave and persistent** for any scoped task: move through exploration → design → concrete edits → verification for the agreed scope, rather than stopping at analysis or commentary.
- Long-running, self-directed work is encouraged as long as you respect this repo’s guardrails (spec-only, implementation-neutral, SDD principles, and the Spec Analysis / Clarification Gates).
- When you must stop early due to platform limits or missing information, state clearly what blocked you and what you would do next.

## Session Handover / Handoff

- When the human says “session handover” (or “handoff”), treat it as a request to prepare a high-signal summary for the next assistant or future session.
- Use the template in `ReadMe.LLM` section “Session Handover / Handoff Template”: fill in as many bracketed fields as you can from repo context (specs, bundles, catalogs, open-questions files, recent changes, and git state).
- The response SHOULD be copy/paste‑ready for the next assistant and SHOULD highlight environment, current status, recent increments, pending scope, git state, and concrete next steps in this repo.

## Exhaustive Execution for Scoped Tasks

- When the human describes a phase or task with an explicit scope (for example “this spec unit”, “all profiles under this spec”, “all bundles that reference this spec”), treat that scope as **exhaustive by default**, not best-effort.
- Do **not** silently narrow scope (for example, only updating “key” examples or a subset of bundles) unless the human has explicitly approved a reduced scope in this session.
- Before declaring a scoped task “complete”, you must:
  - Define concrete acceptance conditions in your own reasoning (for example: “no placeholder IDs left in this spec unit”, “all normative bundles that reference this spec are updated and validate cleanly”).
  - Use repo- or subtree-wide search commands (for example `rg`) to confirm there are **zero** remaining occurrences of the old pattern within the declared scope.
  - Run relevant quality gates for the artifacts you changed:
    - `./tools/validate-specs.sh` for spec changes.
    - `./tools/validate-bundles.sh` for bundle/profile changes.
    - Treat validation errors as blockers to be fixed or explicitly deferred.
- Balance exhaustiveness with this repo’s preference for **small, local changes**:
  - Default to scopes that are naturally local (a single spec unit, its profiles, its bundles, or a clearly bounded catalog section).
  - For very broad scopes (for example “all specs in the repo”), propose subdividing into smaller phases instead of silently ignoring parts of the requested scope.
- If you cannot finish the full agreed scope (platform limits, time, or missing information):
  - Say explicitly that the task is **partial**.
  - List which files, patterns, or subscopes remain.
  - Do not describe the phase as “done” while any known items in scope are still outstanding.

## No Silent Scope Narrowing

- When the human asks to “execute Phase N”, “update all profiles under this spec”, or similar, assume they mean **all artifacts covered by that phase** unless they explicitly say otherwise.
- If a strictly exhaustive pass over the requested scope would be unusually large or risky, pause and:
  - Surface the estimated size/complexity.
  - Ask whether to:
    - A) still do the exhaustive pass; or
    - B) explicitly limit the scope (for example to a subset of specs, profiles, bundles, or catalog entries).
  - Once agreed, record the narrowed scope in your own reasoning and respect it; do not narrow further without another explicit agreement.
- Never claim that a phase or scope is complete while you know of remaining artifacts within that agreed scope that still use the previous contract, even if they are low-importance or currently lint-clean.

## No-Laziness Expectations for Agents

- Always read the relevant spec unit (`spec.yaml`, `spec.md`, examples, and
  bundles) and key docs (`docs/specs-constitution.md`, `docs/repo-vision.md`,
  `docs/sdd-principles.md`, `docs/style-guide.md`, `docs/authoring-guidelines.md`)
  before proposing structural changes.
- Prefer concrete edits (spec fields, examples, catalog entries) over vague
  commentary.
- Keep specs and catalogs in sync; when adding or moving specs, update the
  appropriate entries under `catalog/`.
- Do not introduce implementation details, build commands, or environment-
  specific configuration into this repository; those belong in downstream
  implementation repos.

## How to Use This Agent Guide

- When asked to “create a new spec”:
  - Work from the template in `specs/_template-spec-unit/`.
  - Ensure new files respect schemas in `schemas/` and indices in `catalog/`.
- When asked to “improve” or “refactor”:
  - Focus on clarity, consistency, and schema alignment.
  - Avoid speculative fields or concepts that are not grounded in existing docs or schemas unless explicitly requested.
- When unsure:
  - Prefer adding TODO comments in Markdown (`> TODO:` style) over inventing semantics.
  - Defer implementation details to downstream repositories; keep this one specification-focused.
