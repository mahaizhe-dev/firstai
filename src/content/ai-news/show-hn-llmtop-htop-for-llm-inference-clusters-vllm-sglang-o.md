---
title: 'Show HN: Llmtop – Htop for LLM Inference Clusters (vLLM, SGLang, Ollama, llama)'
description: 'I work on inference scheduling — KV cache-aware routing, load balancing across GPU workers, that kind of thing. I wanted something like k9s but for my inference stack. Nothing existed, so I built it.l'
pubDate: 2026-03-18T04:58:49
source: 'Hacker News'
sourceUrl: 'https://github.com/InfraWhisperer/llmtop'
tags: []
---

I work on inference scheduling — KV cache-aware routing, load balancing across GPU workers, that kind of thing. I wanted something like k9s but for my inference stack. Nothing existed, so I built it.llmtop is a real-time terminal dashboard for LLM inference workers. It scrapes the Prometheus /metrics endpoints that vLLM, SGLang, and LMCache already expose and shows everything in one view: KV cache usage, queue depth, TTFT/ITL latencies (P50/P99 from histogram buckets), token throughput, prefix cache hit rates. Color-coded — red means go fix it.``` brew install InfraWhisperer/tap/llmtop Or go install github.com/InfraWhisperer/llmtop/cmd/llmtop@latest. ```Single binary, no Prometheus server needed, no Grafana, no config. Just run llmtop and it auto-discovers local workers.Written in Go with Bubbletea. Working on Kubernetes pod auto-discovery and a GPU metrics view next. Comments URL: https://news.ycombinator.com/item?id=47421736 Points: 1 # Comments: 0
