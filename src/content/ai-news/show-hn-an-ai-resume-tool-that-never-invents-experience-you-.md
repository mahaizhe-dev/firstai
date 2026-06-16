---
title: 'Show HN: An AI resume tool that never invents experience you didn''t have'
description: 'I have seen way too many people waste time tailoring their resumes to a specific Job description, practicing interview questions etc. and most of them don''t trust AI tailoring and rightfully so, cuz i'
pubDate: 2026-06-16T15:22:50
source: 'Hacker News'
sourceUrl: 'https://hiredcopilot.com'
tags: []
---

I have seen way too many people waste time tailoring their resumes to a specific Job description, practicing interview questions etc. and most of them don't trust AI tailoring and rightfully so, cuz it invents experience you never had. All it takes is the interviewer asking you one question that you do not know the answer to and the house of cards falls. So hear me out:I made HiredCopilot an AI tool that helps you tailor your resume for a specific job description and I made it different. Apart from all the features a usual AI resume tailoring app has, I made it so that it never invents ANYTHING that you can't defend in an interview.Here is how that specific part works: The tailoring pass is constrained to the source content and a check diffs the generated claims against the original resume so invented specifics get caught instead of shipped. The UI also shows a before/after of exactly what changed so nothing gets silently added.The stack is Next.js + FastAPI, Claude for the AI and OF COURSE rate limiting cuz i don't want a 10k$ bill. It is free to try without an account (there is a no-login resume check), with a paid tier for unlimited tailoring. You can check it out here: hiredcopilot.com.I would appreciate your guys feedback, especially on the anti-fabrication approach and also what can i do to make the app better or any errors you may find that need a fix. If you have worked on grounding or faithfulness for LLM output i would love to hear from you on how to do this better. Comments URL: https://news.ycombinator.com/item?id=48556701 Points: 2 # Comments: 0
