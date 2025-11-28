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

below are the prompts used to generate 12 slides in the PDF:
---
```text
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 1:
“RFC 9861 IN ONE PICTURE — XOF FAMILY & LINEAGE”
Goal:
- Draw a single, research-grade family diagram that shows the lineage and relationships between:
• Keccak-p[1600] permutations
• SHA-3 and SHAKE (FIPS 202)
• NIST SP 800-185 (KMAC, TupleHash, ParallelHash, etc.) as a sibling branch
• TurboSHAKE128 and TurboSHAKE256
• KangarooTwelve KT128 and KT256
• HopMAC built on top of these XOFs
- Also indicate where RFC 9861 sits in this lineage and how it connects to registries (IANA, COSE).
Overall layout:
- Use a single panel with a clear hierarchical “family tree” / dependency graph.
- Place the most primitive object in the center: the Keccak permutation, and fan out to derived constructions.
- Reading order should be roughly top→down or center→outwards, with short labels explaining each step.
Core structure:
(1) Central primitive:
- In the center, draw a large block labeled:
“Keccak-p[1600, n_r] — 1600-bit permutation”
- Inside or just beneath, annotate:
• “Keccak-f[1600] = Keccak-p[1600, 24] (full-round)”
• “Round-reduced: Keccak-p[1600, 12]”
- Use two small color-coded tags for:
• “24 rounds → SHA-3 / SHAKE”
• “12 rounds → TurboSHAKE / KangarooTwelve (RFC 9861)”
(2) Upper or left branch — FIPS 202 family:
- From the “Keccak-p[1600, 24] / Keccak-f[1600]” tag, branch upwards or leftwards to a block labeled:
“FIPS 202 — SHA-3 & SHAKE”
- Under that, draw 2–4 small child nodes:
• “SHA3-256, SHA3-512 (fixed-length hashes)”
• “SHAKE128, SHAKE256 (XOFs)”
- Annotate key properties:
• “24-round permutation”
• “Fixed-length vs XOF”
• “Standardized in FIPS 202”
- Optionally, branch to a small “NIST SP 800-185” node with sublabels:
• “KMAC”, “TupleHash”, “ParallelHash”
to show its close relation, but keep this visually lighter (secondary branch).
(3) Lower or right branch — RFC 9861 family (focus region):
- From the “Keccak-p[1600, 12]” annotation, branch to a prominent node labeled:
“RFC 9861 — TurboSHAKE & KangarooTwelve”
- Under this node, create a structured family:
(A) TurboSHAKE branch:
- Two sibling blocks:
• “TurboSHAKE128”
– Sub-label: “XOF, ≈128-bit security”
– “Rate r = 168 bytes, capacity c = 32 bytes”
• “TurboSHAKE256”
– Sub-label: “XOF, ≈256-bit security”
– “Rate r = 136 bytes, capacity c = 64 bytes”
- Add a small note between them:
“Both use Keccak-p[1600, 12 rounds]; r + c = 1600 bits (sponge).”
(B) KangarooTwelve branch (on top of TurboSHAKE):
- From TurboSHAKE128, draw an arrow to:
“KT128 — tree XOF on TurboSHAKE128”
• Sub-label: “Parallelizable, ≈128-bit security”
- From TurboSHAKE256, draw an arrow to:
“KT256 — tree XOF on TurboSHAKE256”
• Sub-label: “Parallelizable, ≈256-bit security”
- Add a small tag near both KT nodes:
“Single-node (short messages) and tree-hashing (long messages) modes.”
(C) HopMAC:
- Above KT128/KT256, place a small box labeled:
“HopMAC — MAC construction using RFC 9861 XOFs”
- Connect it with arrows from KT128 and KT256 (or from TurboSHAKE and K12 together) to indicate:
“Builds MACs and KDFs on top of these XOFs.”
(4) Standards & registries annotations:
- Near the FIPS 202 branch, add a label:
“Standard: FIPS 202 (SHA-3/SHAKE)”
- Near the SP 800-185 node, add:
“Standard: NIST SP 800-185”
- Near the RFC 9861 node, add a distinct label:
“Standard: RFC 9861 (IETF)”
- On the right side, add a small table or box:
“Registries”
• “IANA: hash function identifiers for TurboSHAKE, KT”
• “COSE: algorithm IDs for use in protocols”
- Use fine-print labels, keeping them compact.
(5) Visual cues and legends:
- Use color or line style to distinguish:
• “Base permutation” level (Keccak-p[1600])
• “Hash/XOF functions” level (SHA-3, SHAKE, TurboSHAKE, KangarooTwelve)
• “Constructions on top” level (KMAC, HopMAC, KDF/MAC usage)
- Example:
• Base permutation: dark slate/grey
• Hash/XOF primitives: teal/blue
• Upper-level constructions (MACs/KDFs): accent color (orange or magenta)
- Add a tiny legend in one corner explaining this color coding.
Bottom strip:
- At the very bottom, add a 1-sentence distilled insight, such as:
“RFC 9861 defines four round-reduced Keccak-based XOFs and a MAC construction that extend the SHA-3 family with faster, parallelizable hashing and rich protocol integration via standardized registries.”
```
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 2:
“WHY NEW XOFS BEYOND SHA-3? — TRADE-OFF LANDSCAPE”
Goal:
- Draw a single, research-grade comparative figure that explains why RFC 9861 introduces TurboSHAKE and KangarooTwelve instead of just using SHA-2 or SHA-3/SHAKE.
- Show a trade-off landscape contrasting:
• SHA-2 (e.g., SHA-256/SHA-512)
• SHA-3 and SHAKE (FIPS 202)
• TurboSHAKE128 / TurboSHAKE256
• KangarooTwelve (KT128 / KT256)
- Emphasize differences in: performance, flexibility (XOF vs fixed-length), parallelism/tree hashing, domain separation, and structural complexity.
Overall layout:
- Partition the canvas into three regions:
(A) Trade-off Plane
(B) Property Matrix
(C) Design Timeline / Evolution
- Use consistent colors with Slide 1:
• Base / legacy hash family (SHA-2): grey/neutral.
• FIPS 202 (SHA-3/SHAKE, SP 800-185): teal/blue tones.
• RFC 9861 (TurboSHAKE, K12, HopMAC): accent color (orange or magenta).
- Reading order left→right: (A) → (B) → (C).
(A) TRADE-OFF PLANE — PERFORMANCE VS STRUCTURAL RICHNESS
- Draw a 2D plot occupying the left half of the slide.
- X-axis: “Performance / Throughput” (left = lower, right = higher).
- Y-axis: “Structural Flexibility & Parallelism” (bottom = simpler, top = more features).
- Mark and label 4–5 points:
1) “SHA-2 (SHA-256 / SHA-512)”
- Place in lower-middle: performance moderate, flexibility low.
- Optional tiny annotation:
“Merkle–Damgård, fixed-length, length-extension issue.”
2) “SHA-3 (SHA3-256 / SHA3-512)”
- Slightly above SHA-2 in flexibility (sponge structure), similar or slightly different in performance depending on depiction (do not over-claim).
- Annotation:
“Sponge, fixed-length outputs, 24-round Keccak-f[1600].”
3) “SHAKE128 / SHAKE256”
- Above SHA-3 (more flexible: XOF).
- Annotation:
“XOFs, arbitrary L, 24-round Keccak-f[1600].”
4) “TurboSHAKE128 / TurboSHAKE256”
- To the right of SHAKE (higher performance via reduced rounds).
- Similar vertical position (XOF, same rate/capacity as SHAKE) or slightly higher for additional interface features.
- Annotation:
“XOF, Keccak-p[1600, 12 rounds]; domain byte D for multiple independent streams.”
5) “KangarooTwelve (KT128 / KT256)”
- Positioned higher and to the right of TurboSHAKE.
- Annotation:
“Tree XOF on TurboSHAKE; built-in parallelism; good for long messages.”
- Optionally, draw a shaded “desired region” in the upper-right corner labeled:
“High performance + rich structure (XOF, parallelism, customization)”
and visually show that TurboSHAKE/K12 sit inside this region.
(B) PROPERTY MATRIX — FEATURE-LEVEL COMPARISON
- In the middle-right area, draw a compact table or grid (no more than 6 rows) with columns for:
• “SHA-2”
• “SHA-3 / SHAKE”
• “TurboSHAKE”
• “KangarooTwelve”
- Rows should capture key differentiating properties with concise labels, for example:
Row 1: “Output type”
- SHA-2: “Fixed-length (e.g., 256 bits)”
- SHA-3/SHAKE: “Fixed-length (SHA-3); XOF (SHAKE)”
- TurboSHAKE: “XOF (arbitrary-length)”
- K12: “Tree XOF (arbitrary-length)”
Row 2: “Permutation rounds”
- SHA-2: “non-Keccak (Merkle–Damgård)”
- SHA-3/SHAKE: “Keccak-f[1600, 24 rounds]”
- TurboSHAKE: “Keccak-p[1600, 12 rounds]”
- K12: “Tree over TurboSHAKE (12 rounds per call)”
Row 3: “Parallelism / tree hashing”
- SHA-2: “none in standard (Merkle tree external)”
- SHA-3/SHAKE: “no defined tree mode”
- TurboSHAKE: “sequential sponge; external tree needed”
- K12: “built-in tree hashing for long messages”
Row 4: “Domain separation / customization”
- SHA-2: “ad hoc (prepend tags, etc.)”
- SHA-3/SHAKE: “flexible but not standardized for all uses”
- TurboSHAKE: “explicit D byte for stream separation”
- K12: “D byte + customization string C + length_encode(|C|)”
Row 5: “Typical usage”
- SHA-2: “legacy protocols, wide deployment”
- SHA-3/SHAKE: “FIPS 202 compliant hashing & XOF”
- TurboSHAKE: “high-performance XOF in new designs”
- K12: “fast hashing of large messages, tree-based constructions”
- Keep text tightly compressed, research-style.
(C) DESIGN TIMELINE / EVOLUTION
- On the far right, draw a simple vertical or diagonal arrow representing concept evolution:
“SHA-2 → SHA-3/SHAKE → TurboSHAKE → KangarooTwelve”
- Each step is a labeled node on the arrow, with a very short “design motive” phrase:
Node 1: “SHA-2”
- “Wide adoption; Merkle–Damgård; length-extension.”
Node 2: “SHA-3 / SHAKE”
- “Keccak sponge; strong security margin; XOF via SHAKE.”
Node 3: “TurboSHAKE”
- “Round-reduced Keccak; faster XOF with explicit D-byte.”
Node 4: “KangarooTwelve”
- “Tree mode on TurboSHAKE; parallel, long-message friendly.”
- Near the TurboSHAKE/K12 nodes, add a small tag:
“RFC 9861 focus.”
Legend and bottom strip:
- Add a tiny legend explaining color or shape codes for:
• legacy / baseline constructions
• FIPS 202 / SP 800-185 family
• RFC 9861 family
- Bottom distilled insight (1 sentence), for example:
“TurboSHAKE and KangarooTwelve occupy the high-performance, high-flexibility corner of the Keccak-based design space, extending SHA-3/SHAKE with round-reduced XOFs and built-in tree hashing for modern protocol needs.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 3:
“SPONGE REFRESHER & XOF CONCEPT”
Goal:
- Draw a single, research-grade infographic that:
• Recaps the Keccak-style sponge construction (absorb/squeeze over a 1600-bit state).
• Explains the roles of rate r and capacity c.
• Contrasts fixed-length hash functions vs XOFs (extendable-output functions).
• Highlights the prefix property and the idea of requesting arbitrary output length L.
Overall layout:
- Partition the canvas into three regions:
(A) Sponge Conceptual Model (left)
(B) Absorb/Squeeze Algorithmic Flow (center)
(C) Fixed-Length vs XOF Comparison (right)
- Use the same color palette and typography as previous slides for consistency:
• Base state and structure: desaturated blue/teal.
• Capacity-related security region: darker purple/grey.
• XOF-specific elements: accent color (orange or magenta).
(A) SPONGE CONCEPTUAL MODEL
- Title for region: “(A) Sponge Construction — State, Rate, Capacity”.
- Draw a large horizontal rectangle representing the 1600-bit internal state.
• Label the full width: “1600-bit state”.
• Visually split it into two adjacent segments:
– Left segment labeled “rate r” (larger portion).
– Right segment labeled “capacity c” (smaller, darker shaded portion).
- Under the state, include concise annotations:
• “r + c = 1600 bits”
• “rate r: part of the state that is XORed with message blocks and used for output”
• “capacity c: hidden part, controls security level (~2^(c/2))”
- Above the state, draw a box labeled “Keccak-p[1600, n_r] permutation”.
• Arrow from state rectangle up into this box and back down, indicating that the permutation permutes the entire state.
• Small note: “Full-round Keccak-f[1600] uses 24 rounds; RFC 9861 uses 12-round Keccak-p[1600, 12].”
(B) ABSORB / SQUEEZE ALGORITHMIC FLOW
- Title for region: “(B) Absorb and Squeeze Phases”.
- Draw a left→right numbered pipeline with 5 steps:
Step 1: Input preparation
- Small box: “Message M (padded)” feeding into a splitter producing “r-bit blocks”.
- Label: “Pad M; split into blocks of r bits (or r bytes).”
Step 2: Absorb loop
- Show the state rectangle (rate+capacity) again.
- Arrow from one message block into the rate portion with label:
“XOR block into rate part of state”.
- Arrow from the modified state up through the permutation box:
“Apply Keccak-p[1600, n_r].”
- Use a loop indicator (curved arrow) and “repeat for all blocks”.
Step 3: Start of squeeze
- State rectangle after final absorb/permutation.
- Arrow from rate portion outwards labeled:
“Output first r bits (or bytes) as Z₀.”
Step 4: Continued squeeze
- Loop: permutation box above the state and arrows indicating:
“Apply permutation again; output next r bits (Z₁, Z₂, …)”.
- Show that outputs Z₀, Z₁, Z₂… are concatenated to form the final output.
Step 5: Stopping condition
- Simple note: “Stop when requested output length L is reached.”
- Use solid arrows for deterministic data flow.
- Optionally, add a subtle contrast between “absorbing phase” (blocks going in) and “squeezing phase” (bits coming out), e.g., different arrow colors or labels.
(C) FIXED-LENGTH HASH VS XOF
- Title for region: “(C) Fixed-Length Hash vs XOF”.
- Split this region into two small panels side-by-side:
Panel 1: Fixed-Length Hash
- Schematic: “H(M) → n-bit digest”.
- Show a box labeled “Hash function H” taking input M and producing a fixed-size output.
- Label: “Output length fixed by design (e.g., 256 bits).”
- Optional warning icon: “Cannot extend output without recomputing; often vulnerable to length-extension in Merkle–Damgård designs.”
Panel 2: XOF (Extendable-Output Function)
- Schematic: “XOF(M, L) → L-bit output (or L-byte)”.
- Show a box labeled “XOF” with:
• Inputs: “M”, “L”.
• Output arrow: “Z of length L”.
- Indicate that the same internal sponge state can be used to generate arbitrarily long output by continuing the squeeze phase.
- Add label: “Prefix property: output for shorter L is prefix of output for larger L (for the same M).”
- Between the two panels, optionally draw a small timeline-like illustration:
• For fixed-length: a single fixed-length block.
• For XOF: multiple blocks Z[0:L₁], Z[0:L₂], showing that one is a strict prefix of the other.
Legend and bottom strip:
- If necessary, include a tiny legend explaining:
• Color used for rate region vs capacity region.
• Style for absorb vs squeeze arrows.
- Bottom one-sentence distilled insight, for example:
“Keccak-based sponge constructions split a 1600-bit internal state into rate and capacity, absorbing message blocks into the rate and squeezing out arbitrary-length XOF outputs while using the hidden capacity portion to enforce a strong security margin.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
  • “(A) Conceptual Model”
  • “(B) Algorithmic Flow”
  • “(C) Complexity / Trade-offs”
  • “(D) Empirical Behavior”
- Each region should contain one core construct:
  • A single graph, a single flow diagram, or a single layered architecture.
  • 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
  • Left→right for narrative progression or pipeline stages.
  • Top→bottom for abstraction levels (theory at top, implementation at bottom).
  • Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.

Axes, notation, and labels:
- When showing plots or planes, always:
  • Label both axes with quantity and (if relevant) units.
  • Use tick marks and 2–5 reference values.
  • Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
  • E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
  • Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
  • Inputs, outputs, parameters, and latent variables.
  • Deterministic vs stochastic paths (e.g., solid vs dashed lines).

Context focus (deep research):
- Suitable for:
  • Formal protocol diagrams (message flows, rounds, adversary model).
  • ML training/evaluation pipelines, including data preprocessing, model, metrics.
  • Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
  • Distributed algorithms with nodes, links, and failure/partition regions.
  • Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
  • Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
  • Where the main complexity/cost is incurred (compute, memory, communication).
  • Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).

Advanced composition patterns:
- Hybrid diagrams:
  • Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
  • Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
  • Top: coarse-grained overview (modules, agents, layers).
  • Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
  • Side-by-side algorithms/models with identical axes and metrics for direct comparison.
  • Highlight differences using color, line style, or annotation.

Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
  • Number key steps (1–N) if depicting an algorithm.
  • Use (A), (B), (C) tags for regions and refer to them in labels.
  • Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.

Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
  “The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.

NOW INSTANTIATE THIS STYLE FOR SLIDE 4:
“TURBOSHAKE INTERFACE & PARAMETER SPACE”

Important correctness requirement:
- The parameter-space visualization for TurboSHAKE128 vs TurboSHAKE256 must respect the actual numeric differences:
  • TurboSHAKE128: r = 168 bytes (1344 bits), c = 32 bytes (256 bits).
  • TurboSHAKE256: r = 136 bytes (1088 bits), c = 64 bytes (512 bits).
- The “rate” and “capacity” segments MUST NOT be drawn with a common vertical split or equal-looking capacities.
  • Capacity of TurboSHAKE256 is twice that of TurboSHAKE128 and must look clearly larger.
  • Rate of TurboSHAKE128 is larger than the rate of TurboSHAKE256 and must look clearly longer.
- Do not reuse a schematic where the r/c boundary is identical for both; each instance has its own distinct r/c split.

Goal:
- Draw a single, research-grade infographic that:
  • Presents the formal interface TurboSHAKE(M, D, L).
  • Explains the roles and constraints of each parameter M, D, L.
  • Shows the parameter space of TurboSHAKE128 vs TurboSHAKE256 (rate, capacity, security level) with correct relative proportions.
  • Visualizes how the domain byte D provides domain separation and multiple independent “virtual hash functions”.

Overall layout:
- Partition the canvas into three regions:
  (A) Interface Signature & Semantics (left)
  (B) Parameter Table: TurboSHAKE128 vs TurboSHAKE256 (center)
  (C) Domain Separation via D (right)
- Use the same palette and typography as previous slides to keep the deck visually coherent:
  • Base structures in blue/teal.
  • RFC 9861-specific elements (TurboSHAKE, D-byte, security parameters) in accent orange or magenta.

(A) INTERFACE SIGNATURE & SEMANTICS
- Region title: “(A) TurboSHAKE Interface”.
- Draw a prominent function box in the upper part of this region:

  Box label:
    “TurboSHAKE(M, D, L) → Z”

  Beneath or inside the box, show the input parameters with concise descriptions:
    • “M: byte string (message)”
    • “D: OPTIONAL byte, 0x01–0x7F (domain separation)”
    • “L: positive integer (requested output length in bytes)”
    • “Z: byte string of length L (XOF output)”

- Below this, show a small schematic of input and output:

  • Left: a stack labeled “M” (message).
  • Small adjacent square labeled “D” (domain byte).
  • Arrow from (M, D) into the TurboSHAKE box.
  • Arrow from the box to a long bar labeled “Z (L bytes)” on the right.

- Add two concise bullet-style annotations near the function box:
  • “XOF semantics: shorter output is a prefix of longer output for same (M,D).”
  • “Output is a hash of (M, D); if D is fixed, this acts as a hash of M.”

- In fine print under the parameters, indicate default behavior:
  • “If D is omitted, treat D as 0x1F (default domain).”
  • “APIs without explicit D MUST use D = 0x1F.”

(B) PARAMETER TABLE — TURBOSHAKE128 VS TURBOSHAKE256
- Region title: “(B) Parameter Space: TurboSHAKE128 vs TurboSHAKE256”.

- Draw a medium-sized table or two stacked cards summarizing rate, capacity, and security:

  Table with 3 columns:
    Columns: “Instance”, “Rate r”, “Capacity c”.
    Rows:
      • “TurboSHAKE128 | 168 bytes (1344 bits) | 32 bytes (256 bits)”
      • “TurboSHAKE256 | 136 bytes (1088 bits) | 64 bytes (512 bits)”

  Under the table, add small annotations:
    • “Keccak-p[1600, 12 rounds]; r + c = 1600 bits.”
    • “Security strength ≈ min(c/2, 128 or 256 bits nominal).”

- Next to the table, draw TWO separate state bars to illustrate the sponge state split.
  This is crucial: each instance must have its own r/c boundary.

  • Place a heading above them: “State width = 1600 bits (per instance)”.
  • Draw two horizontal rectangles of equal total width, stacked vertically:
      - Top bar labeled on the left: “TurboSHAKE128”.
      - Bottom bar labeled on the left: “TurboSHAKE256”.

  • For TurboSHAKE128 (top bar):
      - Split the bar into a left “rate r” region and a right “capacity c” region.
      - Rate r = 1344 bits (84% of the bar width) → visually much longer than the capacity region.
      - Capacity c = 256 bits (16% of the bar width) → relatively narrow.
      - Color the rate region in blue/teal and the capacity region in purple/grey.
      - Place labels under the bar:
          “rate r = 168 bytes (1344 bits)”
          “capacity c = 32 bytes (256 bits)”

  • For TurboSHAKE256 (bottom bar):
      - Again split into left “rate r” and right “capacity c”.
      - Rate r = 1088 bits (68% of the bar width) → clearly shorter than the TurboSHAKE128 rate region.
      - Capacity c = 512 bits (32% of the bar width) → clearly wider, approximately twice the width of the TurboSHAKE128 capacity region.
      - Use the same colors (blue/teal for rate, purple/grey for capacity).
      - Labels under the bar:
          “rate r = 136 bytes (1088 bits)”
          “capacity c = 64 bytes (512 bits)”

  • Explicit correctness constraints for the drawing:
      - Do NOT use a single shared vertical divider for both bars.
      - The internal split between r and c must be at different positions for the two bars.
      - The capacity segment in TurboSHAKE256 must be visibly about 2× the width of the capacity segment in TurboSHAKE128.
      - The rate segment in TurboSHAKE128 must be visibly longer than in TurboSHAKE256.
      - It is acceptable to approximate the percentages visually, but the qualitative differences must be obvious.

  • Optionally, add a light 1D axis or tick marks above/below the bars:
      - Label: “bit position in 1600-bit state”.
      - Markers at 1088 and 1344 bits to indicate the r/c boundaries for each instance.
      - Small text: “r + c = 1600 bits (per instance)”.

(C) DOMAIN SEPARATION VIA D
- Region title: “(C) Domain Separation with D”.

- Visualize how the domain byte D enables multiple independent logical hash functions:

  1) Draw a single shared message stack “M” on the left.

  2) From this stack, draw three arrows to three parallel TurboSHAKE boxes arranged horizontally or in a slight arc.
     Each box has the same overall shape and style as in region (A).

     • Box 1 label: “TurboSHAKE(M, D₁, L₁)” with side annotation “D₁ = 0x1F (default domain)”.
     • Box 2 label: “TurboSHAKE(M, D₂, L₂)” with side annotation “D₂ = 0x01 (e.g., key derivation)”.
     • Box 3 label: “TurboSHAKE(M, D₃, L₃)” with side annotation “D₃ = 0x02 (e.g., commitment)”.

     Each arrow from M to a box should be annotated with its Dᵢ value (0x1F, 0x01, 0x02).

  3) From each TurboSHAKE box, draw a separate output bar:
     • Z₁, Z₂, Z₃ aligned to the right.
     • Annotate them with short captions:
         “Z₁: XOF output for domain D₁”
         “Z₂: XOF output for domain D₂”
         “Z₃: XOF output for domain D₃”

     Add a concise text block nearby:
       “Independent XOF instances for distinct D values.”
       “For fixed M, TurboSHAKE(M, D₁, L) and TurboSHAKE(M, D₂, L) behave as different virtual hash functions when D₁ ≠ D₂.”

- Add a small constraint annotation near D:
  • “D ∈ {0x01,…,0x7F} (non-zero, MSB = 0 → compatible with pad10*1).”
  • “D integrates the first padding bit and leaves room for the final padding bit.”

- Optionally, show one box or annotation for a high-level API that does not expose D:
  • A call like “TurboSHAKE(M, L)” with a side note:
      “High-level APIs may omit D; internally fixed to D = 0x1F (default domain).”

Legend and bottom strip:
- Legend (small, in a corner):
  • Color used for “TurboSHAKE engine boxes”.
  • Color used for “parameters (M, D, L)”.
  • Color used for “security / rate / capacity regions”.

- Bottom distilled insight (1 sentence), for example:
  “TurboSHAKE(M, D, L) exposes a simple three-parameter XOF interface where capacity sets the security level, rate sets throughput, and the optional byte D cleanly separates independent hash domains over the same message space, with TurboSHAKE128 and TurboSHAKE256 differing only in their rate–capacity split within the same 1600-bit state width.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 5:
“TURBOSHAKE INTERNALS — SPONGE PIPELINE”
Goal:
- Draw a single, highly detailed algorithmic diagram that walks through the internal operation of TurboSHAKE(M, D, L) as a sponge-based XOF using Keccak-p[1600, 12].
- Show the full pipeline from raw inputs (M, D, L) to padded message, block absorption into the state, permutation application, and iterative squeezing until L bytes of output are produced.
- Highlight the separation between:
• Input/domain processing,
• Absorb phase,
• Squeeze phase,
while keeping visual consistency with the earlier sponge refresher slide.
Overall layout:
- Partition the canvas into two main regions:
(A) Input Formation & Padding
(B) Absorb / Permute / Squeeze Pipeline
- Use a left→right flow for the algorithm, with explicit numbered steps.
- Reuse the same colors for:
• State and rate/capacity segments (blues/teals/purples),
• RFC 9861-specific features like D and round count (accent color).
(A) INPUT FORMATION & PADDING
- Region title: “(A) Input Formation and Padding”.
- Leftmost: show the formal inputs:
• Stack labeled “M (message bytes)”
• Small square labeled “D (domain byte, 0x01–0x7F; default 0x1F)”
• Scalar “L (output length in bytes)”
- Step 1 — Concatenation:
• Arrow from M and D into a box labeled:
“Step 1: M′ = M || D”
• Under the box, fine-print note:
“D integrates first padding bit and encodes domain separation.”
- Step 2 — Padding to rate:
• Arrow from M′ to a box labeled:
“Step 2: Pad M′ to multiple of rate r bytes”
• Under that box, annotate:
“Append 0x00 bytes as needed, then XOR 0x80 into last byte of last block.”
• To the right, show M′ after padding as a long bar split into equal-sized blocks labeled:
“r-byte blocks: B₀, B₁, …, B_{k−1}”
- Show r as a parameter, not fixed:
• Small note:
“r = 168 bytes (TS128) or 136 bytes (TS256).”
(B) ABSORB / PERMUTE / SQUEEZE PIPELINE
- Region title: “(B) Absorb, Permute, Squeeze”.
- Use a horizontal numbered pipeline with clear states:
Step 3 — Initial state:
- Draw a state rectangle with two segments:
• Left: “rate r” region.
• Right: “capacity c” region.
- Label: “Initial state = all zeros (1600 bits).”
- Optional note near capacity:
“c = 256 bits (TS128) or 512 bits (TS256).”
Step 4 — Absorb loop:
- Show B₀, B₁, …, B_{k−1} as a stack of blocks entering the rate portion.
- For a generic block Bᵢ, draw:
• Arrow from Bᵢ to rate segment with label:
“XOR Bᵢ into first r bytes of state.”
• Arrow from state up into a box labeled:
“Apply Keccak-p[1600, 12] permutation.”
• Arrow from that box back down into the state rectangle.
- Use a loop annotation over i:
“For i = 0..k−1: XOR & permute.”
- Color the permutation box in a distinct accent to emphasize “12-round Keccak-p[1600]”.
- Add small note:
“Same reduced-round permutation for both TurboSHAKE128 and TurboSHAKE256.”
Step 5 — Start of squeeze:
- Show the state rectangle after the last absorb permutation.
- Arrow from the rate region (left segment) to an output bar labeled:
“Z₀ = first r bytes of state”.
- Next to it, note:
“Append Z₀ to output.”
Step 6 — Continued squeeze:
- Loop structure:
• Arrow from state to permutation box again: “Apply Keccak-p[1600, 12]”.
• Arrow from rate region to another output chunk: “Z₁ = first r bytes”, “Z₂”, etc.
• These chunks concatenate to form Z = Z₀ || Z₁ || Z₂ || … until L bytes are collected.
- Use a short annotation:
“Repeat: permute → output r bytes, until |Z| ≥ L; truncate to L bytes.”
Step 7 — Output:
- On the far right, show the final output bar labeled:
“Z (L bytes) — return first L bytes of concatenated Zᵢ.”
- Optional note:
“XOF property: any prefix of Z corresponds to a shorter requested L.”
- Optionally, in a small inset at the bottom of this region, draw a micro comparison vs SHAKE:
• Two small permutation boxes:
– “SHAKE: Keccak-f[1600, 24 rounds]”
– “TurboSHAKE: Keccak-p[1600, 12 rounds]”
• An arrow or caption:
“TurboSHAKE uses fewer rounds per permutation call → higher throughput, with security level governed by capacity c.”
Legend and bottom strip:
- Legend (small corner):
• Color for state and its r/c split.
• Color for message blocks Bᵢ.
• Color for permutation boxes (Keccak-p[1600, 12]).
- Bottom 1-sentence distilled insight, for example:
“TurboSHAKE pads M∥D into r-byte blocks, XORs each into the rate portion of a 1600-bit state with 12-round Keccak permutations, and then repeatedly squeezes r-byte chunks until the requested XOF output length L is reached.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 6:
“KANGAROOTWELVE INTERFACE & MESSAGE ENCODING”
Goal:
- Draw a single, research-grade infographic that:
• Presents the formal interface KT(M, C, L) for KangarooTwelve (KT128 / KT256).
• Shows how the message and customization string are combined into an internal string S = M || C || length_encode(|C|).
• Explains the role of the customization string C and the length encoding in domain separation.
• Clearly separates the interface (what callers see) from the internal encoding (what the XOF actually hashes).
Overall layout:
- Partition the canvas into three regions:
(A) Interface Signature & Parameters (left)
(B) Message Encoding S = M ∥ C ∥ length_encode(|C|) (center)
(C) length_encode(|C|) Detail & Semantic Notes (right)
- Use the same color palette and typography as previous slides.
• API/interface elements: teal/blue.
• Internal encoding and domain-separation aspects: accent orange or magenta.
• Background and structural boxes: neutral greys/purples.
(A) INTERFACE SIGNATURE & PARAMETERS
- Region title: “(A) KangarooTwelve Interface”.
- Draw a prominent function box:
Label:
“KT(M, C, L) → Z”
with a subtitle:
“KT128 or KT256 (depending on underlying TurboSHAKE)”
- Under the function name, list parameters inside or just below the box:
• “M: message (byte string, arbitrary length)”
• “C: customization string (byte string, possibly empty)”
• “L: positive integer (requested output length in bytes)”
• “Z: byte string of length L (XOF output)”
- Show a schematic diagram:
• On the left, a tall stack labeled “M”.
• Beneath or next to it, a smaller stack labeled “C”.
• A scalar “L” as a small scalar node.
• Arrows from M and C into the KT box, with L as an additional parameter arrow.
• Arrow from the box to a long output bar Z on the right, labeled “Z (L bytes)”.
- Add 2–3 short annotations around the interface box:
• “KangarooTwelve = tree XOF built on TurboSHAKEX (X = 128 or 256).”
• “C allows per-application customization without new primitives.”
• “KT128 uses TurboSHAKE128; KT256 uses TurboSHAKE256.”
(B) MESSAGE ENCODING S = M ∥ C ∥ length_encode(|C|)
- Region title: “(B) Internal Message Encoding”.
- Depict the formation of the internal string S step by step:
1) On the left, repeat the M and C stacks (or refer to them via small icons labeled “M” and “C”).
2) Draw a concatenation pipeline:
- First box:
Label: “Concatenate M and C”
Output bar labeled: “M || C”
- Second box:
Label: “Append length_encode(|C|)”
Output bar labeled: “S = M || C || length_encode(|C|)”
3) Show the final S as a long horizontal bar split into three segments with bracket annotations:
• Left segment: “M”
• Middle segment: “C”
• Right segment: “length_encode(|C|)”
Each segment should be clearly labeled above or below the bar.
- Add concise notes under the S bar:
• “S is the exact string passed to the underlying tree XOF construction.”
• “C is always accompanied by an explicit encoding of its length; this makes the boundary between M and C unambiguous.”
• “Different (M, C) pairs with the same concatenation M||C are distinguished by length_encode(|C|).”
(C) length_encode(|C|) DETAIL & SEMANTIC NOTES
- Region title: “(C) length_encode(|C|) and Domain Separation”.
- Draw a small inset diagram to illustrate the idea of length encoding:
1) Represent |C| as an integer (for example, k).
• Small node labeled “k = |C| (length of C in bytes)”.
2) Arrow from k to a box labeled:
“length_encode(k)”
Sub-label:
“Self-delimiting length encoding as defined in RFC 9861 (conceptual depiction).”
3) From that box, show a short bar split into 2–4 bytes:
• Example label: “b₀, b₁, …, b_n”.
• Annotate generically (do NOT commit to specific bit-level format):
“Encodes k as a finite byte sequence that can be parsed unambiguously.”
- Under or beside this diagram, add bullet-style annotations:
• “Ensures (M, C) ↦ S is injective: no ambiguity about where M ends and C begins.”
• “Protects against simple concatenation collisions between different (M, C) pairs.”
• “Integrates C into the input in a structured way, compatible with tree hashing and domain separation strategies.”
- Optionally, show two example rows illustrating disambiguation:
Example 1:
- “M₁ = ‘abc’, C₁ = ‘def’”
- “S₁ = ‘abc’ || ‘def’ || length_encode(3)”
Example 2:
- “M₂ = ‘abcd’, C₂ = ‘ef’”
- “S₂ = ‘abcd’ || ‘ef’ || length_encode(2)”
Place a small note:
“Even if concatenations ‘abc’||‘def’ and ‘abcd’||‘ef’ overlap in a naive sense, the appended length encodings differ and prevent collisions at the S level.”
Legend and bottom strip:
- In a small legend box, clarify:
• Color coding for M, C, and length_encode(|C|) segments.
• Symbol conventions for concatenation (||) and encoding.
- Bottom distilled insight (1 sentence), for example:
“KangarooTwelve exposes a simple KT(M, C, L) interface while internally encoding its input as S = M ∥ C ∥ length_encode(|C|), ensuring unambiguous customization-aware hashing over TurboSHAKE128/256.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 7:
“KANGAROOTWELVE MODES — SINGLE NODE VS TREE HASHING”
Goal:
- Draw a single, research-grade diagram that contrasts the two operational modes of KangarooTwelve:
• Single-node mode for short messages (|S| ≤ 8192 bytes).
• Tree-hashing mode for long messages (|S| > 8192 bytes).
- Clearly show:
• How the internal encoded string S (from the previous slide: S = M ∥ C ∥ length_encode(|C|)) is processed in each mode.
• The chunking of S into 8192-byte pieces S₀,…,Sₙ₋₁ for long messages.
• How intermediate chaining values CVᵢ are computed using TurboSHAKEX with a specific domain byte.
• How the final node is formed and fed to TurboSHAKEX with a different domain byte.
• The domain separation values for SingleNode, IntermediateNode, and FinalNode.
Overall layout:
- Use a split layout with two main horizontal bands:
(A) Short message: Single-node mode (top band)
(B) Long message: Tree-hashing mode (bottom band)
- On the right side, add a narrow region:
(C) Domain-byte legend
- Use consistent color coding:
• KangarooTwelve as a whole: teal/blue.
• TurboSHAKE calls: accent (orange or magenta).
• S segments and chunks: neutral blues/greys.
• Domain-byte semantics: highlighted with small colored tags.
(A) SHORT MESSAGE (|S| ≤ 8192 BYTES) — SINGLE-NODE MODE
- Region title: “(A) Short Messages (Single-node mode, |S| ≤ 8192)”.
- Left side: show the internal string S coming from KT(M, C, L):
• Draw a long bar labeled:
“S = M ∥ C ∥ length_encode(|C|)”
• Under it, small condition:
“If |S| ≤ 8192 bytes: no tree; single-node mode”.
- Middle: show a single TurboSHAKEX call:
• Box labeled:
“TurboSHAKEX(S, D = 0x07, L)”
where X ∈ {128, 256}.
• Inside or below, annotate:
“SingleNode domain: D = 0x07”.
- Right: show the output:
• Arrow from TurboSHAKE box to a bar labeled:
“KT128(M, C, L) = TurboSHAKE128(S, 0x07, L)”
“KT256(M, C, L) = TurboSHAKE256(S, 0x07, L)”
• Keep formulas compact; use two lines or a stacked label.
- Optionally, add one short note:
• “No parallelism needed; direct XOF call over S.”
(B) LONG MESSAGE (|S| > 8192 BYTES) — TREE-HASHING MODE
- Region title: “(B) Long Messages (Tree mode, |S| > 8192)”.
- Left: repeat S bar, but now with chunk boundaries:
• Bar labeled “S = M ∥ C ∥ length_encode(|C|)”.
• Beneath, annotation:
“Split S into 8192-byte chunks: S = S₀ ∥ S₁ ∥ … ∥ Sₙ₋₁”.
• Visually slice the bar into equal chunks S₀, S₁,…,Sₙ₋₂ and a potentially shorter final chunk Sₙ₋₁.
- Middle-left: leaf computations (parallel):
• For chunks S₁,…,Sₙ₋₁ (all except S₀), draw multiple parallel branches:
– Each branch: Sᵢ → TurboSHAKEX box → CVᵢ.
– Box label:
“TurboSHAKEX(Sᵢ, D = 0x0B, t)”
– Under box:
“IntermediateNode domain 0x0B”
“t = 32 bytes (KT128) or 64 bytes (KT256)”
• Arrows from each TurboSHAKE leaf box to small blocks labeled “CV₁, CV₂, …, CVₙ₋₁”.
• Add a parallelism annotation:
“Leaf CVᵢ can be computed in parallel”.
- Middle-right: final node formation:
• Draw a large box labeled:
“Construct FinalNode input”.
• Feed into this box:
– S₀
– A constant block (e.g., label: “0x03 followed by zeros”)
– The sequence CV₁,…,CVₙ₋₁
– length_encode(n−1)
– A trailing constant label “0xFF ∥ 0xFF”
• Do NOT show exact bytes; just label inputs as high-level blocks with text like:
“S₀”, “constant 0x03‖00…00”, “CV₁…CVₙ₋₁”, “length_encode(n−1)”, “0xFF‖0xFF”.
- Right: final TurboSHAKE call and output:
• From the “FinalNode input” box, arrow into a TurboSHAKEX box:
– Label:
“TurboSHAKEX(FinalNode, D = 0x06, L)”
with note:
“FinalNode domain 0x06”.
• Arrow from this box to the final output bar:
– For KT128:
“KT128(M, C, L) = TurboSHAKE128(FinalNode, 0x06, L)”
– For KT256:
“KT256(M, C, L) = TurboSHAKE256(FinalNode, 0x06, L)”
• Add a short note:
“FinalNode aggregates S₀ and all CVᵢ into a single root call.”
(C) DOMAIN-BYTE LEGEND
- Region title: “(C) Domain Separation Values”.
- Draw a small table or legend box listing the key domain bytes used by KangarooTwelve:
• Row 1:
– Label: “SingleNode”
– D = 0x07
– Comment: “Short messages, no tree.”
• Row 2:
– Label: “IntermediateNode”
– D = 0x0B
– Comment: “Leaf nodes; each chunk Sᵢ, i ≥ 1, produces CVᵢ.”
• Row 3:
– Label: “FinalNode”
– D = 0x06
– Comment: “Root node; combines S₀ and all CVᵢ.”
- Optionally color-code each row with a subtle accent color stripe matching the D tags used in bands (A) and (B).
Legend and bottom strip:
- If needed, add a tiny legend for:
• Shapes representing chunks Sᵢ.
• Boxes representing TurboSHAKEX calls.
• Boxes representing node-role (leaf vs root).
- Bottom 1-sentence distilled insight, for example:
“KangarooTwelve uses a single-node TurboSHAKE call for short inputs and a domain-separated tree of intermediate and final nodes for long inputs, enabling parallel processing while preserving clear security domains via distinct D-byte values.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 8:
“HOPMAC & GENERIC MAC/KDF CONSTRUCTIONS”
Goal:
- Draw a single, research-grade diagram that:
• Shows the structure of HopMAC as defined on top of KangarooTwelve/TurboSHAKE (inner keyless compression + outer keyed MAC).
• Contrasts HopMAC with generic “XOF-as-MAC” and “XOF-as-KDF” usages.
• Highlights the side-channel advantage of a keyless inner call (only the outer call needs SCA protection).
• Shows how RFC 9861 XOFs (TurboSHAKE128/256, KT128/256) can be used for MAC and KDF in a clean, pattern-based way.
Overall layout:
- Partition the canvas into three regions:
(A) HopMAC Conceptual Structure (left)
(B) HopMAC Algorithmic Flow (center)
(C) Generic MAC & KDF Patterns Using RFC 9861 XOFs (right)
- Use consistent colors:
• KangarooTwelve / TurboSHAKE XOF blocks: teal/blue.
• Keyed MAC/KDF wrappers: accent (orange or magenta).
• Keys and secrets: slightly darker tone with lock icon or “K” label.
• Messages/customization strings: neutral blues/greys.
(A) HOPMAC CONCEPTUAL STRUCTURE
- Region title: “(A) HopMAC on RFC 9861 XOFs”.
- Draw a two-layer schematic reminiscent of HMAC but with a keyless inner layer:
1) Inner layer (keyless compression):
• Box labeled:
“Inner: KangarooTwelve(M, C, L_inner) — keyless”
• Inputs:
– M: message
– C: optional customization string
• Output:
– V: intermediate digest (fixed or short length).
• Annotate:
“Keyless compression of (M, C) to digest V.”
2) Outer layer (keyed MAC):
• Box on top or to the right labeled:
“Outer: MAC(K, V) via KangarooTwelve / TurboSHAKE”
• Inputs:
– K: secret key
– V: digest from inner layer
• Output:
– T: MAC tag.
• Note:
“Only outer call is keyed → only this call needs SCA protection.”
- Connect inner to outer:
• Arrow from V output of inner box to V input of outer MAC box.
• Highlight the key difference vs HMAC:
– Add a small comparison annotation:
“Unlike HMAC: inner call is keyless; outer call uses key once.”
- Add a concise annotation in the corner:
• “HopMAC = 2 calls (inner K12 XOF, outer keyed XOF).”
• “Designed to reduce side-channel attack surface on the key.”
(B) HOPMAC ALGORITHMIC FLOW
- Region title: “(B) HopMAC Flow (informal)”.
- Draw a left→right pipeline with numbered steps:
Step 1:
- Inputs:
• K: secret key.
• M: message.
• C: optional customization string.
- Visual: three elements feeding into the pipeline.
Step 2 — Inner K12 compression:
- Box labeled:
“1. V = KT128(M, C, L_v) or KT256(M, C, L_v) (keyless)”
- L_v is a short fixed length (e.g., 32 or 64 bytes); represent as parameter L_v without choosing a hard-coded value.
- Output: bar labeled “V (digest)”.
Step 3 — Outer keyed call:
- Box labeled something like:
“2. T = KT128(V, C_outer(K), L_t) or TurboSHAKE-based MAC(K, V, L_t)”
- Illustrate that K is used only in this outer layer:
• Arrow from K to a small transformation box “key formatting / outer customization” producing “C_outer(K)” or “K_formatted”.
• Arrow from V and this formatted key into the outer MAC box.
Step 4 — Output:
- Output bar labeled:
“T (MAC tag, L_t bytes)”.
- Around this pipeline, add 2–3 comments:
• “Inner call has no key → no key-dependent branching or timing.”
• “Outer call can be implemented with masking / constant-time code.”
• “Security is related to K12/TurboSHAKE XOF security + standard MAC reduction.”
- You may explicitly depict “SCA protection boundary” around the outer call:
• A dashed boundary region around the outer MAC box labeled “Side-channel hardened region”.
(C) GENERIC MAC & KDF PATTERNS USING RFC 9861 XOFS
- Region title: “(C) Generic MAC & KDF Patterns with TurboSHAKE/KT”.
- Split this region into two small conceptual sub-panels:
Panel 1 — Generic MAC Patterns:
- Draw a small cluster of patterns showing how to use TurboSHAKE or K12 as a MAC without HopMAC:
Pattern A:
• Label:
“MAC_A(K, M) = XOF(K || M, L_t)”
• Box: XOF = TurboSHAKE128, TurboSHAKE256, KT128, or KT256.
• Inputs:
– “K || M” as concatenated input.
Pattern B:
• Label:
“MAC_B(K, M) = KT128(M, C = K, L_t)”
• Box: “KT128(M, C, L_t)”.
• Show K feeding into the C input (customization string) while M is the main message.
Small annotation:
• “RFC 9861 allows using TurboSHAKE/KT directly as MACs by prepending/appending keys or using key as customization C.”
• “HopMAC is the recommended structured MAC; these are generic patterns.”
Panel 2 — Generic KDF Pattern:
- Draw a small KDF construction based on an RFC 9861 XOF:
• Box labeled:
“KDF(K, info, L_total) = XOF(K || info, L_total)”
or
“XOF(K, D_info, L_total) with info in D/C”.
• Input:
– K: master key.
– info: context string (e.g., “app id”, “key usage”).
• Output:
– Several derived keys K₁, K₂, K₃ obtained by slicing the XOF output:
“K₁ = first ℓ bits, K₂ = next ℓ bits, …”.
• Annotate:
• “XOFs (TurboSHAKE, KT) are natural KDF building blocks due to arbitrary-length output.”
• “Domain separation via D/C prevents cross-use collisions between MAC and KDF roles.”
Legend and bottom strip:
- Small legend:
• Color for “XOF engines (TurboSHAKE/KT)”.
• Color for “keys K”.
• Color for “digests V / tags T / derived keys”.
- Bottom distilled insight, for example:
“HopMAC builds a MAC from KangarooTwelve using a keyless inner compression and a single keyed outer call, while RFC 9861 XOFs also support straightforward MAC and KDF patterns by hashing keys and context with domain separation.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 9:
“SECURITY LEVELS, OUTPUT LENGTH & FAMILY OVERVIEW”
Goal:
- Draw a single, research-grade figure that:
• Maps the four main RFC 9861 XOF instances (TurboSHAKE128, TurboSHAKE256, KT128, KT256) to their intended security levels and typical output-length choices.
• Shows how these instances relate to each other as a family (hash/XOF, tree XOF, MAC/KDF usage).
• Clarifies the relationship between capacity c, nominal security strength, and recommended minimum output lengths.
• Gives protocol designers an at-a-glance guide for “which variant do I pick for which target security and output length?”.
Overall layout:
- Partition the canvas into three regions:
(A) Family Grid: Instances × Security Levels
(B) Output Length vs Security Guidance
(C) Role/Usage Overview (Hash, XOF, MAC, KDF)
- Maintain the same color scheme as previous slides:
• Base RFC 9861 instances (TS/KT): teal/blue.
• Security-related annotations (bits, capacity, min L): accent (orange/magenta).
• Background organization: neutral greys/purples.
(A) FAMILY GRID — INSTANCES × PARAMETERS
- Region title: “(A) RFC 9861 Instances and Parameters”.
- Draw a compact 4-row grid, one row per instance:
Columns (suggested):
1) “Instance”
2) “Underlying primitive”
3) “Rate r (bytes)”
4) “Capacity c (bytes)”
5) “Nominal security level”
Rows:
- Row 1:
• Instance: “TurboSHAKE128”
• Underlying primitive: “Keccak-p[1600, 12] sponge”
• r: “168 bytes”
• c: “32 bytes (256 bits)”
• Security: “≈128-bit”
- Row 2:
• Instance: “TurboSHAKE256”
• Underlying primitive: “Keccak-p[1600, 12] sponge”
• r: “136 bytes”
• c: “64 bytes (512 bits)”
• Security: “≈256-bit”
- Row 3:
• Instance: “KT128”
• Underlying primitive: “Tree XOF on TurboSHAKE128”
• r: “168 bytes (inner)”
• c: “32 bytes (256 bits)”
• Security: “≈128-bit”
- Row 4:
• Instance: “KT256”
• Underlying primitive: “Tree XOF on TurboSHAKE256”
• r: “136 bytes (inner)”
• c: “64 bytes (512 bits)”
• Security: “≈256-bit”
- Under the grid, add a concise annotation:
• “Security strength is governed primarily by capacity c and the reduced-round Keccak-p[1600, 12]; KT128/KT256 inherit the underlying TurboSHAKE security (modulo tree composition).”
(B) OUTPUT LENGTH VS SECURITY GUIDANCE
- Region title: “(B) Output Length L and Security Targets”.
- Draw a 2D schematic or small chart that helps select L for typical use cases:
1) Horizontal axis: “Output length L (bytes)” with indicative ticks:
• 16, 32, 64, 128, “arbitrary”.
2) Vertical grouping: two bands for “≈128-bit” and “≈256-bit” security.
- Within this structure, place 4 labeled bars/markers:
• For TurboSHAKE128:
– Place a bar starting at 32 bytes extending right (“Recommended L ≥ 32 bytes for ≈128-bit collision resistance”).
– Label near the bar:
“TurboSHAKE128: pick L ≥ 32 bytes for typical 128-bit-strength uses (hashing, MAC, KDF).”
• For TurboSHAKE256:
– Place a bar starting at 64 bytes extending right.
– Label:
“TurboSHAKE256: pick L ≥ 64 bytes for typical 256-bit-strength uses.”
• For KT128:
– Similar to TurboSHAKE128, but annotate:
“KT128: same security target as TurboSHAKE128; tree mode optimized for long messages.”
• For KT256:
– Similar to TurboSHAKE256 with annotation:
“KT256: same security target as TurboSHAKE256; tree mode optimized for long messages.”
- Add 2–3 concise bullet-like notes near the chart:
• “Using L shorter than 2·security_bits/8 may waste security margin but is generally safe for some applications; recommended minima provide comfortable collision/preimage robustness.”
• “Because these are XOFs, longer outputs can be requested when protocol needs multiple subkeys or tags — but security is still bounded by the capacity/security level, not by L alone.”
• “Collision/preimage guarantees depend on capacity and construction, not simply on L, but short outputs reduce brute-force cost.”
(C) ROLE / USAGE OVERVIEW — WHERE EACH INSTANCE FITS
- Region title: “(C) Family Roles and Typical Uses”.
- Draw a small “role map” with the four instances as nodes placed in a 2×2 conceptual grid:
Suggested axes:
- Horizontal: “Primitive style” — “Flat XOF (single-node)” on left, “Tree XOF (long-message optimized)” on right.
- Vertical: “Target security” — “≈128-bit” on top, “≈256-bit” on bottom.
- Place nodes:
• Top-left: “TurboSHAKE128 — general-purpose 128-bit XOF”.
• Bottom-left: “TurboSHAKE256 — general-purpose 256-bit XOF”.
• Top-right: “KT128 — 128-bit tree XOF (fast on large inputs)”.
• Bottom-right: “KT256 — 256-bit tree XOF (fast on large inputs)”.
- For each node, attach 2–3 short labels indicating typical use cases:
TurboSHAKE128:
• “Hash function replacement in new designs.”
• “XOF-based KDF for 128-bit keys.”
• “MAC/PRF core where 128-bit security is sufficient.”
TurboSHAKE256:
• “High-assurance hashing.”
• “KDF for 256-bit keys.”
• “Protocols needing ≥256-bit security margin.”
KT128:
• “Fast hashing of long messages (files, transcripts).”
• “Merkle-like tree hashing without external tree structure.”
• “Streaming contexts with parallel processing.”
KT256:
• “Same as KT128 but with 256-bit target security.”
• “High-assurance content-addressable storage, long transcripts, etc.”
- Optionally, show a small arrow from TS128→KT128 and TS256→KT256 to remind that KT variants sit “on top of” TurboSHAKE.
Legend and bottom strip:
- Small legend explaining:
• Color used for 128-bit vs 256-bit instances.
• Node shapes or borders for TurboSHAKE vs KangarooTwelve.
- Bottom 1-sentence distilled insight, for example:
“TurboSHAKE128/256 and KT128/256 form a coherent XOF family where capacity c fixes the security level (≈128 or ≈256 bits), while output length L and tree vs flat mode let designers trade off digest size, performance, and long-message behavior without leaving the same Keccak-based framework.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 10:
“SECURITY ARGUMENT STACK & MISUSE RESISTANCE”
Goal:
- Draw a single, research-grade figure that:
• Shows the layered security argument for RFC 9861 constructions: from the underlying Keccak permutation, through the sponge/XOF layer (TurboSHAKE), to the tree construction (KangarooTwelve) and higher-level uses (HopMAC, MAC/KDF).
• Highlights key assumptions and where they enter the reasoning.
• Summarizes misuse resistance properties (length-extension resistance, domain separation, key separation, robustness under common protocol mistakes).
• Shows side-channel (SCA) and masking considerations: low algebraic degree vs SHA-2, keyless inner calls, where constant-time implementations are needed.
Overall layout:
- Partition the canvas into three regions:
(A) Layered Security Argument Stack (left, vertical layers)
(B) Misuse & Protocol-Level Resistance (center)
(C) Side-Channel & Implementation Considerations (right)
- Use consistent colors:
• Core Keccak permutation & sponge layer: deep blue/purple.
• RFC 9861 constructions (TurboSHAKE, K12, HopMAC): teal/blue with accent outlines.
• Assumptions, adversary, and misuse scenarios: accent (orange/magenta).
(A) LAYERED SECURITY ARGUMENT STACK
- Region title: “(A) Security Argument Stack (Conceptual)”.
- Draw a vertical stack of 4–5 layers, each as a wide horizontal block, with arrows flowing from bottom to top:
Layer 1 (bottom):
- Label: “Keccak-p[1600, n_r] permutation security”.
- Subtext:
• “Assumption: 12-round Keccak-p[1600, 12] is a good permutation, with no feasible structural attacks.”
• “Inherited analysis from Keccak team and SHA-3 competition community.”
- Small note: “Reference primitive; also 24-round Keccak-f[1600] used in SHA-3/SHAKE.”
Layer 2:
- Label: “Sponge/XOF construction (TurboSHAKE)”.
- Subtext:
• “Assumes standard sponge security bounds given permutation security.”
• “Capacity c (256 or 512 bits) ⇒ ~2^(c/2) collision resistance, ~2^c preimage bound (modulo round reduction).”
• “Domain separation via D ensures independent XOF instances.”
Layer 3:
- Label: “Tree hashing (KangarooTwelve)”.
- Subtext:
• “Uses Sakura-inspired tree framing; proven to preserve security of underlying sponge.”
• “Intermediate nodes and final node are domain-separated (0x0B, 0x06, 0x07).”
• “Parallelism does not reduce security below that of TurboSHAKE, given correct framing.”
Layer 4:
- Label: “Constructions on top (HopMAC, MAC/KDF patterns)”.
- Subtext:
• “Security reduces to XOF security under standard MAC/KDF reductions.”
• “Keyless inner call in HopMAC avoids leaking keys via inner state.”
Layer 5 (optional top strip):
- Label: “Protocol instantiations (COSE, applications)”.
- Subtext:
• “As long as domain separation and usage guidelines are respected, protocol-level security reduces to above layers.”
- On the left side of the stack, add a vertical arrow labeled “Assumptions flow upward”, indicating that each layer’s security argument builds on the one below.
(B) MISUSE & PROTOCOL-LEVEL RESISTANCE
- Region title: “(B) Misuse Resistance Properties”.
- Draw a set of 3–4 “misuse scenarios” as boxes or icons aligned vertically, each with a short label and a “resistance summary”:
Scenario 1: Length-extension-style misuse
- Box label: “Using XOF output as a MAC tag / hash directly, attacker appends data”.
- Annotation:
• “Sponge-based XOFs (TurboSHAKE/K12) do not suffer classical Merkle–Damgård length extension.”
• “Danger remains if protocol naively chains hashes, but no trivial ‘append without key’ attack as in SHA-2.”
Scenario 2: Re-using the same XOF instance for multiple roles
- Box label: “Same TurboSHAKE instance for MAC, KDF, and hashing, without domain separation.”
- Annotation:
• “RFC 9861 provides domain byte D and customization C to isolate roles.”
• “Guideline: always use distinct D/C for different roles to avoid cross-protocol collisions.”
Scenario 3: Short output misuse
- Box label: “Choosing too-short L for tags or identifiers.”
- Annotation:
• “Security still bounded by capacity, but short outputs reduce brute-force cost.”
• “Recommended minima: ≥32 bytes (128-bit) and ≥64 bytes (256-bit) for robust collision/preimage margins.”
Scenario 4: Partial-tree misuse
- Box label: “Cutting off parts of the K12 tree or re-using CVᵢ values out of context.”
- Annotation:
• “Sakura-style framing ensures that valid trees have unique encodings.”
• “But protocols must not expose internal CVᵢ as independent digests without additional domain separation.”
- Optionally, draw small colored badges next to each scenario:
• “Good” (resists classic issue) vs “Warning” (requires protocol care).
(C) SIDE-CHANNEL & IMPLEMENTATION CONSIDERATIONS
- Region title: “(C) Side-Channel & Implementation Aspects”.
- Draw a conceptual diagram with:
1) Algebraic degree & masking:
- Box labeled:
“Low algebraic degree (Keccak-based) vs SHA-2”.
- Annotation:
• “Keccak’s low algebraic degree makes masked implementations easier/cheaper than SHA-2.”
• “Fewer nonlinear operations per round → more SCA-friendly when properly implemented.”
2) Keyless vs keyed calls:
- Two side-by-side mini diagrams:
Diagram A:
• Label: “Keyless inner call (K12 / HopMAC inner)”.
• Inputs: only public data (M, C).
• Note: “No key-dependent branching; can reuse generic optimized code.”
Diagram B:
• Label: “Keyed outer call (HopMAC, MAC/KDF)”.
• Inputs: “K” and digest V.
• Boundary drawn around this box with label:
“Side-channel hardened: constant-time, masked, protected environment”.
- Add a short text:
• “Security guidance: treat keyed K12/TurboSHAKE uses as cryptographic primitives requiring constant-time, SCA-safe implementations; keyless calls can be optimized differently.”
3) Round-reduction vs margin:
- Small chart or side note:
• Two bars:
– “SHAKE: Keccak-f[1600, 24 rounds]” (higher bar).
– “TurboSHAKE/K12: Keccak-p[1600, 12 rounds]” (lower bar).
• Annotation:
“RFC 9861 chooses 12 rounds as a performance/security trade-off, relying on available cryptanalytic evidence for comfortable margins at 128/256-bit capacity settings.”
- Around this region, add 2–3 compact bullets summarizing implementation guidance:
• “Avoid reusing keyed state across unrelated operations; use fresh domain bytes and customization.”
• “Use constant-time, masking, and fence instructions where appropriate for keyed calls.”
• “Leverage keyless K12/TurboSHAKE for hashing large public data to minimize high-assurance SCA code footprint.”
Legend and bottom strip:
- Legend (small corner):
• Color coding for “assumption layers”, “misuse scenarios”, and “implementation/SCA aspects”.
- Bottom distilled insight (1 sentence), for example:
“The security of TurboSHAKE, KangarooTwelve, and HopMAC rests on Keccak-p[1600, 12] and sponge/tree reductions, with domain separation and keyless inner calls providing strong resistance to typical misuse patterns and a favorable profile for side-channel-hardened implementations.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 11:
“TESTING, VECTORS & REGISTRIES (INTEROPERABILITY VIEW)”
Goal:
- Draw a single, research-grade figure that:
• Explains the test vector strategy for RFC 9861 (coverage across message lengths, boundary at 8192 bytes, customization strings, and output lengths).
• Shows two concrete example vectors (one TurboSHAKE, one KangarooTwelve) in a schematic, not hex-dump-heavy, manner.
• Connects these vectors and algorithms to interoperability registries: IANA hash function identifiers and COSE algorithm IDs.
• Gives implementers a visual mental model of how to validate their implementation and plug it into standard protocol ecosystems.
Overall layout:
- Partition the canvas into three regions:
(A) Test Vector Strategy & Coverage (left)
(B) Example Vectors (TurboSHAKE & K12) (center)
(C) Interoperability Registries (IANA / COSE) (right)
- Preserve the same color palette as earlier slides:
• RFC 9861 algorithms (TS/KT): teal/blue.
• Testing and validation signal: accent (orange/magenta).
• Registry/interop elements: neutral + accent frames.
(A) TEST VECTOR STRATEGY & COVERAGE
- Region title: “(A) Test Vector Strategy”.
- Depict the strategy as a coverage diagram rather than raw examples:
1) Message-length coverage:
- Draw a horizontal axis labeled “Message length |M| (bytes)”.
- Mark points such as:
• Very short (0, 1, small)
• Around the 8192-byte threshold
• Larger multi-block messages
- Over this axis, draw several small colored intervals or markers labeled:
• “Short messages (single block)”
• “Near 8192-byte boundary (tree mode switch)”
• “Long multi-chunk messages”
- Annotation:
“Vectors selected to cover both ≤8192-byte and >8192-byte regimes, stressing the tree boundary.”
2) Customization string coverage:
- Draw a small panel showing C values:
• “C = empty”
• “C = short string”
• “C = longer string”
- Indicate that some vectors use empty C, others use non-empty customization.
- Note:
“Vectors ensure that S = M ∥ C ∥ length_encode(|C|) is exercised with different |C|.”
3) Output length coverage:
- Draw a mini axis labeled “L (output length in bytes)”.
- Mark representative values:
• small (e.g., 32)
• medium (e.g., 64)
• larger (e.g., 200+)
- Annotation:
“Vectors request multiple output lengths per function to test XOF behavior and prefix property.”
4) Pattern function mention:
- Add a small box labeled:
“Patterned messages ptn(n)”
with subtext:
“Messages follow structured byte patterns to detect alignment/padding issues.”
- Summarize this region with a compact sentence:
“Vectors are chosen to span length regimes, customization usage, and output sizes, using patterned inputs to detect subtle bugs in padding, tree framing, and squeezing.”
(B) EXAMPLE VECTORS (TURBOSHAKE & K12)
- Region title: “(B) Example Test Vectors (Schematic)”.
- Draw two stacked “cards”, one for TurboSHAKE and one for KangarooTwelve.
Card 1: TurboSHAKE example
- Header: “TurboSHAKE128 example (schematic)”.
- Inside the card, present the structure rather than full hex:
• Inputs:
– “M = ptn(n₁) (structured byte pattern of length n₁)”
– “D = 0x1F (default domain)”
– “L = L₁ bytes”
• Function:
– “Z = TurboSHAKE128(M, D, L₁)”
• Output:
– Show a bar labeled:
“Z[0..L₁−1] = 0x… (see RFC 9861 for exact bytes)”
– Under the bar, add a note:
“Implementation should match the published hex string exactly.”
• Side annotation:
– “This example exercises: default D, single-mode (no tree), specific L₁.”
Card 2: KangarooTwelve example
- Header: “KangarooTwelve (KT128) example (schematic)”.
- Inside the card:
• Inputs:
– “M = ptn(n₂), chosen so that |S| > 8192 bytes (forces tree mode)”
– “C = ‘Example customization’”
– “L = L₂ bytes”
• Encoded string:
– Small bar: “S = M ∥ C ∥ length_encode(|C|)”
• Function:
– “Z = KT128(M, C, L₂)”
• Output:
– Output bar labeled:
“Z[0..L₂−1] = 0x… (see RFC 9861 test vector)”
• Side annotations:
– “Exercises tree hashing (S split into S₀,…,Sₙ₋₁).”
– “Exercises non-empty customization C.”
- Between the two cards, add a small note:
“Exact hex values are defined in RFC 9861; implementations must match them bit-for-bit to be considered conformant.”
(C) INTEROPERABILITY REGISTRIES (IANA / COSE)
- Region title: “(C) Interoperability: IANA & COSE Registrations”.
- Draw a small table-like or mapping diagram that connects RFC 9861 functions to registry identifiers.
1) IANA hash/alg registrations:
- Box labeled “IANA Registries”.
- Inside, 3–4 rows such as (schematic, not necessarily exact names):
• “TurboSHAKE128 → IANA identifier ‘TURBOSHAKE128’”
• “TurboSHAKE256 → IANA identifier ‘TURBOSHAKE256’”
• “KangarooTwelve KT128 → IANA identifier ‘K12-128’ (schematic label)”
• “KangarooTwelve KT256 → IANA identifier ‘K12-256’ (schematic label)”
- Note:
“IANA entries allow use in generic hash/XOF registries, protocol negotiation, and algorithm agility.”
2) COSE algorithm identifiers:
- Box labeled “COSE Algorithms”.
- Show a small mapping:
• “COSE alg X ↦ TurboSHAKE128”
• “COSE alg Y ↦ TurboSHAKE256”
• “COSE alg Z ↦ KangarooTwelve (KT128/KT256 profiles)”
- Add a short annotation:
“COSE alg IDs bind RFC 9861 algorithms into JOSE/COSE-based ecosystems.”
3) Protocol ecosystem:
- On the far right, show small generic icons for “Protocol A”, “Protocol B”, “App”, with arrows to the IANA/COSE boxes.
- Label:
“Protocols reference RFC 9861 XOFs via registry identifiers, not ad-hoc names.”
- Under this region, add a concise textual summary:
“Registries ensure that all implementations refer to the same concrete function, test against the same vectors, and maintain interoperability across libraries and platforms.”
Legend and bottom strip:
- Tiny legend (if needed) explaining:
• Color for “test strategy / coverage”.
• Color for “example vector cards”.
• Color for “registry / protocol integration”.
- Bottom distilled insight (1 sentence), for example:
“RFC 9861 couples a structured test-vector strategy with IANA and COSE registrations so that TurboSHAKE and KangarooTwelve implementations can be validated bit-for-bit and deployed interoperably in protocol ecosystems.”
---
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
- Partition the canvas into 2–4 clearly separated regions with explicit headings, e.g.:
• “(A) Conceptual Model”
• “(B) Algorithmic Flow”
• “(C) Complexity / Trade-offs”
• “(D) Empirical Behavior”
- Each region should contain one core construct:
• A single graph, a single flow diagram, or a single layered architecture.
• 3–8 labeled elements maximum, each with precise short labels.
- Use clearly directional story structure:
• Left→right for narrative progression or pipeline stages.
• Top→bottom for abstraction levels (theory at top, implementation at bottom).
• Center→periphery for ecosystems or multi-agent interactions.
- Maintain adequate whitespace between regions; do not crowd symbols.
- Include a compact legend when multiple colors or line styles are used.
Axes, notation, and labels:
- When showing plots or planes, always:
• Label both axes with quantity and (if relevant) units.
• Use tick marks and 2–5 reference values.
• Provide a legend for multiple lines/series/classes.
- Use research-style notation where useful:
• E[x], Var(x), p(x), fθ(x), O(n²), O(n log n).
• Mark regimes with labels such as “high-signal”, “low-data”, “asymptotic region”.
- For models, explicitly label:
• Inputs, outputs, parameters, and latent variables.
• Deterministic vs stochastic paths (e.g., solid vs dashed lines).
Context focus (deep research):
- Suitable for:
• Formal protocol diagrams (message flows, rounds, adversary model).
• ML training/evaluation pipelines, including data preprocessing, model, metrics.
• Cryptographic constructions with setup, keygen, sign/verify, encrypt/decrypt flows.
• Distributed algorithms with nodes, links, and failure/partition regions.
• Experimental setups: environment, control variables, measured outputs.
- Always make explicit:
• Where the assumptions enter (e.g., “IID”, “synchronous network”, “honest majority”).
• Where the main complexity/cost is incurred (compute, memory, communication).
• Where the main risks/failure modes lie (bottlenecks, attack surfaces, instability).
Advanced composition patterns:
- Hybrid diagrams:
• Combine one conceptual diagram (high-level) with one precise flow or graph (low-level).
• Connect them with subtle arrows or reference markers (A1, B2, etc.).
- Multi-scale views:
• Top: coarse-grained overview (modules, agents, layers).
• Bottom: fine-grained detail (timeline, state transitions, micro-steps).
- Comparative views:
• Side-by-side algorithms/models with identical axes and metrics for direct comparison.
• Highlight differences using color, line style, or annotation.
Reading orientation & storytelling:
- Ensure the diagram can be “read” logically:
• Number key steps (1–N) if depicting an algorithm.
• Use (A), (B), (C) tags for regions and refer to them in labels.
• Group related elements with subtle background shapes or subtle bounding boxes.
- Avoid decorative elements that do not support the technical story.
Bottom strip:
- At the bottom, add a narrow strip with a 1-sentence distilled insight, e.g.:
“The algorithm refines the state through three constrained projections, achieving a Pareto-optimal trade-off between error and compute.”
- This sentence should summarize what an expert should remember after seeing the figure once.
NOW INSTANTIATE THIS STYLE FOR SLIDE 12:
“DESIGN TRADE-OFFS & SUMMARY”
Goal:
- Draw a single, research-grade summary figure that:
• Makes the main design trade-offs of RFC 9861 explicit: performance vs security margin, simplicity vs structural richness, and implementation complexity vs functionality.
• Contrasts the benefits and costs of adopting TurboSHAKE, KangarooTwelve, and HopMAC compared to legacy SHA-2/SHA-3/SHAKE.
• Provides a final, high-level synthesis of the family: when to use TurboSHAKE, when to use K12, and when to deploy HopMAC.
- The figure should read as an “executive technical summary”: dense but visually structured, suitable as a closing slide.
Overall layout:
- Partition the canvas into three regions:
(A) Trade-off Quadrant (left)
(B) Pros / Cons Matrix (center)
(C) Final Family Summary Strip (right)
- Maintain full visual consistency with previous slides in palette, font, and iconography.
(A) TRADE-OFF QUADRANT — PERFORMANCE VS STRUCTURAL COMPLEXITY
- Region title: “(A) Design Trade-offs in the Keccak XOF Space”.
- Draw a 2D quadrant diagram:
• X-axis: “Performance / Throughput” (left = lower, right = higher).
• Y-axis: “Structural Richness & Flexibility” (bottom = simpler, top = more features: XOF, tree, domain separation).
- Place four main reference points from the broader family:
1) “SHA-2 (SHA-256 / SHA-512)”
- Lower-right-ish but with low “structural richness”.
- Annotation:
“Fixed-length; Merkle–Damgård; length-extension issue; no native tree mode.”
2) “SHA-3 / SHAKE”
- Slightly higher on richness (sponge, XOF) and moderate performance.
- Annotation:
“Sponge; XOF (SHAKE); 24 rounds; strong conservative margin.”
3) “TurboSHAKE (128/256)”
- Further right along performance axis due to 12-round permutation; similar or slightly higher richness than SHAKE thanks to explicit D-byte.
- Annotation:
“Round-reduced Keccak-p[1600, 12]; high-speed XOF; explicit domain byte D.”
4) “KangarooTwelve (KT128/KT256)”
- High performance and high structural richness (tree hashing, parallelism).
- Annotation:
“Tree XOF over TurboSHAKE; built-in parallelism and long-message optimization.”
- Optionally, shade a region in the upper-right labeled:
“RFC 9861 design target: fast, flexible, parallel Keccak-based XOFs for modern protocols.”
(B) PROS / CONS MATRIX — BENEFITS VS COSTS
- Region title: “(B) Benefits and Costs of RFC 9861 Choices”.
- Draw a two-column table or box layout with three rows, grouping pros and cons:
Left column: “Benefits”
Right column: “Costs / Risks”
Row 1 — Performance & Functionality:
- Benefits:
• “Higher throughput vs SHAKE due to 12-round Keccak-p[1600].”
• “XOF everywhere; no need to juggle multiple fixed-length outputs.”
• “Tree hashing via K12 for long messages and parallel processing.”
- Costs:
• “Reduced cryptanalytic margin compared to full-round Keccak-f[1600].”
• “Tree machinery is conceptually more complex than flat hashing.”
Row 2 — Protocol Design & Domain Separation:
- Benefits:
• “Built-in domain separation via D-byte and customization string C.”
• “Small, coherent family makes it easier to reason about KDF, MAC, and hash roles.”
• “HopMAC gives a structured MAC directly on K12, reducing design space for ad-hoc constructions.”
- Costs:
• “Protocols must actually use distinct D/C values per role to avoid cross-protocol issues.”
• “New algorithms require integration into existing standards and code bases; adoption takes time.”
Row 3 — Implementation & Side Channels:
- Benefits:
• “Keccak structure is generally friendlier to masking and SCA protections than SHA-2.”
• “HopMAC’s keyless inner call shrinks the surface that needs heavy SCA hardening.”
• “Single underlying permutation can unify implementation effort across hash, XOF, MAC, KDF.”
- Costs:
• “Keyed uses still require constant-time, masked implementations.”
• “Round-reduced security relies on ongoing cryptanalysis; risk appetite must be explicit.”
• “Implementation complexity increases if libraries support both legacy and RFC 9861 families.”
(C) FINAL FAMILY SUMMARY STRIP — “WHAT TO USE WHEN”
- Region title: “(C) Family Summary: TurboSHAKE, K12, HopMAC”.
- Draw three horizontally arranged “summary cards” or blocks:
Card 1 — TurboSHAKE:
- Title: “TurboSHAKE128 / TurboSHAKE256”.
- Bullet-like labels:
• “Flat, high-speed XOFs (Keccak-p[1600, 12]).”
• “Use as default XOF / hash primitive in new designs.”
• “Good for KDFs and MAC cores with explicit domain separation.”
• “Pick 128 vs 256 bits based on threat model and key size.”
Card 2 — KangarooTwelve:
- Title: “KangarooTwelve (KT128 / KT256)”.
- Bullet-like labels:
• “Tree XOFs on TurboSHAKE; optimized for long messages and parallel hardware.”
• “Use where you need very fast hashing of large data (logs, files, transcripts).”
• “Same security levels as TurboSHAKE variants; same ecosystem (XOF + D/C).”
Card 3 — HopMAC:
- Title: “HopMAC”.
- Bullet-like labels:
• “MAC construction built directly on K12; inner call keyless, outer call keyed.”
• “Minimizes SCA-sensitive code footprint.”
• “Use when you want a structured MAC with clear reduction to K12/TurboSHAKE security, instead of ad-hoc XOF-based MACs.”
- Under the three cards, add a short “decision line”:
• Example: “Need a fast XOF? → TurboSHAKE. Hashing huge messages? → K12. Need a MAC on this family? → HopMAC.”
Legend and bottom strip:
- If needed, add a tiny legend explaining:
• Shape/colors for legacy vs FIPS 202 vs RFC 9861 family nodes in the quadrant.
- Bottom distilled insight sentence, for example:
“RFC 9861 trades some Keccak round margin for a compact family of fast, domain-separated XOFs and a MAC that together offer a pragmatic, protocol-friendly evolution of the SHA-3 ecosystem.”