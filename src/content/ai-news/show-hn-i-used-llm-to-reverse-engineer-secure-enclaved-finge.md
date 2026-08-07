---
title: 'Show HN: I used LLM to reverse-engineer secure-enclaved fingerprint scanner'
description: 'I own a Xiaomi Mi Pad 5 Pro 5G Android tablet, which is also pretty-much a perfect Linux tablet: has 5G support, great screen, nice folio keyboard, 8 speakers, a pen, is lightweight and relatively pow'
pubDate: 2026-08-07T12:26:07
source: 'Hacker News'
sourceUrl: 'https://github.com/wrobelda/goodix-fp-spi-linux'
tags: []
---

I own a Xiaomi Mi Pad 5 Pro 5G Android tablet, which is also pretty-much a perfect Linux tablet: has 5G support, great screen, nice folio keyboard, 8 speakers, a pen, is lightweight and relatively powerful. All of its hardware is supported at this point, although not all has been mainlined yet.It also features a Goodix SPI fingerprint scanner, except it is implemented using an app living in Qualcomm's QSEE secure enclave which handles the scanner, and which Android communicates with using a HAL and a protocol that are not documented. This 2021 article explains the problem in details: https://emainline.gitlab.io/2021/12/12/fingerprint_P1.htmlIt took me about a week of intense work of reverse-engineering it with Opus 5 and Kimi K3, and further 5 days on polishing the documentation, but I can safely say this is now done.I used Opus 5, since Fable naturally dropped out as this is security subject, and Kimi K3 for reviewing the code. I resorted to both disassembling and tracing live Android sessions using Frida to figure out the issues along the way.Happy to answer any questions. Also, I expect the same approach can be used to reverse-engineer the secure-enclaved fingerprint scanners on Macbooks and since I run Asahi on my M1, I will look into it when I next take a break from regular work. Comments URL: https://news.ycombinator.com/item?id=49209348 Points: 1 # Comments: 0
