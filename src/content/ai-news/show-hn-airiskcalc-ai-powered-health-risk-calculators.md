---
title: 'Show HN: AIRiskCalc – AI-Powered Health Risk Calculators'
description: 'Last year, my doctor mentioned I should pay attention to my cardiovascular risk. I searched for online calculators and found two problems: they were either filled with ads or simply threw numbers at y'
pubDate: 2026-03-11T14:04:05
source: 'Hacker News'
sourceUrl: 'https://www.airiskcalc.com'
tags: []
---

Last year, my doctor mentioned I should pay attention to my cardiovascular risk. I searched for online calculators and found two problems: they were either filled with ads or simply threw numbers at you without explaining what they meant.So I built AIRiskCalc. It's a collection of free health risk assessment tools with AI interpretation.Currently live with five calculators:ASCVD Risk (10-year cardiovascular risk based on ACC/AHA 2013 Pooled Cohort Equations) Type 2 Diabetes Risk (ADA assessment model) Cardiovascular Risk (multi-factor evaluation) CVD Risk (cerebrovascular focus) Miscarriage Risk (early pregnancy assessment) Implementation: Next.js 15, Cloudflare Pages. AI layer uses Vercel AI SDK with Claude.One detail I paid attention to: the ASCVD formula involves logarithmic transformations and coefficient matrices from the original 2013 paper. I transcribed the equations into TypeScript and verified against sample data in the paper's appendix.Each calculator displays the reference source in code comments. Results include AI-generated explanations of what the numbers mean. No personal data is collected.The question I'm thinking about: where's the line between helpful AI interpretation and overstepping into medical advice? I want the tool to be useful without replacing professional judgment.Feedback welcome on this balance. Comments URL: https://news.ycombinator.com/item?id=47335719 Points: 2 # Comments: 1
