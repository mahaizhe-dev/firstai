---
title: 'Show HN: 100Hires MCP, 130 tools to run an ATS through LLM. Is 130 too many?'
description: 'Hi HN. I''m one of the co-founders of 100Hires ATS. We built an MCP server on top of our REST API.I would love HN to weigh in on whether 130 tools are too many. Big competitors have 30-40Some details:T'
pubDate: 2026-06-15T16:48:48
source: 'Hacker News'
sourceUrl: 'https://100hires.com/mcp'
tags: []
---

Hi HN. I'm one of the co-founders of 100Hires ATS. We built an MCP server on top of our REST API.I would love HN to weigh in on whether 130 tools are too many. Big competitors have 30-40Some details:Three layers, from the bottom up: - REST API v2: 87 endpoints, OpenAPI 3.0 spec, Bearer auth, public docs at 100hires.com/api - MCP server: 130 tools mapping roughly 1:1 to REST endpoints, hosted at mcp.100hires.com/mcp, ~400 LOC of wrapper code - ChatGPT plugin: thin wrapper on the MCP, OAuth handled by the plugin storeAuth on the MCP: OAuth 2.1 with PKCE and Dynamic Client Registration. Tokens scoped per user, 1-hour access tokens with auto-refresh, revoked when the user leaves the workspace. Tested in Claude Desktop, Claude Code, Cursor, VS Code, Codex, Windsurf, and Zed.Available on the free trial (but rate-limited) and on all paid plans. Comments URL: https://news.ycombinator.com/item?id=48543929 Points: 1 # Comments: 0
