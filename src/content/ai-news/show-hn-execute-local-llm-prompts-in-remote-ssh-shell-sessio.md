---
title: 'Show HN: Execute local LLM prompts in remote SSH shell sessions'
description: 'Hi HN,This is a tool I''ve worked on the past few months.Instead of giving LLM tools SSH access or installing them on a server, the following command: $ promptctl ssh user@server makes a set of locally'
pubDate: 2026-03-13T18:22:08
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47367795'
tags: []
---

Hi HN,This is a tool I've worked on the past few months.Instead of giving LLM tools SSH access or installing them on a server, the following command: $ promptctl ssh user@server makes a set of locally defined prompts "magically" appear within the remote shell as executable command line programs.For example, I have locally defined prompts for `llm-analyze-config` and `askai`. Then on (any) remote host I can: $ promptctl ssh user@host # Now on remote host $ llm-analyze-config /etc/nginx.conf $ cat docker-compose.yml | askai "add a load balancer" the prompts behind `llm-analyze-config` and `askai` execute on my local computer (even though they're invoked remotely) via the llm of my choosing.This way LLM tools are never granted SSH access to the server, and nothing needs to be installed to the server. In fact, the server does not even need outbound internet connections to be enabled.Eager to get feedback!Github: https://github.com/tgalal/promptcmd/ Comments URL: https://news.ycombinator.com/item?id=47367795 Points: 3 # Comments: 2
