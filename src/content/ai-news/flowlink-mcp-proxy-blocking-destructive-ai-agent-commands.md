---
title: 'FlowLink: MCP proxy blocking destructive AI agent commands'
description: 'We built FlowLink because AI agents (Claude Code, Cursor, Copilot) keep executing destructive commands on production servers with no guardrails.The recent "AI agent deleted production database" post ('
pubDate: 2026-05-26T18:01:25
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48283348'
tags: []
---

We built FlowLink because AI agents (Claude Code, Cursor, Copilot) keep executing destructive commands on production servers with no guardrails.The recent "AI agent deleted production database" post (860 pts here) is exactly what this prevents.FlowLink is an MCP proxy between your AI agent and your tools. No code changes required. Point your agent config to FlowLink and it starts intercepting destructive commands.What it does:Shield Engine intercepts rm -rf, DROP TABLE, git push --force, chmod 777 and 100+ destructive patterns BEFORE execution.Policy Engine: per-agent, per-tool rules (e.g. "Claude can read but not delete").Zero-Trust Secrets: agents get scoped, time-limited tokens, never raw credentials.Telegram approval queue for human-in-the-loop on high-risk operations.Full audit trail of every agent action.Setup takes 2 minutes. Works with Claude Code, Cursor, Copilot, any MCP-compatible agent.Tech: Rust backend, MCP protocol native, E2EE, self-hosted.What guardrails are you currently using for AI agents? What's missing? Comments URL: https://news.ycombinator.com/item?id=48283348 Points: 1 # Comments: 0
