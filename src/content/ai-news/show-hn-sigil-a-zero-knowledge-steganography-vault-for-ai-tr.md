---
title: 'Show HN: Sigil – A zero-knowledge steganography vault for AI training data'
description: 'Hi HN,I’ve been experimenting with ways to protect digital assets from automated AI web scrapers. I built Sigil, a local-first desktop application that embeds cryptographically signed ownership IDs in'
pubDate: 2026-03-28T03:17:08
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47551236'
tags: []
---

Hi HN,I’ve been experimenting with ways to protect digital assets from automated AI web scrapers. I built Sigil, a local-first desktop application that embeds cryptographically signed ownership IDs into the LSB (Least Significant Bit) layer of images.The desktop vault itself (Svelte/Tauri/SQLite) is closed-source to protect the HMAC-SHA256 signing architecture, but I have open-sourced the Rust extraction standard today.The idea is to create an open protocol where AI data procurement teams can run the extractor against their scraped datasets. If it detects a payload, they know the asset is cryptographically locked and requires a license.The extractor logic relies entirely on image and hex crates for memory-safe pixel parsing. I'd love any feedback on the extraction architecture or the LSB approach.Extractor Repo: https://github.com/nishal21/Sigil-extractor Landing Page (Astro): https://nishal21.github.io/Sigil-extractor/ Comments URL: https://news.ycombinator.com/item?id=47551236 Points: 1 # Comments: 0
