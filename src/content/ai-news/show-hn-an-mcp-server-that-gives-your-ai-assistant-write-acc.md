---
title: 'Show HN: An MCP server that gives your AI assistant write access to /etc./hosts'
description: 'I was tired of how bad distraction blockers are so I built my own.LockIn lets AI assistants (Claude, ChatGPT, Cursor, etc.) block websites by editing the system hosts file directly via MCP tools (via '
pubDate: 2026-07-04T10:09:17
source: 'Hacker News'
sourceUrl: 'https://www.lockinmcp.com'
tags: []
---

I was tired of how bad distraction blockers are so I built my own.LockIn lets AI assistants (Claude, ChatGPT, Cursor, etc.) block websites by editing the system hosts file directly via MCP tools (via a secure cloudflare bridge).Why? Because chrome extensions don't work. Blocking it natively makes it unbypassable, and having your agent gatekeep your focus is the ultimate cheat code.Since everyone is using AI agents nowadays, but most people start scrolling or Reddit while waiting for Claude Code to finish, giving them control over your focus solves that.The MCP server exposes four tools: block_site, unblock_temp, focus_session, get_status. A background daemon keeps the state synced and persists across restarts. There's a relay URL for hosted MCP connections (ChatGPT, Copilot).Install: npx -y lockin-mcp installWhat makes it so good for me is the timed unblock: it gives the flexibility most tools miss. If you're studying for school you don't want to be distracted by yt, but perhaps you have to watch a 5 minute video FOR school, in that case you can now ask your agent to 'unblock yt for 5 minutes' and it does it.Happy to get into the daemon architecture or the relay setup if anyone's curious. Comments URL: https://news.ycombinator.com/item?id=48784250 Points: 2 # Comments: 1
