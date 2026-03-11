---
title: 'Show HN: AgentSign – Open-source zero trust engine for AI agents'
description: 'Hi HN. This week Meta acquired Moltbook (agent social network), OpenAI acquired Promptfoo (agent testing), and Mandiant''s founder raised $190M for Armadin. Agent infrastructure is clearly where things'
pubDate: 2026-03-11T13:57:42
source: 'Hacker News'
sourceUrl: 'https://github.com/razashariff/agentsign'
tags: []
---

Hi HN. This week Meta acquired Moltbook (agent social network), OpenAI acquired Promptfoo (agent testing), and Mandiant's founder raised $190M for Armadin. Agent infrastructure is clearly where things are heading.We built AgentSign -- a zero trust engine for AI agents. The problem: agents are operating without any identity infrastructure. Moltbook went viral for fake posts because there was zero verification on who or what was posting.AgentSign gives every agent a cryptographic identity certificate, signs every action into an execution chain, and runs runtime code attestation before anything executes. There's also an MCP Trust Layer for agent-to-MCP server verification, and a Stripe-powered Trust Gate for agent payments.5 subsystems: identity certs, execution chain verification, runtime code attestation, output tamper detection, and cryptographic trust scoring.Free and open source. Built in London.SDK: https://github.com/razashariff/agentsign-sdkHappy to answer questions. Comments URL: https://news.ycombinator.com/item?id=47335647 Points: 2 # Comments: 0
