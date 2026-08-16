---
title: 'Ask HN: What tools are you using for human code review of AI-assisted code?'
description: 'A good proportion of us and our colleagues are now churning out agent-assisted code at an incredible rate, with some of it that is actually good, and a lot that is not so good. I''m personally finding '
pubDate: 2026-08-16T16:20:45
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=49321400'
tags: []
---

A good proportion of us and our colleagues are now churning out agent-assisted code at an incredible rate, with some of it that is actually good, and a lot that is not so good. I'm personally finding that the real quality gate for our projects is now how thoroughly the generated code was human reviewed to ensure that it is not just correct, but architecturally sensible.AI code review tools like coderabbit and copilot, or even pointing claude code at a PR are all generally pretty good at finding bugs and style nits, but less good at finding duplicate code, module cross coupling, bad separation of concerns, and so on, even if prompted to do so.I'm finding that github's PR interface is not really cutting it for me, it was janky even when the reviews were small, but now at the size they're at, it is becoming unmanageable. Add to that the extra noise of mixing in agent reviews, and people "meat-proxying" in copy-pasted agent output, and it's getting pretty noisy and difficult to navigate.What have you all found that works well for streamlining human review of AI assisted code? Tools and process suggestions are welcome. Comments URL: https://news.ycombinator.com/item?id=49321400 Points: 1 # Comments: 0
