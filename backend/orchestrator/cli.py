import os
import sys
import argparse
import json
from backend.orchestrator.state import OrchestrationState, SDLCPhase, save_state, load_state
from backend.orchestrator.engine import SDLCOrchestrator
from dotenv import load_dotenv

# 1. Get the absolute path to the directory where cli.py lives (.../backend/orchestrator)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level to get the backend directory path (.../backend)
backend_dir = os.path.dirname(current_dir)

# 3. Construct the exact path to backend/.env
env_path = os.path.join(backend_dir, '.env')

# 4. Load that specific file
load_dotenv(env_path)

def get_state_path(feature_id: str) -> str:
    return os.path.join(".specify", f"state_{feature_id}.json")

def init_command(args):
    feature_id = args.short_name or "new-feature"
    feature_dir = f"specs/{feature_id}"
    os.makedirs(feature_dir, exist_ok=True)
    
    state = OrchestrationState(
        feature_id=feature_id,
        branch_name=feature_id, # Simplified
        metadata={"feature_dir": feature_dir}
    )
    
    orchestrator = SDLCOrchestrator(state)
    result = orchestrator.step(args.description)
    
    save_state(state, get_state_path(feature_id))
    print(result)

def approve_command(args):
    # Determine feature_id from current context or provided arg
    feature_id = args.feature_id
    state_path = get_state_path(feature_id)
    
    if not os.path.exists(state_path):
        print(f"Error: No orchestration state found for {feature_id}")
        return

    state = load_state(state_path)
    orchestrator = SDLCOrchestrator(state)
    result = orchestrator.approve()
    
    save_state(state, state_path)
    print(result)

def status_command(args):
    feature_id = args.feature_id
    state_path = get_state_path(feature_id)
    
    if not os.path.exists(state_path):
        print(f"Error: No orchestration state found for {feature_id}")
        return

    state = load_state(state_path)
    print(f"Feature: {state.feature_id}")
    print(f"Phase:   {state.current_phase}")
    print(f"Updated: {state.updated_at}")
    print("\nRecent History:")
    for msg in state.history[-5:]:
        print(f"[{msg.role}] {msg.content[:100]}...")

def fix_command(args):
    feature_id = args.feature_id
    state_path = get_state_path(feature_id)
    
    if not os.path.exists(state_path):
        print(f"Error: No orchestration state found for {feature_id}")
        return

    state = load_state(state_path)
    orchestrator = SDLCOrchestrator(state)
    
    print(f"Injecting fix instructions: {args.instructions}")
    result = orchestrator.step(f"FIX: {args.instructions}")
    
    save_state(state, state_path)
    print(result)

def main():
    parser = argparse.ArgumentParser(description="SDLC Orchestrator CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Init
    init_parser = subparsers.add_parser("init", help="Initialize a new feature")
    init_parser.add_argument("description", help="Feature description")
    init_parser.add_argument("--short-name", help="Concise name for the feature")

    # Approve
    approve_parser = subparsers.add_parser("approve", help="Approve current artifact")
    approve_parser.add_argument("--feature-id", required=True, help="Feature ID to approve")

    # Status
    status_parser = subparsers.add_parser("status", help="Show current status")
    status_parser.add_argument("--feature-id", required=True, help="Feature ID")

    # Fix
    fix_parser = subparsers.add_parser("fix", help="Inject fix instructions")
    fix_parser.add_argument("--feature-id", required=True, help="Feature ID")
    fix_parser.add_argument("instructions", help="What needs to be fixed")

    args = parser.parse_args()

    if args.command == "init":
        init_command(args)
    elif args.command == "approve":
        approve_command(args)
    elif args.command == "status":
        status_command(args)
    elif args.command == "fix":
        fix_command(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
