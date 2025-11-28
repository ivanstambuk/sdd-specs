# Visual Prompts (Non-Normative) – PLACEHOLDER_TITLE

This file is **non-normative**. It collects AI image prompts to generate
visuals (individual figures or slide-ready panels) that illustrate the spec.
Each prompt must be fully self-contained (no shared “global style primer”).
Behavioral and conformance requirements remain defined by `spec.yaml` and any
referenced normative bundles; this file is only for visualization guidance.

## Prompts

Each prompt entry should define a clear, self-contained request. Use multiple
entries for different aspects (e.g., algorithm overview, threat model, API
surface, performance trade-offs) or for different output shapes (e.g., slide
panel vs poster).

Recommended fields per prompt:

- `id`: e.g., V-001
- `title`: short label
- `intent`: figure | slide-panel | poster | thumbnail | cover
- `aspect_ratio`: 16:9 | 4:3 | A4 portrait | square, etc.
- `style`: inline style snippet (self-contained; do not rely on a global primer)
- `content_brief`: spec-specific content to depict
- `must_include`: bullets of required elements / labels
- `avoid`: bullets for exclusions (brands, decorative icons, etc.)
- `layout_guidance`: regions/flow if desired
- `legend_notes`: colors/line styles/notation guidance
- `bottom_line`: one-sentence takeaway for the generated image
- `status`: draft | approved | superseded
- `version`: prompt version

### Example Prompt – Algorithm Overview

id: V-001  
title: RFC 9861 – Family Overview  
intent: figure  
aspect_ratio: 16:9  
style: |
  High-resolution, research-grade vector infographic. Clean, flat lines; restrained palette (desaturated blues/teals/greys; single orange accent). Geometric sans-serif hierarchy (title > region headings > node labels > fine annotations). Thin sharp strokes; no decorative icons or logos.
content_brief: TurboSHAKE128/256, KT128/256, Keccak-p[1600,12], tree hashing, domain bytes 0x06/0x07/0x0B, XOF outputs.  
must_include:
- Four XOFs branching from Keccak-p[1600,12].
- TurboSHAKE sponge flow (absorb/squeeze).
- KangarooTwelve tree layout (FinalNode, IntermediateNode, SingleNode).
- Domain-separation values table (0x06, 0x07, 0x0B).
layout_guidance: Left→right regions (A) Family, (B) Sponge, (C) Tree, (D) Properties.  
legend_notes: solid vs dashed arrows; color per family (TurboSHAKE vs KT).  
bottom_line: “Keccak-based XOF family that halves rounds, adds tree hashing, and keeps strong security.”  
status: draft  
version: v1

### Example Prompt – Slide Deck (Multi-Panel)

id: V-002  
title: Slide Deck Panels – TurboSHAKE/KT Profile  
intent: slide-panel (set of 4 panels for PPT/Keynote)  
aspect_ratio: 16:9  
style: |
  Cohesive slide-panel set in a research style: clean vector lines, restrained blues/greys with one orange accent, consistent typography hierarchy across panels. Minimal clutter; clear axes/labels where used.
content_brief: Create four coordinated panels for a slide deck: (1) Family map; (2) TurboSHAKE sponge micro-view; (3) KT tree hashing; (4) Security/throughput snapshot.  
must_include:
- Panel 1: family map with rates/capacities and 12-round Keccak-p core.
- Panel 2: numbered absorb/squeeze steps with r/c shown.
- Panel 3: chunking, CV leaves, FinalNode assembly, domain bytes.
- Panel 4: mini comparison grid vs SHA-2/SHAKE and a relative throughput axis.
layout_guidance: Four side-by-side or 2×2 grid panels with consistent palette and typography.  
legend_notes: shared legend for arrows/colors across panels.  
bottom_line: “Unified visual set for presenting the TurboSHAKE/KT profile in talks.”  
status: draft  
version: v1
