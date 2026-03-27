---
title: 'Show HN: I made an AI that reviews iPhone apps – 1h of autonomous GUI work'
description: 'I''ve been building Understudy, an open-source GUI agent for macOS. Wanted to push the GUI stuff beyond the usual short demos, so I tried turning it into an iPhone app reviewer.You give it one prompt. '
pubDate: 2026-03-27T19:39:28
source: 'Hacker News'
sourceUrl: 'https://understudy-ai.github.io/understudy/'
tags: []
---

I've been building Understudy, an open-source GUI agent for macOS. Wanted to push the GUI stuff beyond the usual short demos, so I tried turning it into an iPhone app reviewer.You give it one prompt. It browses the real App Store in Chrome, installs the app on a real iPhone through macOS iPhone Mirroring (not a simulator), opens the app and explores it — never seen Snapseed before — records clips and screenshots, composites a narrated review video with FFmpeg locally, uploads it to YouTube, then deletes the app. About an hour, didn't touch the keyboard.The exploration part is what I'm happiest with. The agent reads the App Store description, goes "they say background removal works, let me try that," and then figures out an unfamiliar app on its own. It regrounds from the live screenshot every action, so unexpected dialogs or UI changes don't kill it.The reason it can sustain an hour of work: each of the 6 stages runs as a separate child session with its own context. You can't fit an hour of screenshots into one window, so the isolation is necessary. Stages are typed — "workers" are deterministic (browser automation, device control), "skills" are agentic (the agent decides what to do). A "playbook" orchestrates both.Result video (what the agent published): https://youtube.com/shorts/jliTvpTnsKY?feature=shareProcess video (how it was built): https://youtu.be/gYMYI0bxkJsX: https://x.com/LiangSong850509/status/2037612742392357218?s=2...MIT license. Comments URL: https://news.ycombinator.com/item?id=47547256 Points: 1 # Comments: 0
