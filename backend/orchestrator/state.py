from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime

class SDLCPhase(str, Enum):
    NOT_STARTED = "not_started"
    SPECIFYING = "specifying"
    PLANNING = "planning"
    IMPLEMENTING = "implementing"
    VERIFYING = "verifying"
    COMPLETED = "completed"
    FAILED = "failed"

class AgentMessage(BaseModel):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class OrchestrationState(BaseModel):
    feature_id: str
    branch_name: str
    current_phase: SDLCPhase = SDLCPhase.NOT_STARTED
    history: List[AgentMessage] = Field(default_factory=list)
    artifacts: Dict[str, str] = Field(default_factory=dict)  # phase -> path
    metadata: Dict[str, Any] = Field(default_factory=dict)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        use_enum_values = True

def save_state(state: OrchestrationState, file_path: str):
    """Persist the orchestration state to a JSON file."""
    with open(file_path, "w") as f:
        f.write(state.json())

def load_state(file_path: str) -> OrchestrationState:
    """load the orchestration state from a JSON file."""
    with open(file_path, "r") as f:
        return OrchestrationState.parse_raw(f.read())
