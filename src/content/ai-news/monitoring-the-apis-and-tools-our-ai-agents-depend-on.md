---
title: 'Monitoring the APIs and tools our AI agents depend on'
description: 'Hi HN,One thing we''ve been noticing while building systems recently is how much modern applications depend on external APIs.Stripe / OpenAI / Anthropic / Twilio / Supabase / Resend / various 3P APIsMo'
pubDate: 2026-03-12T14:18:50
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47350879'
tags: []
---

Hi HN,One thing we've been noticing while building systems recently is how much modern applications depend on external APIs.Stripe / OpenAI / Anthropic / Twilio / Supabase / Resend / various 3P APIsMost teams have very good observability for infrastructure:servers / containers / databases / queuesBut much less visibility into the external systems their software depends on.The issue becomes even more visible with AI agents.Agents often rely on multiple APIs and tools to complete tasks. If one dependency slows down or starts failing, the agent behavior changes in ways that can be surprisingly hard to diagnose.We ran into this repeatedly while building production systems, so we started working on something to make that layer visible.DependWatch focuses specifically on monitoring external dependencies.It tracks things like:• latency across API providers • failure rates per endpoint • cost signals across APIs • alerts when dependencies degradeThe goal is simple: one place to see whether the APIs and tools your system relies on are healthy.We've been building it quietly for a while and are starting to open early access.Would love feedback from people running systems with lots of API dependencies or AI agent workflows.https://www.dependwatch.app/Curious how others here monitor external dependencies in their systems. Comments URL: https://news.ycombinator.com/item?id=47350879 Points: 1 # Comments: 0
