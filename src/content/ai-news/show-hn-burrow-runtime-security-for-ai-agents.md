---
title: 'Show HN: Burrow – Runtime Security for AI Agents'
description: 'We use Claude Code, Cursor, and Copilot daily. These tools run shell commands, read files, and call APIs on their own. When something goes wrong you find out after.A .env file gets read, a secret ends'
pubDate: 2026-04-14T06:25:47
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47761957'
tags: []
---

We use Claude Code, Cursor, and Copilot daily. These tools run shell commands, read files, and call APIs on their own. When something goes wrong you find out after.A .env file gets read, a secret ends up somewhere it should not, a command runs that nobody approved. EDR sees process spawns. Cloud audit logs see API calls. Neither understands that the agent's chain of actions together is credential theft.Burrow sits between the agent and the machine. You define policies in plain language, like "block any agent from deleting production resources" or "alert if an agent reads AWS credentials and then sends data to an external endpoint." Burrow maps those policies against the actual tools, MCP servers, and plugins in your environment, then intercepts tool calls at the framework level before they execute. Risky calls get dropped. Everything else passes through.Works with Claude Code, Cursor, Copilot, Windsurf, CrewAI, LangChain, LangGraph, and a few more. CLI and SDK install in under a minute. Free tier for individuals, paid for teams.I ran infrastructure security at a large media company before this. Going full time on Burrow later this month. Happy to answer anything, especially the "does this actually work in production" question.try - https://burrow.run Comments URL: https://news.ycombinator.com/item?id=47761957 Points: 2 # Comments: 0
