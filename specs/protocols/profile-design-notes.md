# TurboSHAKE / KangarooTwelve / HopMAC Profile – Design Notes (Non-Normative)

This document collects editorial philosophy, agent-focused rationale, and design history for the profiled TurboSHAKE / KangarooTwelve / HopMAC specification aligned with RFC 9861. It is **non-normative**: all enforceable behavior is defined by the ProfileSchema bundle in `profile-core.yaml`, the Error Model, and the Test Vectors & Conformance bundles in `conformance.yaml` and RFC 9861.

The goal is to keep `rfc.md` focused on the behavioral core (types, Constraints, API Contracts, algorithms, Error Model, FR/NFR indices, and test/conformance criteria) while preserving the thinking behind those choices here for humans and agents that need additional context.

## 1. LLM Implementation Contract – Rationale

The **LLM Implementation Contract** section in `rfc.md` specifies how an AI/LLM agent should *use* the ProfileSchema to generate implementations. Its key points:

- **Behavioral source of truth.** Agents must treat the ProfileSchema YAML (Constraints + API Contracts + Algorithms + Error Model/Context*) as the only source of observable behavior. FR/NFR tables and narrative prose are obligation indices and explanations, not behavioral sources.
- **Parameter bounds and validation.** All bounds on `M`, `C`, `D`, `L`, keys, and streaming lengths are taken from `Constraints` and `constraints_ref` fields. If FR/NFR or commentary seems to disagree, Constraints win.
- **Control flow and state machines.** Allowed phases and state transitions come from the API/Algorithm YAML for TurboSHAKEContext, KT128/256, HopMAC128/256, and Error Model/Context* blocks. Narrative text must conform to those structures.
- **Algorithm fidelity.** TurboSHAKE, KT128/256, and HopMAC128/256 algorithms must be implemented exactly as specified in the Algorithm YAML. RFC 9861 and FIPS 202 are normative for KP and the published test vectors; this profile narrows RFC 9861 where it leaves latitude, but does not deliberately change those core constructions.
- **No cryptographic design delegation.** The profile is written so that all security-relevant degrees of freedom (bounds, domains, tree layout, HopMAC policy) are fixed. Agents must not ask external users to choose alternative cryptographic parameters for an implementation that claims conformance to this profile.

These rules are expressed in `rfc.md` for direct agent consumption; this design note exists so maintainers can see the intent without adding more prose to Part I.

## 2. Document Economy and Agent-Normativity – Rationale

Earlier versions of the profile contained long sections titled **“Document Economy”** and **“Agent-Normativity Rationale”** in Part I. Their purposes were:

- To explain why the profile is written “AI-first” and optimized for mechanical consumption rather than human narrative.
- To discourage adding prose that does not change, constrain, or clarify behavior in ways that matter for implementations or conformance.
- To make the “normative for agents” nature explicit: some BCP 14 language is applied to agent workflows (reading order, editing constraints) as a design choice for this project’s maintenance model.

In the current structure:

- The normative effect of these ideas is already captured by:
  - The definition of the canonical behavioral core (Constraints + API + Algorithms + Error Model/Context*),
  - The derived role of FR/NFR, SpecIndex, AgentCoreView, and ImplementationChecklist,
  - The ProfileSchema invariants.
- Part I now carries only the **minimum** necessary workflow guidance for agents (see “How an Agent Uses This Specification”) and points here for further rationale.

As a result, the long-form philosophy has been moved here so that:

- Part I remains tight and primarily about behavior and indices.
- Agents that need more context can still read these notes, but must not derive new requirements from them.

## 3. Out-of-Scope Topics (Fixed Profile Parameters)

Several design choices are intentionally fixed for this profile and are treated as **out of scope** for edits within `rfc.md`:

- **Primitive set and round counts.** The profile assumes Keccak-p[1600,12] as in RFC 9861 / FIPS 202 and defines KP, TurboSHAKE128/256, TurboSHAKEContext, KT128/256, and HopMAC128/256 on top of it. Alternative primitives or round counts require a separate profile or major revision, not edits to this one.
- **64-bit length model (minimum guarantee).** All profile-mandated conceptual lengths/counters are guaranteed to be supported for values `0 ≤ n ≤ 2^64 − 1` via `TypesAndNotation.Integers.length_counters` and the `Constraints` schema. RFC 9861’s broader conceptual domains (for example, `0 ≤ x < 256^255` for `length_encode(x)`) are reflected in `max_expr` fields, but this profile’s normative ranges stop at `2^64 − 1`. Implementations MAY choose to handle conceptual messages or outputs beyond `2^64 − 1` bytes in a manner consistent with those RFC bounds, yet such behavior is outside this profile’s conformance guarantees and, if it needs to be standardized, should be captured by a separate profile.
- **HopMAC tag-length minima.** Minimum tag lengths in `Constraints.HopMAC.L_HopMAC128` and `.L_HopMAC256` encode this profile’s security targets. Shorter tags define different MAC variants and must not be described as HopMAC128/256 conformant to this profile.
- **Agent-only editing model.** The requirement that normative edits flow through agents, and that the spec remains AI-first, are part of the project’s governance. Changing that model is a governance decision, not a profile edit.

These constraints are restated here for clarity, but their enforceable form lives in the ProfileSchema and Error Model in `profile-core.yaml`.

## 4. Profile Bindings PB1–PB8 – Rationale

PB1–PB8 in `rfc.md` summarize where RFC 9861 leaves latitude and how this profile fixes it. The normative behavior for each binding is already encoded in:

- `Constraints` entries (e.g., for D, L, message/customization lengths, HopMAC keys/tags),
- API Contracts and Algorithm YAML for TurboSHAKEContext, KT128/256, HopMAC128/256,
- FR/NFR table entries,
- The Error Model.

This design note serves only to preserve **why** those choices were made (e.g., explicit streaming state machine for portability, 64-bit length model for practicality, HopMAC tag policy for security targets). Implementations and conformance tools must look to the ProfileSchema bundle and conformance bundles, not to this document, for enforceable behavior.

## 5. Maintenance Guidance for Spec Authors

When modifying the profile:

- Change the **ProfileSchema bundle** first (`profile-core.yaml`), keeping IDs stable where possible.
- Regenerate or update:
  - Embedded YAML blocks in `rfc.md`,
  - FR/NFR Normative reference(s) columns,
  - AgentCoreView and SpecIndex,
  - Conformance/test bundles in `conformance.yaml`.
- Update this design note only if the underlying design rationale changes; do not add narrative to `rfc.md` that is not necessary for behavior, indices, or conformance definitions.

This keeps the spec aligned with the critique: Part I stays lean and behavioral, while deeper narrative lives in clearly non-normative design notes.
