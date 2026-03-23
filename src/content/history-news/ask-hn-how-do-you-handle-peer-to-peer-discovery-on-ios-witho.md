---
title: 'Ask HN: How do you handle peer-to-peer discovery on iOS without a server?'
description: 'I''m building an app that syncs between phones over Bluetooth when there''s no cell service. Android has Nearby Connections API which handles discovery and transport nicely. iOS has Multipeer Connectivi'
pubDate: 2026-03-22T20:21:38
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47481736'
tags: []
---

I'm building an app that syncs between phones over Bluetooth when there's no cell service. Android has Nearby Connections API which handles discovery and transport nicely. iOS has Multipeer Connectivity but it's flaky and Apple hasn't updated it in years. CoreBluetooth works but discovery is slow and you're limited to advertising 28 bytes. Has anyone found a reliable cross-platform approach to BLE device discovery that doesn't require a central server or pre-shared identifiers? Comments URL: https://news.ycombinator.com/item?id=47481736 Points: 6 # Comments: 5
