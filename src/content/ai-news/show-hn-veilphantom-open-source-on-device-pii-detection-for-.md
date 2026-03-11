---
title: 'Show HN: VeilPhantom – Open-source on-device PII detection for AI pipelines'
description: 'I built VeilPhantom, a Python SDK that detects and tokenizes PII before text reaches any LLM.The problem: AI agents processing meetings, emails, support tickets are handling raw sensitive data. Names,'
pubDate: 2026-03-10T18:12:48
source: 'Hacker News'
sourceUrl: 'https://helloveil.com/sdk/'
tags: []
---

I built VeilPhantom, a Python SDK that detects and tokenizes PII before text reaches any LLM.The problem: AI agents processing meetings, emails, support tickets are handling raw sensitive data. Names, salaries, medical details — all flowing through cloud APIs.The solution: Detect PII on-device, replace with tokens ([PERSON_1], [AMOUNT_1]), send safe tokens to LLM, rehydrate response locally.Interesting finding: In benchmarks (98 scenarios, 8 verticals, Claude Haiku), accuracy went UP with PII redaction — 91.5% → 93.3%. Token-structured input seems to help models parse arguments more reliably.Technical details: - Shade V7: 22M param PhoneticDeBERTa (DeBERTa-v3-xsmall + Double Metaphone embeddings) - Trained on 72M words of meeting/business data - 7 detection layers (NER, gazetteers, regex, NLP, contextual) - 19 PII token types - 6ms average overhead - 97.1% F1 on meeting transcriptsThe phonetic embeddings help catch ASR-mangled names across cultures — "Nkosinathi" transcribed as "Ink Casino Thea" still gets detected.pip install veil-phantomDocs + benchmarks: https://helloveil.com/sdk GitHub: https://github.com/helloveil/veil-phantomApache 2.0. Happy to answer questions about the architecture or training approach. Comments URL: https://news.ycombinator.com/item?id=47326850 Points: 1 # Comments: 0
