---
title: 'Show HN: Bash4LLM+ – A lightweight, dependency-free Bash wrapper for LLM APIs'
description: 'Hi HN!I built Bash4LLM+ because I wanted a minimal, transparent, and completely customizable way to interact with LLM APIs directly from my terminal, without having to spin up heavy Python virtual env'
pubDate: 2026-06-27T23:31:18
source: 'Hacker News'
sourceUrl: 'https://github.com/kamaludu/bash4llm/'
tags: []
---

Hi HN!I built Bash4LLM+ because I wanted a minimal, transparent, and completely customizable way to interact with LLM APIs directly from my terminal, without having to spin up heavy Python virtual environments or pull in NPM packages on small VPS instances.It is written in pure Bash (4+) and its only strict dependencies are standard utilities like curl and jq.Some of the implementation details: - It supports standard and streaming API outputs. - It manages session history using an NDJSON flat-file approach, with POSIX fallbacks for file locking when flock is not present on clean/default macOS systems. - It includes a fully-featured interactive REPL chat mode with built-in commands (like /file to load context). - Licensed under GNU GPL v3.The code is fully single-file (with optional extras) and easy to audit. I'd love to hear your feedback on the script design, edge cases, or how you integrate terminal-first LLMs into your daily automation! Comments URL: https://news.ycombinator.com/item?id=48702835 Points: 1 # Comments: 0
