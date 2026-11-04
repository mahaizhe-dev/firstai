---
title: 'Show HN: Export your Character.AI chats in minutes – open-source, runs locally'
description: 'Character.AI filed for Chapter 11 in October, and the auction of the company is scheduled for November 23. Its built-in data export can take three to four weeks, and the download link expires after se'
pubDate: 2026-11-03T23:33:27
source: 'Hacker News'
sourceUrl: 'https://github.com/anima-universe/character-ai-chat-exporter'
tags: []
---

Character.AI filed for Chapter 11 in October, and the auction of the company is scheduled for November 23. Its built-in data export can take three to four weeks, and the download link expires after seven days. People with years of conversations have been asking how to keep a copy before anything changes.This is a small browser extension for Chrome and Firefox (Manifest V3). On a character.ai tab you press its button, and it reads your own chats, characters, personas and memory boxes from the site's web API with the session you are already signed in with, one request at a time, and saves one JSON file, plus plain text if you want it. Every line keeps who wrote it and when, which the official export does not.It asks for no permissions in advance (activeTab and scripting), only reads, talks to nothing but character.ai, and has no analytics or servers. The code in src/ is what runs: nothing is bundled or minified. MIT license.Disclosure: we make Amavie, an AI character app. We also built a free viewer that opens the file, or the official export ZIP, in the browser without uploading it: https://amavie.ai/character-ai-export. The extension does not need an account with us.The store listings are in review; until then, unzip the Chrome build from Releases and load it unpacked. Feedback is welcome, especially from very large accounts. Comments URL: https://news.ycombinator.com/item?id=50359691 Points: 1 # Comments: 0
