---
title: 'Show HN: Clusterflock: An AI orchestrator for networked hardware'
description: 'Hi HN!We built Clusterflock to solve our own headaches with managing AI agents across distributed setups, different VRAM and RAM allowances, and the need to easily try out new models.While we focus on'
pubDate: 2026-04-04T11:43:53
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47638172'
tags: []
---

Hi HN!We built Clusterflock to solve our own headaches with managing AI agents across distributed setups, different VRAM and RAM allowances, and the need to easily try out new models.While we focus on infrastructure (we built this specifically for networked hardware) it does ship with a powerful mission runner (or orchestrator), which is multi-session and asynchronous.Here is what it does best:Hardware-aware auto-downloading: It profiles your networked hardware and automatically pulls down the best models for your specific setup (currently only from HuggingFace).Tight packing: Native parallelism via llama.cpp, you can allow it to fit multiple smaller models on same device.It is fully open-source. We wanted a painless way to deploy agentic clusters, and we hope you find it useful too.Website: https://clusterflock.netHappy to hear feedback. Flocks very much given. Comments URL: https://news.ycombinator.com/item?id=47638172 Points: 2 # Comments: 0
