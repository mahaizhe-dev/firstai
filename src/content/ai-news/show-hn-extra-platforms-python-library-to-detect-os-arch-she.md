---
title: 'Show HN: Extra-Platforms, Python library to detect OS, arch, shell, CI, AI'
description: 'I built Extra Platforms over the past 5 years because I kept writing the same detection boilerplate over and over. And also because Python''s original platform.linux_distribution() function has been re'
pubDate: 2026-04-02T09:24:09
source: 'Hacker News'
sourceUrl: 'https://github.com/kdeldycke/extra-platforms'
tags: []
---

I built Extra Platforms over the past 5 years because I kept writing the same detection boilerplate over and over. And also because Python's original platform.linux_distribution() function has been removed in Python 3.8. Its replacement, Distro, only covers Linux.It detects six traits (CPU architecture, OS/distribution, shell, terminal, CI, agents), which are grouped into families (BSD, LINUX, UNIX, ...) for convenience.You can try the library without installing anything: $ uvx --with extra-platforms python >>> from extra_platforms import current_platform, BSD, is_linux >>> current_platform() Platform(id='macos', name='macOS') >>> current_platform() in BSD True >>> is_linux() False It also ships Pytest decorators (@skip_linux, @unless_macos) for platform-conditional tests.The library has zero dependencies and is Apache-2.0 licensed.I'm interested in collecting edge cases, which you can send me by performing an auto-detection with: $ uvx extra-platforms Comments URL: https://news.ycombinator.com/item?id=47611994 Points: 4 # Comments: 0
