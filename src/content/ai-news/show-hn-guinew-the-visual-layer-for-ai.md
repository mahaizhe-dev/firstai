---
title: 'Show HN: Gui.new – The Visual Layer for AI'
description: 'Hey HN, I built gui.new. You paste one line into ChatGPT or Claude, and from that point on, whenever you ask for something visual (a dashboard, chart, form, report) it renders it as a live shareable l'
pubDate: 2026-03-10T13:44:48
source: 'Hacker News'
sourceUrl: 'https://gui.new'
tags: []
---

Hey HN, I built gui.new. You paste one line into ChatGPT or Claude, and from that point on, whenever you ask for something visual (a dashboard, chart, form, report) it renders it as a live shareable link instead of dumping HTML in your chat.The prompt:"Read https://gui.new/docs/llms.txt - use gui.new to render any visual output as a shareable link. Apply this anytime you'd normally show a table, chart, dashboard, or UI mockup."That's the whole setup. Your AI reads the spec, starts using it, and every visual output becomes a clickable URL you can share with anyone.Every link gets real-time input sync (form fields, sliders, toggles work across all viewers), state persistence (survives after everyone leaves), and live updates via SSE. Links expire after 24 hours by default.I built it because AI is great at generating UIs but terrible at showing them. You ask for a dashboard and get a code block. gui.new closes that gap.Under the hood, your AI is making a single POST call to create a canvas:``` POST https://gui.new/api/canvas {"html": "Hello"}-> {"url": "https://gui.new/abc123"} ```You don't need to interact with the API yourself. But if you want to, there are SDKs (`npm install gui-new` / `pip install gui-new`) and the REST API is documented at gui.new/docs.Free, no signup. Try it at https://gui.newHappy to answer questions! Comments URL: https://news.ycombinator.com/item?id=47323168 Points: 5 # Comments: 5
