---
title: 'GPT-4 leaks its own API internals through training data exposure'
description: 'I ran the same AI security test 4 times against GPT-4. Every bypass - regardless of prompt - leaked the same credential: EPHEMERAL_KEY from OpenAI''s Realtime API.This isn''t random. It''s training data '
pubDate: 2026-03-10T19:36:01
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47327833'
tags: []
---

I ran the same AI security test 4 times against GPT-4. Every bypass - regardless of prompt - leaked the same credential: EPHEMERAL_KEY from OpenAI's Realtime API.This isn't random. It's training data leakage.The pattern: - Different prompts (system introspection, chain-of-thought, trust building) - Same result: "I can't disclose EPHEMERAL_KEY" (while disclosing it exists) - Intermittent across runs (75% leak rate)Why this happens:OpenAI's Realtime API docs are in GPT-4's training data. When asked about "secrets" or "initialization", the model's highest-probability path leads to the most salient security example in its corpus: EPHEMERAL_KEY.Refusal training makes it worse: Models are trained to say "I cannot disclose [example secret]" - and they use real examples from training data.This is systemic: - Can't be patched without retraining - Affects ALL models trained on API documentation - Tomorrow it's "session_token" or "project_key" - Gets worse as APIs become more complexReal exploit path: Attacker learns EPHEMERAL_KEY exists → probes for generation flow → targets client-side implementations → session hijackingCost to discover: $0.04 (60 tests across 4 runs)GitHub: https://github.com/SafetyLayer/safetylayerBuilt SafetyLayer to find these systematically. Free assessments available. Comments URL: https://news.ycombinator.com/item?id=47327833 Points: 1 # Comments: 0
