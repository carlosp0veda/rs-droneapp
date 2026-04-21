import pytest
from backend.orchestrator.state import OrchestrationState, SDLCPhase
from backend.orchestrator.engine import SDLCOrchestrator

def test_initial_transition():
    state = OrchestrationState(feature_id="test", branch_name="test")
    orchestrator = SDLCOrchestrator(state)
    
    assert state.current_phase == SDLCPhase.NOT_STARTED
    
    result = orchestrator.step("Create a new feature")
    assert state.current_phase == SDLCPhase.SPECIFYING
    assert "Specification generated" in result

def test_approval_transition():
    state = OrchestrationState(
        feature_id="test", 
        branch_name="test", 
        current_phase=SDLCPhase.SPECIFYING
    )
    orchestrator = SDLCOrchestrator(state)
    
    orchestrator.approve()
    assert state.current_phase == SDLCPhase.PLANNING
