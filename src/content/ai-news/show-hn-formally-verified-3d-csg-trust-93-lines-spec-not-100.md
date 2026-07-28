---
title: 'Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code'
description: 'To my knowledge, this is the first formally verified implementation of a 3D constructive solid geometry (CSG) operation: mesh intersection, implemented in Lean 4 and verified against a concise specifi'
pubDate: 2026-07-28T13:07:14
source: 'Hacker News'
sourceUrl: 'https://github.com/schildep/verified-3d-mesh-intersection'
tags: []
---

To my knowledge, this is the first formally verified implementation of a 3D constructive solid geometry (CSG) operation: mesh intersection, implemented in Lean 4 and verified against a concise specification that pins down the surface of the resulting mesh exactly and guarantees practical well-formedness conditions on the triangulation.This project is also an experiment in avoiding having to trust AI-generated code. A human reviewer only needs to read 93 lines of formal specification and run the Lean checker to certify the correctness of the kernel, skipping the intricate 1000+ lines of AI-written implementation. To prove correctness, AI autonomously wrote over 60,000 lines of Lean proofs, which also never have to be inspected by a human. The Lean checker guarantees conformance to the specification at compile time, with zero trust placed in any LLM. This allows us to treat the implementation and proofs as a black box. I guided the agent through the milestones described in the readme to arrive at the result presented here.Also take a look at the web demo https://schildep.github.io/verified-3d-mesh-intersection/, which runs the verified mesh intersection kernel compiled to WebAssembly in your browser. Comments URL: https://news.ycombinator.com/item?id=49083239 Points: 5 # Comments: 1
