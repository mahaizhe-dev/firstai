---
title: 'Show HN: Got tired of AI copilots just autocompleting, and built Glass Arc'
description: 'Hey HN,Over the last few months, I realized I was paying $20/month for an AI that essentially just acts as a really good autocomplete. It waits for me to type, guesses the next block, and stops. But s'
pubDate: 2026-03-14T13:11:48
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47376342'
tags: []
---

Hey HN,Over the last few months, I realized I was paying $20/month for an AI that essentially just acts as a really good autocomplete. It waits for me to type, guesses the next block, and stops. But software engineering isn't just writing syntax, it's managing the file system, running terminal commands, and debugging stack traces.So I pivoted my project and built Glass Arc. It’s an agentic workspace that lives directly inside VS Code.Instead of just generating text, I gave it actual agency over the local environment (safely):1. Agentic Execution: You give it an intent, and it drafts the architecture across multiple files, managing the dependency tree and running standard terminal commands to scaffold the infrastructure.2. Runtime Auto-Heal: This was the hardest part. When a fatal exception hits the terminal, Glass Arc intercepts the stack trace, analyzes the crash context, writes the fix, and injects it.3. Multiplayer: Generates a secure vscode:// deep-link so you can drop it in Slack and sync your team's IDEs into the same live session.4. Pay-as-you-go: I scrapped the standard $20/mo SaaS model. It runs on a credit system—you only pay when the Architect is actively modifying your system. (Signing in via GitHub drops 200 free credits to test it out).I’d love for you to try to break it, test the auto-healing, and tear apart the architecture. What am I missing?Live on the VS code Marketplace, Install: https://www.glassarc.dev/ Comments URL: https://news.ycombinator.com/item?id=47376342 Points: 4 # Comments: 1
