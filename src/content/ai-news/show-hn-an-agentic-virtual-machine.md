---
title: 'Show HN: An Agentic Virtual Machine'
description: 'I''m interested in feedback pertaining to the features in my agentic harness project.* Addressable MemoryEverything in the context is divided into receipts with internal urls that the model can address'
pubDate: 2026-10-11T08:27:40
source: 'Hacker News'
sourceUrl: 'https://github.com/plurnk/plurnk'
tags: []
---

I'm interested in feedback pertaining to the features in my agentic harness project.* Addressable MemoryEverything in the context is divided into receipts with internal urls that the model can address, with a "pulled preview" approach where dozens of spammy tools can be streaming output at the same time without flooding the attention window.* Perpetual ContextPlurnk has no compaction algorithm because the addressable memory empowers the model to curate its context on its own terms. This has an incredible impact over extended sessions, with the agent retaining its bearings for weeks on end.* Model-Oriented Programming LanguagePlurnk presents the model with a "virtual machine" that it "programs," with all core and extended tools having a common markdown-adjacent shape.* First-Party BenchmarksThe architecture is basically sqlite+node, with the only dependency weight being ANTLR for building the programming language AST and the giant bag of wasm treesitters necessary for all of the integrated pattern dialect functionality (glob, regex, jsonpath, xpath, graph, fts).My latest benchmark, published on the separate bench repo, is comparable with bare pi agent, despite all of these bells and whistles.Looking for honest, including brutally honest, feedback. All MIT. No telemetry. Works on everything node can be installed on (tested on mac, android, arm64, etc). Comments URL: https://news.ycombinator.com/item?id=50040855 Points: 1 # Comments: 0
