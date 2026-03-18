---
title: 'Show HN: Clippy – screen-aware voice AI in the browser'
description: 'A friend and I built a browser prototype that answers questions about whatever’s on your screen using getDisplayMedia, client-side wake-word detection, and server-side multimodal inference.Hard parts:'
pubDate: 2026-03-18T18:50:40
source: 'Hacker News'
sourceUrl: 'https://RememberClippy.com'
tags: []
---

A friend and I built a browser prototype that answers questions about whatever’s on your screen using getDisplayMedia, client-side wake-word detection, and server-side multimodal inference.Hard parts:– Getting the model to point to specific UI elements– Keeping it coherent across multi-step workflows (“Help me create a sword in Tinkercad”)– Preventing the infinite mirror effect and confusion between window vs full-screen sharing– Keeping voice → screenshot → inference → voice latency low enough to feel conversationalWe packaged it as “Clippy” for fun, but the real experiment is letting a model tool-call fresh screenshots to help it gather more context.One practical use case is remote tech support — I'm sending this to my mom next time she calls instead of screen sharing.Curious what breaks. Comments URL: https://news.ycombinator.com/item?id=47429822 Points: 2 # Comments: 0
