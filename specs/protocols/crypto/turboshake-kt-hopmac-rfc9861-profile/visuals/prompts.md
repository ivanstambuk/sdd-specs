# Visual Prompts (Non-Normative) – TurboSHAKE / KangarooTwelve / HopMAC (RFC 9861)

This file is **non-normative**. It captures self-contained AI image prompts for
illustrating the RFC 9861 TurboSHAKE / KangarooTwelve / HopMAC profile. All
behavioral and conformance requirements remain defined by `spec.yaml`,
`profile-core.yaml`, `profile-spec.md`, and `conformance.yaml`.

## Prompt V-001 – RFC 9861 Family Overview (16:9)

id: V-001  
title: RFC 9861 – TurboSHAKE / KangarooTwelve Family  
intent: figure  
aspect_ratio: 16:9  
style: |
  GLOBAL STYLE PRIMER — HYPER-TECHNICAL RESEARCH DIAGRAMS
  
  Create a high-resolution 16:9 infographic suitable for deep technical and research presentations:
  - systems research
  - algorithms and asymptotic analyses
  - formal models and protocols
  - ML/AI pipelines and ablation studies
  - cryptography, security, and distributed systems
  - experimental setups and empirical results
  
  Overall look:
  - Very clean, flat, vector-illustration style with research-grade precision.
  - Palette: restrained, professional — desaturated blues, teals, purples, greys; at most 2 accent colors (orange/magenta) to distinguish key elements or classes.
  - Typography: highly legible geometric or humanist sans-serif with clear hierarchy:
    • Primary title (largest)
    • Region/section headings
    • Node labels
    • Fine-print annotations
  - Prefer thin but sharp lines; avoid fuzzy or “cute” visuals.
  - No brand logos or decorative icons; use abstract, domain-neutral symbols.
  
  Visual grammar / metaphors (technical):
  - Processes / algorithms:
    • Stepwise pipelines with numbered stages (1, 2, 3, …).
    • Control-flow graphs with branches, loops, and merge points.
    • State machines with explicit states and labeled transitions.
  - Data and signals:
    • Vectors/tensors as stacked bars or small matrices.
    • Probability distributions as curves, density blobs, or histograms.
    • Time-series as line plots with axes, ticks, and legends.
  - Modules, layers, and components:
    • Blocks, layers, or stacked rectangles with explicit interfaces.
    • “Engines” or solvers as highlighted cores with inputs/outputs.
    • Optional annotation of complexity, e.g., O(n²), O(n log n).
  - Interfaces and APIs:
    • Ports, adapters, or boundary boxes labeled “API”, “RPC”, “IPC” etc.
    • Explicit arrows crossing boundaries to indicate coupling.
  - Trade-offs and frontiers:
    • 2D planes with axes (e.g., “accuracy vs compute”, “latency vs consistency”).
    • Pareto-front curves highlighting optimal regions vs dominated regions.
  - Uncertainty / error:
    • Confidence intervals as shaded bands.
    • Error bars on data points.
    • Regions labeled as “feasible”, “unsafe”, “unproven”.
  
  Image structure rules:
  - Partition the canvas into 4 labeled regions with explicit headings:
    • “(A) Family Overview”
    • “(B) TurboSHAKE Sponge Flow”
    • “(C) KangarooTwelve Tree Hashing”
    • “(D) Security & Performance Properties”
  - Each region should contain one core construct with 3–8 labeled elements.
  - Directional story: left→right A→B→C→D; top→bottom for abstraction if helpful.
  - Maintain whitespace; include a compact legend when multiple colors/line styles are used.
  
  Axes, notation, and labels:
  - When showing plots/planes, label both axes with quantities/units; include ticks and a legend for multiple series.
  - Use research notation where useful: E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
  - Label inputs, outputs, parameters; distinguish deterministic vs stochastic (solid vs dashed).
  
  Reading orientation & storytelling:
  - Number key steps if depicting an algorithm.
  - Use (A),(B),(C),(D) tags and refer to them in labels.
  - Group related elements with subtle background shapes; avoid decorative elements that don’t support the story.
  
content_brief: |
  Draw a single, dense research-grade figure for “RFC 9861: KangarooTwelve and TurboSHAKE” with four regions:
  - (A) Family Overview: Keccak-p[1600, n_r = 12] core; reference to FIPS 202 (24 rounds). Four XOFs: TurboSHAKE128/256, KT128/256. Show rates/capacities: TurboSHAKE128 r=168B c=32B; TurboSHAKE256 r=136B c=64B; note r+c=1600 bits. KT128/256 built on TurboSHAKE (arrows “TurboSHAKE128 → KT128”, “TurboSHAKE256 → KT256”), with notes: tree hashing, customization string C, parallelizable.
  - (B) TurboSHAKE Sponge Flow: numbered absorb/squeeze pipeline for TurboSHAKE(M,D,L). Inputs M, D (0x01–0x7F, default 0x1F), L. Pad M||D to multiples of r; XOR 0x80 in last byte; split into blocks; absorb (XOR block into first r bytes, then Keccak-p[1600,12]); loop over blocks; squeeze r-byte chunks, reapply permutation until L bytes produced.
  - (C) KangarooTwelve Tree Hashing: show S = M || C || length_encode(|C|). Short case (|S|≤8192): S → TurboSHAKE with domain 0x07 (SingleNode). Long case: split S into 8192-byte chunks S0…Sn-1; leaves CV_i = TurboSHAKEX(S_i, 0x0B, t) (t=32 for KT128, 64 for KT256); FinalNode = S0 || constant 0x03||00…00 || CVs || length_encode(n−1) || 0xFF||0xFF; Final output: TurboSHAKEX(FinalNode, 0x06, L) (0x06 = FinalNode). Include a small table of domain bytes: SingleNode 0x07, Intermediate 0x0B, FinalNode 0x06.
  - (D) Security & Performance: compact comparison grid vs SHA-2 and SHAKE; note “XOF outputs”, “128-bit and 256-bit variants”, “Keccak-p[1600, 12 rounds] vs 24 for SHAKE”, “Tree hashing parallelism (KT)”, “Customization via C and D”. Add a small relative throughput axis positioning SHA-2, SHAKE, TurboSHAKE, KT (tree) qualitatively.
must_include:
  - Four XOFs branching from Keccak-p[1600,12] with rates/capacities annotated.
  - TurboSHAKE absorb/squeeze pipeline with r and c labeled.
  - KangarooTwelve tree: chunking, CV leaves (0x0B), FinalNode assembly, Final TurboSHAKE with 0x06, SingleNode with 0x07.
  - Domain-separation table for 0x06 / 0x07 / 0x0B.
  - Security/performance comparison highlights vs SHA-2/SHAKE.
layout_guidance: |
  Left→right regions: (A) Family Overview; (B) TurboSHAKE Sponge Flow; (C) KangarooTwelve Tree Hashing; (D) Security & Performance. Keep 3–8 labeled elements per region; include a small legend for arrow styles/colors.
legend_notes: |
  Solid arrows = deterministic main data path; dashed arrows = optional/incremental API details; color-coding to distinguish TurboSHAKE vs KT vs external references.
bottom_line: "RFC 9861 defines four Keccak-based XOFs that reduce rounds, add tree hashing, and use domain separation to deliver fast, parallelizable, extendable hashing with strong security guarantees."  
status: draft  
version: v1

## Prompt V-002 – Slide 1: RFC 9861 in One Picture — XOF Family & Lineage

intent: slide  
aspect_ratio: 16:9  
style: |
  Global, research-grade infographic style: clean, flat, vector lines; restrained palette (desaturated blues/teals/greys with one accent color); geometric sans-serif hierarchy; thin sharp strokes; no logos; abstract, domain-neutral symbols. Use 2–4 regions with clear headings and numbered flow where needed.
content_brief: |
  Single-panel family tree showing lineage from Keccak-p[1600] to SHA-3/SHAKE (24 rounds), SP 800-185 (KMAC/TupleHash/ParallelHash), and RFC 9861 (TurboSHAKE128/256, KT128/256, HopMAC). Center the Keccak permutation; branch to SHA-3/SHAKE and SP 800-185; branch to RFC 9861 round-reduced Keccak-p[1600,12] with four XOFs. Include rates/capacities for TurboSHAKE128 (r=168B, c=32B) and TurboSHAKE256 (r=136B, c=64B); arrows TurboSHAKE128→KT128 and TurboSHAKE256→KT256 with notes (tree hashing, customization C, parallelizable). Small box for XOF property (arbitrary-length output). Annotations for standards/registries: FIPS 202, NIST SP 800-185, RFC 9861; registry notes for IANA/COSE.
must_include:
  - Central Keccak-p[1600] block with 24- vs 12-round tags.
  - Four RFC 9861 XOFs branching, with rates/capacities.
  - KT128/KT256 as tree XOFs on TurboSHAKE128/256.
  - HopMAC box above, built on these XOFs.
  - Standards/registries callouts (FIPS 202, SP 800-185, RFC 9861, IANA/COSE).
layout_guidance: Single-panel family/dependency graph; top/left for SHA-3/SHAKE/SP800-185; center for Keccak; right/bottom for RFC 9861 branch; concise legend for colors/lines.  
legend_notes: Color layers for base permutation, hash/XOF primitives, higher-level constructions; small legend in a corner.  
bottom_line: "RFC 9861 extends the Keccak family with round-reduced, domain-separated XOFs and tree hashing, connecting cleanly to existing standards and registries."  
status: used  
version: v1

## Prompt V-003 – Slide 2: Why New XOFs Beyond SHA-3? — Trade-off Landscape

intent: slide  
aspect_ratio: 16:9  
style: |
  Research-style comparative graphic; same palette and typography as V-002. Clear axes, concise labels, small grid/table elements; thin lines; minimal clutter.
content_brief: |
  Comparative trade-off slide with three regions: (A) performance vs structural richness plane placing SHA-2, SHA-3/SHAKE, TurboSHAKE, K12; (B) property matrix (≤6 rows) comparing output type, rounds, parallelism/tree mode, domain separation/customization, typical usage; (C) evolution arrow SHA-2→SHA-3/SHAKE→TurboSHAKE→K12 with short motive phrases. Emphasize flexibility (XOF, tree), parallelism, domain separation, and performance gains from 12-round Keccak-p.
must_include:
  - 2D trade-off plot with points for SHA-2, SHA-3, SHAKE, TurboSHAKE, K12.
  - Compact property matrix with four columns (SHA-2, SHA-3/SHAKE, TurboSHAKE, K12).
  - Evolution arrow with nodes and motives.
layout_guidance: Left (A) trade-off plane; middle (B) matrix; right (C) timeline arrow. Consistent color coding from V-002.  
legend_notes: Small legend for color families; axes labeled; minimal ticks.  
bottom_line: "TurboSHAKE and K12 target the high-performance, high-flexibility corner beyond SHA-3/SHAKE while retaining Keccak-based assurances."  
status: used  
version: v1

## Prompt V-004 – Slide 3: Sponge Refresher & XOF Concept

intent: slide  
aspect_ratio: 16:9  
style: |
  Clean, technical; highlight rate vs capacity; thin strokes; restrained palette with an accent for XOF elements.
content_brief: |
  Three regions: (A) Sponge conceptual model showing 1600-bit state split into rate r and capacity c (r+c=1600), with Keccak-p box above; (B) Absorb/Squeeze pipeline (5 steps) from padded blocks to iterative squeezing until L bytes; (C) Fixed-length hash vs XOF comparison with prefix property. Annotate round counts (24 vs 12) briefly; emphasize prefix property and arbitrary-length output.
must_include:
  - 1600-bit state bar split into r and c with labels.
  - Absorb/squeeze loop with permutation calls.
  - Two-panel comparison: fixed-length hash vs XOF(M,L) with prefix note.
layout_guidance: Left (A) state diagram; center (B) pipeline; right (C) comparison mini-panels.  
legend_notes: Colors for rate vs capacity; solid arrows for absorb/squeeze.  
bottom_line: "Keccak sponges split state into rate and capacity, letting TurboSHAKE/K12 absorb blocks and squeeze arbitrary-length XOF outputs with prefix-consistent results."  
status: used  
version: v1

## Prompt V-005 – Slide 4: TurboSHAKE Interface & Parameter Space

intent: slide  
aspect_ratio: 16:9  
style: |
  Technical interface view; same deck palette; crisp tables and flow lines.
content_brief: |
  Three regions: (A) Interface TurboSHAKE(M,D,L) with inputs/outputs and default D=0x1F; XOF/prefix notes. (B) Parameter table comparing TurboSHAKE128 vs TurboSHAKE256 (r, c, security) plus shared state bar (r+c=1600). (C) Domain separation via D: multiple TurboSHAKE boxes with different D values over same M producing independent outputs; constraints D∈0x01–0x7F.
must_include:
  - Function box TurboSHAKE(M,D,L) and schematic I/O.
  - Table/cards for TS128 (r=168,c=32) and TS256 (r=136,c=64) with security notes.
  - Parallel D-variant illustration (D=0x1F default, D=0x01, D=0x02).
layout_guidance: Left interface; center table/state; right domain-separation panel.  
legend_notes: Color for parameters vs state; accent for D/domain separation.  
bottom_line: "TurboSHAKE exposes a simple three-parameter XOF; rate/capacity set throughput and security, while D cleanly separates domains over the same message space."  
status: used  
version: v1

## Prompt V-006 – Slide 5: TurboSHAKE Internals — Sponge Pipeline

intent: slide  
aspect_ratio: 16:9  
style: |
  Detailed algorithmic flow; keep visuals consistent with prior slides; highlight 12-round permutation boxes.
content_brief: |
  Two regions: (A) Input formation and padding: M, D (default 0x1F), L; M′=M||D; pad to rate r; XOR 0x80; r-byte blocks B_i (r=168 or 136). (B) Absorb/permute/squeeze pipeline: zeroed state split r/c; absorb loop XOR B_i into rate then Keccak-p[1600,12]; start squeeze Z0 from rate; repeat permutation + r-byte outputs until ≥L, truncate to L. Optional micro-comparison to SHAKE (24 vs 12 rounds).
must_include:
  - Inputs (M,D,L), padding to r, block split.
  - Absorb loop with 12-round permutation.
  - Squeeze loop producing Z_i until L bytes.
layout_guidance: Left padding/blocks; center/right pipeline with numbered steps.  
legend_notes: Colors for state segments, blocks, permutation boxes.  
bottom_line: "TurboSHAKE pads M∥D into r-byte blocks, XORs into the rate with 12-round Keccak permutations, then squeezes r-byte chunks until L bytes are produced."  
status: used  
version: v1

## Prompt V-007 – Slide 6: KangarooTwelve Interface & Message Encoding

intent: slide  
aspect_ratio: 16:9  
style: |
  Interface + encoding focus; consistent palette; clear segment labels.
content_brief: |
  Three regions: (A) Interface KT(M,C,L) with KT128/KT256 note; parameters M,C,L, output Z. (B) Internal string S = M ∥ C ∥ length_encode(|C|) with three-segment bar and injectivity notes. (C) length_encode(|C|) inset: k=|C| → length_encode(k) → bytes; notes on unambiguous boundary and collision avoidance; small examples contrasting different M,C.
must_include:
  - KT function box and I/O schematic.
  - S bar split into M, C, length_encode(|C|).
  - length_encode detail inset and bullet notes on domain separation.
layout_guidance: Left interface; center encoding pipeline; right length_encode detail.  
legend_notes: Color code for M, C, length_encode segments.  
bottom_line: "KT128/256 present KT(M,C,L) while internally hashing S = M ∥ C ∥ length_encode(|C|), ensuring clear customization-aware separation."  
status: used  
version: v1

## Prompt V-008 – Slide 7: KangarooTwelve Modes — Single Node vs Tree Hashing

intent: slide  
aspect_ratio: 16:9  
style: |
  Mode contrast; tree framing; concise domain-byte legend.
content_brief: |
  Two bands: (A) Short messages |S|≤8192: single TurboSHAKEX(S, D=0x07, L) → KT128/256 outputs. (B) Long messages |S|>8192: chunk S into 8192-byte S0..Sn-1; leaves CV_i = TurboSHAKEX(S_i, D=0x0B, t=32/64); FinalNode inputs S0, constant 0x03||00…00, CVs, length_encode(n−1), 0xFF||0xFF → TurboSHAKEX(FinalNode, D=0x06, L). Region (C) legend for domain bytes: SingleNode 0x07, Intermediate 0x0B, FinalNode 0x06.
must_include:
  - Single-node pipeline for short case with D=0x07.
  - Tree case: chunking, leaf CVs with D=0x0B, FinalNode assembly, final call with D=0x06.
  - Domain-byte legend.
layout_guidance: Top short-mode band; bottom tree-mode band; right legend.  
legend_notes: Colors for chunks, TurboSHAKE calls, domain tags.  
bottom_line: "K12 uses a single-node TurboSHAKE for short inputs and a domain-separated tree of leaves and root for long inputs, enabling parallelism and clear framing."  
status: used  
version: v1

## Prompt V-009 – Slide 8: HopMAC & Generic MAC/KDF Constructions

intent: slide  
aspect_ratio: 16:9  
style: |
  Two-layer MAC visuals; side panels for generic patterns; consistent palette with accent for keys/SCA areas.
content_brief: |
  Three regions: (A) HopMAC conceptual (keyless inner K12 over M,C producing V; keyed outer MAC using K and V; note: only outer is SCA-sensitive). (B) HopMAC flow steps: inputs K,M,C; inner KT128/256 to V (L_v); outer keyed TurboSHAKE/KT to tag T; SCA boundary around outer call; notes on constant-time requirement. (C) Generic MAC/KDF patterns: MAC_A(K||M) via XOF; MAC_B using C=K; KDF via XOF(K||info, L_total) with derived keys slices; emphasize domain separation via D/C.
must_include:
  - Two-layer HopMAC schematic with keyless inner, keyed outer.
  - Flow with L_v, L_t, and SCA boundary.
  - MAC/KDF pattern mini-panels with domain-separation callouts.
layout_guidance: Left conceptual; center flow; right mini-panels.  
legend_notes: Colors for XOF engines, keys, digests/tags; SCA boundary styling.  
bottom_line: "HopMAC builds a MAC from K12 with a keyless inner and single keyed outer call, while RFC 9861 XOFs also support straightforward MAC/KDF patterns via domain separation."  
status: used  
version: v1

## Prompt V-010 – Slide 9: Security Levels, Output Length & Family Overview

intent: slide  
aspect_ratio: 16:9  
style: |
  Security/selection guide; grids and small chart; consistent palette with security accents.
content_brief: |
  Regions: (A) Family grid listing TurboSHAKE128/256, KT128/256 with underlying primitive, r, c, nominal security. (B) Output length vs security schematic: axis for L with bars for TS128 (≥32 bytes), TS256 (≥64 bytes), KT counterparts, and notes on XOF outputs vs capacity-bound security. (C) Role map 2×2 grid: flat XOF vs tree XOF, 128-bit vs 256-bit, with typical use bullets per node; arrows TS→KT. Notes on picking variants and that security bounded by capacity, not just L.
must_include:
  - Parameter grid (instances, r, c, security).
  - L vs security chart with recommended minima.
  - Role/usage map with four instances.
layout_guidance: Left grid; center L-vs-security schematic; right role map.  
legend_notes: Colors for 128 vs 256, TurboSHAKE vs KT.  
bottom_line: "TS128/256 and KT128/256 share Keccak-p[1600,12] with capacities that set ≈128/256-bit strength; choose L and flat vs tree mode to match performance and data size needs."  
status: used  
version: v1

## Prompt V-011 – Slide 10: Security Argument Stack & Misuse Resistance

intent: slide  
aspect_ratio: 16:9  
style: |
  Layered stack plus misuse panels; accent highlights for assumptions and warnings; consistent deck visuals.
content_brief: |
  Regions: (A) Vertical security stack: Keccak-p[1600,12] assumption; sponge/XOF (TurboSHAKE) with capacity-based bounds and D; tree hashing (K12) with Sakura framing and domains 0x0B/0x06/0x07; constructions on top (HopMAC/MAC/KDF); optional protocol instantiations. (B) Misuse scenarios: length-extension, missing domain separation, too-short L, partial-tree misuse, each with resistance notes. (C) Side-channel/implementation: low algebraic degree vs SHA-2; keyless vs keyed calls (SCA boundary); round-reduction vs margin bar (24 vs 12). Include bullets for constant-time guidance and domain separation best practices.
must_include:
  - Layered stack with 4–5 layers and short assumptions per layer.
  - Misuse scenario boxes with concise “resists / needs care” notes.
  - SCA panel with keyless vs keyed mini-diagrams and 24 vs 12 round comparison.
layout_guidance: Left stack; center misuse list; right SCA/implementation notes.  
legend_notes: Colors for assumption layers, warnings, SCA regions.  
bottom_line: "Security flows from Keccak-p[1600,12] up through sponge, tree, and MAC/KDF constructions; domain separation and SCA-aware keyed calls provide robustness against common misuse."  
status: used  
version: v1

## Prompt V-012 – Slide 11: Testing, Vectors & Registries (Interoperability View)

intent: slide  
aspect_ratio: 16:9  
style: |
  Testing/interop focus; tidy cards and axes; consistent palette with accent for tests/registries.
content_brief: |
  Regions: (A) Test-vector strategy coverage: |M| axis with short/threshold/long; customization cases; output-length axis; ptn(n) note; summary sentence. (B) Two schematic example vector cards: TurboSHAKE example with M=ptn(n1), D=0x1F, L1; KT example with |S|>8192, C non-empty, L2; outputs referenced to RFC hex. (C) Registries: IANA identifiers for TS/KT; COSE alg IDs mapping; small protocol ecosystem icons referencing registries; note on interoperability and bit-for-bit validation.
must_include:
  - Coverage axes for length/customization/output.
  - Two example vector cards (TurboSHAKE, K12) schematic (no hex dump).
  - Registry mapping boxes for IANA and COSE with alg names/IDs.
layout_guidance: Left coverage; center cards; right registries/protocols.  
legend_notes: Colors for tests vs algorithms vs registries.  
bottom_line: "RFC 9861 pairs structured test coverage with IANA/COSE registrations so TS/KT implementations can be validated bit-for-bit and plugged into standard protocol ecosystems."  
status: used  
version: v1

## Prompt V-013 – Slide 12: Design Trade-offs & Summary

intent: slide  
aspect_ratio: 16:9  
style: |
  Executive technical summary; quadrant + matrix + summary cards; consistent palette and typography.
content_brief: |
  Regions: (A) Trade-off quadrant (performance vs structural richness) placing SHA-2, SHA-3/SHAKE, TurboSHAKE, K12; shade target region upper-right. (B) Pros/cons matrix with rows: performance/functionality, protocol/domain separation, implementation/SCA; benefits vs costs. (C) Family summary cards: TurboSHAKE (use as default XOF; 128/256 choice), K12 (long-message/tree, parallel), HopMAC (MAC with keyless inner). Include decision line “Need fast XOF? → TS; hashing huge data? → K12; MAC? → HopMAC.”
must_include:
  - Quadrant with four family points.
  - Pros/cons two-column grid with concise bullets.
  - Three summary cards with use-when guidance.
layout_guidance: Left quadrant; center matrix; right summary strip.  
legend_notes: Colors for legacy vs FIPS202 vs RFC9861 nodes; clarify axes.  
bottom_line: "TurboSHAKE/K12/HopMAC trade some Keccak round margin for speed, tree parallelism, and structured MACs—choose TS, K12, or HopMAC according to data size, security target, and role."  
status: used  
version: v1
