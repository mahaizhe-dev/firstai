---
title: 'Show HN: Ocarina – Automate and test MCP servers from YAML, no LLM'
description: 'Hi all. As someone who has spent years working with Ansible and other automation frameworks, the recent MCP boom has me fascinated. People are creating nice, typed, LLM-readable (and thus human-readab'
pubDate: 2026-06-27T15:33:22
source: 'Hacker News'
sourceUrl: 'https://github.com/msradam/ocarina'
tags: []
---

Hi all. As someone who has spent years working with Ansible and other automation frameworks, the recent MCP boom has me fascinated. People are creating nice, typed, LLM-readable (and thus human-readable) interfaces for their servers, over a standardized protocol that exposes both tools and resources. I wanted to see if I could create a way to run scripts against these servers directly, with no AI in the loop.Ocarina lets you inspect MCP server characteristics and write Rondos (the equivalent of Ansible playbooks) that express tool calls in yaml so you can play them step-by-step without needing to drive with an LLM.Here's what a Rondo looks like: keys: owner: acme repo: api server: command: npx args: [-y, "@modelcontextprotocol/server-github"] rondo: - name: recent commits tool: list_commits args: owner: "{{owner}}" repo: "{{repo}}" grab: ".0.sha" echo: latest_sha - name: commit detail tool: get_commit args: owner: "{{owner}}" repo: "{{repo}}" sha: "{{latest_sha}}" expect: contains: "feat" I have started using Ocarina myself to test and validate the MCP servers I am creating at my job, and I am interested in the broader field of how we can maximize the use of the massive MCP ecosystem. The README includes links to repos you can clone and try right away (and a little Blender demo ;])Happy Saturday! Comments URL: https://news.ycombinator.com/item?id=48699141 Points: 2 # Comments: 0
