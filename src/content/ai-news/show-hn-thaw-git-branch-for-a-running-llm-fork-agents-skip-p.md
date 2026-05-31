---
title: 'Show HN: Thaw – Git branch for a running LLM (fork agents, skip prefill)'
description: 'I built thaw because forking an LLM agent is absurdly wasteful today. When an agent explores N branches — RL rollouts, best-of-N, parallel coding attempts — each branch re-runs prefill over the same s'
pubDate: 2026-05-30T22:07:26
source: 'Hacker News'
sourceUrl: 'https://github.com/thaw-ai/thaw'
tags: []
---

I built thaw because forking an LLM agent is absurdly wasteful today. When an agent explores N branches — RL rollouts, best-of-N, parallel coding attempts — each branch re-runs prefill over the same shared context. You pay for the same prompt N times.thaw snapshots a live inference session — weights, KV cache, scheduler state, and the prefix-hash table — and hydrates N children that diverge from the fork point without re-prefilling. It's `git branch` for a running model.The receipt (H100 80GB, Llama-3.1-8B, real hardware): a pre-warmed pool boots once in 22.3s, then each fork round of 4 branches × 64 tokens runs in 0.88s median. Cold-boot equivalent would be ~340s/round — ~400× amortized. All rounds bit-identical at the fork boundary. Full JSON receipt + reproducer in the repo, nothing hand-waved.NVIDIA shipped Dynamo Snapshot last week for fast pod cold-starts — and they free the KV cache before checkpoint, by design. thaw is the opposite bet: preserve the KV cache so a fork is near-free. Different problem, opposite mechanic.pip install thaw-vllm. Works with vLLM and SGLang, Apache-2.0.https://github.com/thaw-ai/thawI'm a solo dev and this is the thing I most want feedback on: is the fork primitive the right shape, or do people want it wrapped in a framework(LangGraph/TRL) node instead? Happy to go deep on the KV-restore internals. Comments URL: https://news.ycombinator.com/item?id=48341069 Points: 2 # Comments: 0
