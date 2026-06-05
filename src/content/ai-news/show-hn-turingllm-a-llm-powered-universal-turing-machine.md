---
title: 'Show HN: TuringLLM – a LLM-powered Universal Turing machine'
description: 'Hi, I built TuringLLM to see how far we could go with a universal execution model totally controlled by an LLM.The basic idea: use the LLM for the step function of a Turing machine. State and instruct'
pubDate: 2026-06-05T19:09:43
source: 'Hacker News'
sourceUrl: 'https://github.com/gmlion/TuringLLM'
tags: []
---

Hi, I built TuringLLM to see how far we could go with a universal execution model totally controlled by an LLM.The basic idea: use the LLM for the step function of a Turing machine. State and instructions are MD files (STATE.md and INSTRUCTIONS.md, respectively). They represent the "modifiable tape" of the Turing machine. Each cycle, the LLM read the state and finds the corresponding instruction to execute. Instructions (and conditions) are written as free-text and, together with state, can be written by the LLM itself during execution.The scope of each cycle is controlled - each LLM invocation only receives STATE and INSTRUCTIONS. On top of it, a call-stack mechanism provides hierarchical invocation of subroutines with argument passing and return values. This can be used to implement freely multi-agents patterns and also meta-frameworks.To test its "universality", I implemented 14 patterns from the MAS literature, including Tree of Thoughts, LATS, Meta got, ADAS. They share common operatore when possible. is part is still very much a WIP and may be a bit rough around the edges, so feel free to peek and suggest improvements - but I can confirm it's easy to implement and see a new pattern run in no time; all it takes is some prompting to build the INTERPRETER.md.There's also a visualizer that renders the cycles and the subroutines as a graph or each cycle as a log of the machine's state.Let me know what you think, especially if you're working on agents or MAS research. Comments URL: https://news.ycombinator.com/item?id=48416857 Points: 1 # Comments: 0
