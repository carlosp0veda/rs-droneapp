# Research Report: SDLC Agents and Orchestrator

**Feature**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)

## Google Agent Development Kit (ADK) Analysis

The Google Agent Development Kit (ADK) is the primary framework for building and orchestrating multi-agent systems in this project.

### Core Components

- **`ParallelAgent`**: designed to execute multiple jobs side-by-side. Ideal for independent tasks like running linting, unit tests, and security scans concurrently.
- **`SequentialAgent`**: Manages a pipeline of agents running in a specific, linear order. This fits the overall SDLC state transitions (Specifier -> Planner -> Coder -> Reviewer).
- **`LoopAgent`**: Repeatedly executes a process until a condition is met. Perfect for the "Coder -> Tester -> Fixer" iteration cycle until all tests pass.

### Findings & Decisions

#### 1. Package Selection
- **Decision**: Install `google-adk` via pip.
- **Rationale**: Formally confirmed as the official Google toolkit for agentic workflows.

#### 2. Orchestration Pattern
- **Decision**: Implement a nested orchestration strategy.
- **Rationale**:
    -   The top-level orchestrator will be a `SequentialAgent` managing the high-level SDLC phases.
    -   Phase-specific sub-orchestrators (e.g., the Implementation phase) will use `ParallelAgent` for concurrent reviews and `LoopAgent` for automated debugging.

#### 3. State Persistence
- **Decision**: use a shareable "Artifact Registry" (state object) that agents can read from and write to.
- **Rationale**: ADK's `ParallelAgent` branches are independent. To ensure the Coder knows what the Reviewer found, they must communicate via a shared state or by the Orchestrator merging their outputs.

#### 4. Tool Usage
- **Decision**: All project-level tools (filesystem access, shell execution) will be exposed to agents as ADK-compatible tools using `async def`.

## Alternatives Considered

| Alternative | Rationale for Rejection |
| ----------- | ----------------------- |
| LangChain LangGraph | While powerful, the user specifically requested the Google Agent Development Kit. |
| Custom `asyncio` orchestration | ADK provides higher-level abstractions like `LoopAgent` and `ParallelAgent` out of the box, reducing boilerplate. |

## Open Questions

- **N/A**: Research confirmed the availability and suitability of the Google ADK.
