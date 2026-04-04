---
title: 'Show HN: MicroSafe-RL – Deterministic 1.18µs safety layer for Edge AI'
description: 'I built MicroSafe-RL to solve the "hardware destruction" problem during Reinforcement Learning and Edge LLM deployment.The Tech: It’s a bare-metal C++ interceptor using an EMA+MAD stability metric der'
pubDate: 2026-04-04T02:51:38
source: 'Hacker News'
sourceUrl: 'https://github.com/Kretski/MicroSafe-RL'
tags: []
---

I built MicroSafe-RL to solve the "hardware destruction" problem during Reinforcement Learning and Edge LLM deployment.The Tech: It’s a bare-metal C++ interceptor using an EMA+MAD stability metric derived from Control Lyapunov Functions. Performance: 1.18 microseconds worst-case execution time (WCET). No heap, no dynamic allocation, just 24 bytes of state. The "Bridge": The latest update includes a Python-C++ bridge to use local LLMs (like Gemma 4 via Ollama) as robotic controllers while keeping them physically safe.Currently under review at IEEE Transactions on Aerospace and Electronic Systems.GitHub: https://github.com/Kretski/MicroSafe-RL Comments URL: https://news.ycombinator.com/item?id=47635181 Points: 1 # Comments: 0
