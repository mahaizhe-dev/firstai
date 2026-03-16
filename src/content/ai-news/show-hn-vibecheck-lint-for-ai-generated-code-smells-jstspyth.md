---
title: 'Show HN: Vibecheck – lint for AI-generated code smells (JS/TS/Python)'
description: 'I built a CLI that detects patterns AI coding tools leave behind: empty catch blocks, hardcoded secrets, as any everywhere, comments that restate the code, god functions, SQL concatenation.24 rules ac'
pubDate: 2026-03-16T12:42:02
source: 'Hacker News'
sourceUrl: 'https://github.com/yuvrajangadsingh/vibecheck'
tags: []
---

I built a CLI that detects patterns AI coding tools leave behind: empty catch blocks, hardcoded secrets, as any everywhere, comments that restate the code, god functions, SQL concatenation.24 rules across JS/TS and Python. Zero config, runs offline, regex-based so it's fast. npx @yuvrajangadsingh/vibecheck . Also ships as a GitHub Action for inline PR annotations and standalone binaries (no Node required).Why: CodeRabbit found AI-generated PRs have 1.7x more issues than human PRs. Veracode says 45% of AI code samples have security vulnerabilities. "Vibe coding" is everywhere now but nobody's linting for the patterns it produces.This isn't a replacement for ESLint. It catches things ESLint doesn't look for, like catch blocks that only console.error without rethrowing, bare except: pass in Python, or mutable default arguments. Comments URL: https://news.ycombinator.com/item?id=47398197 Points: 4 # Comments: 1
