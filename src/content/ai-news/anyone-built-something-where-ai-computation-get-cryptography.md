---
title: 'Anyone built something where AI computation get cryptography receipts'
description: 'We''re a small proof-of-useful-work project. The validators don''t mine — they verify AI computations (matrix multiplications + activation functions) and get consensus weight for it.The part that matter'
pubDate: 2026-10-14T15:30:42
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=50089213'
tags: []
---

We're a small proof-of-useful-work project. The validators don't mine — they verify AI computations (matrix multiplications + activation functions) and get consensus weight for it.The part that matters to you: submit any GEMM workload up to 256×256 and we return the result plus a cryptographic receipt — a SHA-256 commitment chain folded into our ledger state, verifiable by anyone forever. Free, no token, no signup beyond an API key we generate in seconds.Honest limits: we verify GEMM + elementwise activations (GELU/sigmoid/ tanh/exp), not full transformer graphs yet. Attention is on the roadmap. The verification cost curve is published (615ms at 64³ → 157s at 1024³) — we priced our own clamp and labeled every tier.The logs: [pouw-verify] CONFIRMED lines, epoch crossings, claim-decrees folded into the ledger — every claim has a receipt.Live dashboard: http://3.237.91.235:32233 The evidence ledger (250+ owned defects, 250+ laws): github.com/sarinsk629-blip/hsma-core Comments URL: https://news.ycombinator.com/item?id=50089213 Points: 1 # Comments: 0
