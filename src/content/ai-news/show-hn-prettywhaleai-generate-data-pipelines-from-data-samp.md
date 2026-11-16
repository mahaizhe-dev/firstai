---
title: 'Show HN: Prettywhale.ai – Generate data pipelines from data samples'
description: 'Hi HN,I’m Kevin, I run product at PrettyWhale.ai, a small team based in France.We''ve spent the last few months building a VS Code extension that writes the tedious part of ingestion code from a data s'
pubDate: 2026-11-16T13:11:30
source: 'Hacker News'
sourceUrl: 'https://marketplace.visualstudio.com/items?itemName=prettywhale-ai.prettywhale'
tags: []
---

Hi HN,I’m Kevin, I run product at PrettyWhale.ai, a small team based in France.We've spent the last few months building a VS Code extension that writes the tedious part of ingestion code from a data sample.How it works: You give it a CSV or JSON sample. It profiles the fields, you pick the ones to keep, then it suggests transformations you can accept, edit or drop. At the end you get a complete Python project in your workspace that includes all the necessary quality controls: - Pipeline & transformation code - Unit tests - Config files - DocumentationA design choice we care about: the generation of pipeline is driven by a deterministic workflow rather than an endless chat window (no prompting required). We truly believe that the future of integrating AI into tools will involve a redesign of our user interfaces to get the most out of it.What it doesn’t do yet: it works from a file (CSV or JSON) you already have. It doesn’t connect to databases or API. These features are scheduled for release by the end of the year.To try it, there’s a VS Code extension: https://marketplace.visualstudio.com/items?itemName=prettywh... You need an account but free with no credit card.The model runs on our servers, and the samples are not used to train the models. Comments URL: https://news.ycombinator.com/item?id=50517255 Points: 3 # Comments: 3
