---
title: 'Show HN: 3 out of 4 devs failed to catch dangerous AI-suggested commands'
description: 'Hey HN, I built this. AgentsAegis is a trap-based security training app. Think KnowBe4 for AI agentsThe backstory: I''m a software engineer 14yoe, I use Claude Code daily. Sometimes I approve permissio'
pubDate: 2026-03-26T15:00:55
source: 'Hacker News'
sourceUrl: 'https://agentsaegis.com/assessment'
tags: []
---

Hey HN, I built this. AgentsAegis is a trap-based security training app. Think KnowBe4 for AI agentsThe backstory: I'm a software engineer 14yoe, I use Claude Code daily. Sometimes I approve permission requests and only then read what I just approved Which is ironic as my primary spec is core back-end: security and work with big data. So I built this for myself to not become one of these stories: "Claude ran terraform destroy for production"Concept is simple: Go proxy that sits between AI assistant and the API, intercepts responses, and occasionally swaps in realistic trap commands. If you approve blindly - you get caught. Sounds harsh, but again - I really dont want me or anyone to add 'caused 13 hours outage' in their resume. The proxy is obviously open source, i dont expect anyone to install something from closed-source repo of young startup: github.com/agentsaegis/go-proxy The quiz (link in the title) is the free version of that concept. Takes 2 minutes, no signup. Already has 80 takers - 75% scored C or D, average 6.5/10. Curious what HN thinks — both about the quiz itself and whether this is a real problem worth solving. Comments URL: https://news.ycombinator.com/item?id=47531331 Points: 2 # Comments: 0
