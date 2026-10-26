---
title: 'MCP-warden local credential broker so AI agents never see your secrets'
description: 'I got tired of pasting GitHub PATs, Stripe keys and DB passwords into Claude Code / Cursor MCP configs. One prompt injection or a leaked chat and they’re gone. So I built mcp-warden — a local-first cr'
pubDate: 2026-10-26T09:57:32
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=50241410'
tags: []
---

I got tired of pasting GitHub PATs, Stripe keys and DB passwords into Claude Code / Cursor MCP configs. One prompt injection or a leaked chat and they’re gone. So I built mcp-warden — a local-first credential broker for the Model Context Protocol. How it works: • You store the secret once in the OS keychain • You define scoped presets (e.g. github-read, stripe-charges) • The agent calls high-level tools (proxy_http, ssh_exec, db_query) • mcp-warden injects the credential server-side and returns only the result The agent’s context never contains the secret. Allow-list validation runs before credential injection. Sensitive actions can require approval (desktop notification, TUI, or Telegram). Everything is logged locally. Works with Claude Code, Cursor, Codex, Cline and any other MCP client. Written in Rust, Apache-2.0, fully local.GitHub: https://github.com/ermoluk/mcp-wardenHappy to answer questions about the threat model or how people are currently handling secrets with agents. Comments URL: https://news.ycombinator.com/item?id=50241410 Points: 1 # Comments: 2
