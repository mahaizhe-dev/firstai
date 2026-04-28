---
title: 'Show HN: Knowerage – code coverage for LLM analysis'
description: 'Hello HN! Like most of developers, I have worked on migrating a large legacy codebase with no up-to-date documentation or unit tests, and found AI agents, like Claude LLM, to be very helpful for findi'
pubDate: 2026-04-28T12:36:24
source: 'Hacker News'
sourceUrl: 'https://github.com/MTimma/knowerage'
tags: []
---

Hello HN! Like most of developers, I have worked on migrating a large legacy codebase with no up-to-date documentation or unit tests, and found AI agents, like Claude LLM, to be very helpful for finding and describing specific functionality. However, returning to the same code with agents feels wasteful in terms of token usage. Also, after finishing migrating some part of the software, I wanted to know which parts of the code still required analysis and migration. This would require to visit and review both the code and documentation to find the gaps. After not finding a solution on the internet that satisfied my needs, I created a structure that could link markdown analysis files to the source code. To enforce agent to use this structure to help track documentation coverage, I decided to create a small MCP server. With it the agent is able to tell me how much of the code is left to be analysed in percentage, as well as identify parts of code and functionality that require analysis. The ultimate goal is to identify requirements that have not been migrated yet, assuming the documented functionality has been. The server is entirely local, it does not access the internet, besides for the MCP client to download and run the server package using npx. Important disclaimer! The code was generated using orchestrated Claude Opus-4.5 agents from a set of requirements. The requirement and task markdown files can be found in the 'agent_tasks' folder of the repository. Comments URL: https://news.ycombinator.com/item?id=47933691 Points: 1 # Comments: 0
