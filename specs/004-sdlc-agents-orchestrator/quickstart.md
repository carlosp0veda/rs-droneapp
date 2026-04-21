# Quickstart: SDLC Agents and Orchestrator

Learn how to use the automated SDLC orchestrator to build features.

## Prerequisites

1.  **Google Cloud Credentials**: Ensure you have valid application default credentials (ADC) configured.
2.  **Local Environment**: Run the setup script to create a virtual environment and install dependencies:
    ```bash
    ./setup.sh
    source .venv/bin/activate
    ```

## Step 1: Start a New Feature

Use the `sdlc.py` tool to describe your feature:

```bash
python3 -m backend.orchestrator.cli init "Add a drone flight simulator dashboard to the frontend"
```

This will:
- Create a new branch (e.g., `003-drone-flight-simulator`).
- Create `specs/003-drone-flight-simulator/spec.md`.
- Ask for your review.

## Step 2: Review and Approve

Read the generated `spec.md`. If it's correct, approve it:

```bash
python3 -m backend.orchestrator.cli approve --feature-id <id>
```

The orchestrator will then start the **Planning** phase.

## Step 3: Automated Implementation

Once you approve the implementation plan, the **Coder Agent** will begin writing code. Parallel agents will concurrently:
- Run linting and static analysis.
- Generate unit tests.
- Review your code for Constitution compliance.

## Step 4: Verification

If tests fail, the **LoopAgent** will automatically attempt to fix the errors. Once all tests pass and agents are satisfied, you will be notified to review the final PR.
