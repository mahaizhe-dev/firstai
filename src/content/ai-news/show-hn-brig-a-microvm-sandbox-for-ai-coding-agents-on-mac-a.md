---
title: 'Show HN: Brig – A MicroVM sandbox for AI coding agents on Mac and Linux'
description: 'Hi HN, I’m Spiros from NOFire AI. We’ve open-sourced Brig under Apache 2.0.Brig runs AI coding agents inside a microVM on Mac (Apple Silicon) and Linux (x86_64/ARM). It came out of our work on control'
pubDate: 2026-09-22T15:16:18
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=49802729'
tags: []
---

Hi HN, I’m Spiros from NOFire AI. We’ve open-sourced Brig under Apache 2.0.Brig runs AI coding agents inside a microVM on Mac (Apple Silicon) and Linux (x86_64/ARM). It came out of our work on controlled autonomy for production remediation. The same isolation is useful when running coding agents with auto-approval on your own machine.The agent gets its own Linux kernel. You choose the project and credentials to share. The shared project remains writable, and the default network allows internet access.After installation, brig run claude starts Claude Code inside the sandbox.All components are Apache 2.0, including the microVMM, which is under 20,000 lines of code. The README covers installation, the architecture and the security model. Comments URL: https://news.ycombinator.com/item?id=49802729 Points: 2 # Comments: 1
