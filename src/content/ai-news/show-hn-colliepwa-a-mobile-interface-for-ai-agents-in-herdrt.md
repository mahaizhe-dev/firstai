---
title: 'Show HN: ColliePWA a mobile interface for AI agents in herdr/tmux/zellij'
description: 'Sharing the PWA[1] I built over the last couple of weeks to access my terminal sessions/agents when not in front of my computer. This started off as a weekend experiment right when herdr[2] (terminal '
pubDate: 2026-09-09T18:11:46
source: 'Hacker News'
sourceUrl: 'https://colliepwa.dev/'
tags: []
---

Sharing the PWA[1] I built over the last couple of weeks to access my terminal sessions/agents when not in front of my computer. This started off as a weekend experiment right when herdr[2] (terminal multiplexer) released the functionality to write custom plugins and it's been quite helpful to me ever since. The general idea is that this runs a web app on the host machine which is then exposed through a front door implementation like tailscale/netbird/cloudflare tunnels etc.A lot of devs/teams are building sth very similar to this right now so there are many options out there already but I wanted: A PWA (no app store dep), better keyboard support than termux, the ability to manage multiple machines and easy integration with my existing tailnet via headscale.Some of the other features - Push notifications - Support for tmux and zellij (experimental). - Voice transcriptions (Codex sub or API) - Custom commandsYou can check out a live demo with dummy data on the website[1] or look at the implementation on Github[3] (PRs welcome).Looking forward to receiving some feedback or learning more about how people access/work with their agents on the go. Also if you encounter any bugs please report them on Github, if a feature is missing you'd really want to see, open a discussion.[1] https://colliepwa.dev [2] https://herdr.dev [3] https://github.com/AltanS/collie Comments URL: https://news.ycombinator.com/item?id=49630842 Points: 1 # Comments: 0
