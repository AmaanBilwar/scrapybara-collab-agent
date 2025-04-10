# Requirements for the bounty

## Submission rules:
1. Use Scrapybara technology
2. Include a GitHub repository of your code, the project should be open-source
3. Include a README explaining your code and a video demo

[Submission link for the bounty](https://forms.gle/zs7mnuW8U4Cb96Sv5)

## active bounties

Answer engine with computer use - $300
Perplexity-like answer engine where one of the tools is computer use - like our act() and scrape() APIs
Prioritize good UI/UX and a smooth agentic loop


User Query → Query Analysis → Tool Selection → Action Execution → Information Gathering → Response Generation → User Feedback
     ↑                                                                                                              ↓
     └──────────────────────────────── Continuous Refinement ────────────────────────────────────────────────────┘


### Core components needed
 - scrapybara client for instance management
 - ubuntu instance for full capabilities
 - browswer instance for web searches
 - llm model for reasoning
 - tools: BashTool, ComputerTool, EditTool