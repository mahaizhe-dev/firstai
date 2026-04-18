---
title: 'Show HN: PrivaKit – A zero-upload AI workspace in the browser via WebGPU'
description: 'Hi HN, I''m the builder. I realized that using cloud AI APIs for sensitive workflows—like transcribing board meetings, OCRing employment contracts, or cleaning up ID photos—is a massive privacy liabili'
pubDate: 2026-04-18T06:45:11
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47813683'
tags: []
---

Hi HN, I'm the builder. I realized that using cloud AI APIs for sensitive workflows—like transcribing board meetings, OCRing employment contracts, or cleaning up ID photos—is a massive privacy liability. So I built a client-side workspace using transformers.js, Whisper, and WebGPU. Everything runs locally. You can turn on Airplane Mode after the initial model load, and it still transcribes and extracts text perfectly. To keep myself honest, I wrote a technical audit of how the data flows (or rather, doesn't flow). My only backend is a tiny 2-core node in Singapore running self-hosted Plausible analytics: [https://gist.github.com/ygx2378/3275b333504c6a9def50ef531b54...] I'm still learning the ropes of browser-based memory management, so I'd love your feedback on how the models load on your specific GPUs! Comments URL: https://news.ycombinator.com/item?id=47813683 Points: 1 # Comments: 0
