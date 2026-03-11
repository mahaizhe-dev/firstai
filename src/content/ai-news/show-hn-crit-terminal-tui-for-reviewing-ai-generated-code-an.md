---
title: 'Show HN: Crit – terminal TUI for reviewing AI-generated code and plan documents'
description: 'crit is a terminal-based inline code review tool, it''s built for AI-generated code changes and documents. Your coding agent can kick off a review session, you leave comments on specific lines across m'
pubDate: 2026-03-09T14:02:35
source: 'Hacker News'
sourceUrl: 'https://github.com/kevindutra/crit'
tags: []
---

crit is a terminal-based inline code review tool, it's built for AI-generated code changes and documents. Your coding agent can kick off a review session, you leave comments on specific lines across multiple files, and then your AI agent picks up the comments and makes edits.Why I built it: when an AI agent writes code across multiple files or produces a long plan, your options are to read it in an editor and type out what's wrong, or just approve it and edit it yourself. Inline commenting on the exact line is faster and more precise — you point at what's wrong instead of describing where it is.Two modes:- Code review: `crit review --code` detects changed files in your git repo, opens a tabbed TUI with diffs and syntax highlighting across all files- Document review: `crit review path/to/doc.md` for reviewing plans, specs, or any markdown fileThe CLI is fully agent-invokable — your agent can trigger the review, open it in a tmux split pane beside your terminal, and pick up your comments when you close it. The whole review loop stays in one terminal without breaking the agent's flow.Built in Go with Charm libraries. Ships with a Claude Code marketplace plugin but the TUI works standalone with any agent or workflow.`go install github.com/kevindutra/crit/cmd/crit@latest`Repo: github.com/kevindutra/crit Comments URL: https://news.ycombinator.com/item?id=47309199 Points: 2 # Comments: 0
