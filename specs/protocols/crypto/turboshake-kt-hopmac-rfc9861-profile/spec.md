# TurboSHAKE / KangarooTwelve / HopMAC RFC 9861 Profile

> Spec ID: `sdd.crypto.xof.turboshake-kt-hopmac-rfc9861-profile`  
> Kind: `library-api`  
> Domain: `crypto`

This spec unit captures the RFC 9861–aligned profile for TurboSHAKE, the
KangarooTwelve family (KT128/KT256), and HopMAC, intended primarily for
AI/LLM and code-generation agents that emit cryptographic library
implementations.

The canonical behavioral core of this profile lives in the ProfileSchema
bundle ([profile-core.yaml](profile-core.yaml)) and the conformance bundle ([conformance.yaml](conformance.yaml)).
This Markdown file is an implementation-neutral overview and navigation aid
for those bundles; it does not introduce additional behavioral requirements.

## Normative Sources

The normative sources for this spec unit are:

- The ProfileSchema bundle in [profile-core.yaml](profile-core.yaml) (ProfileBundle and related
  sections such as `AgentCoreView`, `SpecIndex`, `Constraints`, API Contracts,
  algorithms, Error Model, and ExternalSpecs/TestVectors).
- The conformance and test-vector bundle in [conformance.yaml](conformance.yaml).
- RFC 9861 “KangarooTwelve and TurboSHAKE” and FIPS 202 for the underlying
  primitives.

Any disagreement between narrative text in Markdown files and the ProfileSchema
bundle in [profile-core.yaml](profile-core.yaml) MUST be resolved in favor of the bundle.

## Files in This Spec Unit

This directory contains:

- [spec.yaml](spec.yaml) – SDD-style metadata for this spec unit, including its ID,
  lifecycle, and pointers to the normative ProfileSchema and conformance
  bundles.
- [spec.md](spec.md) – this overview and navigation document.
- [profile-spec.md](profile-spec.md) – the detailed profiled specification for
  TurboSHAKE/KT/HopMAC, written for agents and tools and anchored in RFC 9861
  and FIPS 202.
- [profile-core.yaml](profile-core.yaml) – the canonical ProfileSchema bundle describing
  primitives, constraints, algorithms, error model, and external references.
- [conformance.yaml](conformance.yaml) – the conformance and test-vector bundle aligned with
  the ProfileSchema.
- `docs/` – design notes and open questions used during the design of this
  profile.
- [critique.md](critique.md), [feedback.md](feedback.md) – commentary and review notes.

For full behavioral detail, agents should consume [profile-core.yaml](profile-core.yaml) and
[conformance.yaml](conformance.yaml) directly (or parse the YAML blocks embedded in [profile-spec.md](profile-spec.md))
and treat this Markdown file as informative.
