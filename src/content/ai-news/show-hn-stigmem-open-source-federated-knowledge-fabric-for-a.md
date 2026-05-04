---
title: 'Show HN: Stigmem – open-source federated knowledge fabric for AI agents (v1.0)'
description: 'Hi HNI''m one of the authors of Stigmem. Stigmem is an open-source specification and reference node for a shared, federated knowledge substrate for AI agents. The core idea: instead of agents maintaini'
pubDate: 2026-05-03T22:52:44
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48002447'
tags: []
---

Hi HNI'm one of the authors of Stigmem. Stigmem is an open-source specification and reference node for a shared, federated knowledge substrate for AI agents. The core idea: instead of agents maintaining isolated memory stores, they write typed, provenance-tagged facts into a shared substrate that replicates across nodes via Ed25519-signed peer handshakes.A fact is a seven-tuple: (entity, relation, value, source, timestamp, confidence, scope). Facts are immutable, contradictions surface as first-class conflict records, not silent overwrites. Each fact carries a Hybrid Logical Clock timestamp so ordering is consistent across distributed nodes without a central coordinator.v1.0 is spec-complete (all 18 sections stable). The reference node is FastAPI + SQLite with 74 tests including automated failure-mode tests (split-brain, malicious peers, replay attacks). We ship an MCP adapter so any MCP-compatible agent runtime can read/write facts without touching the HTTP API.Two nodes federating with Docker: https://docs.stigmem.dev/docs/getting-started/quickstartRepo (Apache 2.0): https://github.com/Eidetic-Labs/stigmem Spec: https://github.com/Eidetic-Labs/stigmem/tree/main/spec Docs: https://docs.stigmem.dev Comments URL: https://news.ycombinator.com/item?id=48002447 Points: 2 # Comments: 0
