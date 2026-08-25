# Agent Concepts and MCP Basics — Explainer

**Intern:** Gungun Sharma  
**Assignment:** FlyRank AI Internship — FL-05  
**Track:** General AI Fluency

## Workflow vs. Agent

An AI workflow is a system where the route is designed in advance. The developer decides which step happens first, which step follows, what information is passed forward, and where the process ends. A model can still make useful decisions inside individual steps, but the overall path is predictable. This makes workflows easier to test because the same structure is executed repeatedly.

An agent is different mainly because the system can decide what action to take next while working toward a goal. Instead of being locked to one fixed sequence, an agent can choose among available tools, inspect results, revise its plan, and continue until a stopping condition is reached. The important distinction is therefore not whether an LLM is present. It is whether the system has meaningful control over its next actions and can adapt its route to the situation.

My FL-04 pipeline is best classified as a **workflow**, not an agent. Its stages are intentionally arranged as a known sequence: the AI works through defined steps and then reaches the final output/approval point. The model may generate or improve content within a stage, but it does not independently choose an open-ended route or decide which external capability to invoke next. Calling it a workflow is more accurate than using “agent” as a marketing label.

## What MCP adds

Model Context Protocol (MCP) is a standard way for an AI application to connect to external context and capabilities. A useful mental model is a USB-C port for AI applications: the host can connect to different tools and data sources through a common protocol instead of requiring a completely custom integration for every service.

MCP servers expose three important primitives: **tools, resources, and prompts**. Tools are executable functions. They let a model perform an action or retrieve information, such as reading a permitted local file or querying a service. Resources represent contextual data that a client can read and provide to the model. Prompts are reusable templates or instructions that users can explicitly invoke. These primitives have different control patterns, but together they give an AI application a standardized interface to useful external capabilities.

In this submission, the local MCP server exposes file-oriented tools. Claude Desktop can ask the server to list files, read an approved local file, and inspect file metadata. This is materially different from ordinary chat: without a connected local tool, the model cannot directly inspect arbitrary files sitting on my computer.

## Three practical MCP tasks

The first task is listing the files in the demo workspace. The second is reading the contents of a specific approved file. The third is obtaining metadata such as file size, line count, and a SHA-256 hash. Each result is returned by an MCP tool call, rather than being supplied manually in the chat message.

These tasks also show why tool output should be treated as evidence rather than blindly trusted. The server restricts file access to the configured demo workspace and rejects path traversal attempts. This keeps the demonstration bounded and makes the external capability explicit.

## How FL-04 could become an agent

The concrete upgrade I would make to the FL-04 pipeline is a **bounded evidence-verification agent**. Instead of always following the same fixed sequence, the system would receive a goal such as “prepare a final claim using only approved project evidence.” It could inspect the available project files through MCP, choose which evidence to examine, check whether each claim is supported, and request another file when evidence is missing. It would then stop at a human approval gate before publishing anything.

The important part is that the agent would have a defined goal, a limited set of tools, explicit safety boundaries, and a stopping condition. MCP would provide the connection to the external files; the agent layer would decide which available action to take next. That separation keeps the architecture understandable: **MCP is the connection/interface, while agent behavior is the decision-making loop on top of it.**

In short, a workflow follows a designed route, while an agent can select and adapt its route toward a goal. MCP does not automatically turn a workflow into an agent. It supplies a standardized way to give an AI application access to tools, resources, and prompts. My FL-04 build is therefore accurately described as a workflow today, with a bounded evidence-verification agent as the next concrete upgrade.
