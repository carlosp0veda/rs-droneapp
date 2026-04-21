from typing import List, Any, Optional
from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent
from backend.agents.base import BaseAgent

class WorkflowBuilder:
    """Helper to construct ADK workflow agents."""
    
    @staticmethod
    def create_sequential(name: str, agents: List[Any]) -> SequentialAgent:
        """Create a pipeline of agents."""
        return SequentialAgent(name=name, agents=agents)

    @staticmethod
    def create_parallel(name: str, agents: List[Any]) -> ParallelAgent:
        """Create a group of agents to run concurrently."""
        return ParallelAgent(name=name, agents=agents)

    @staticmethod
    def create_loop(name: str, agent: Any, condition: str) -> LoopAgent:
        """Create an agent that loops until a condition is met."""
        return LoopAgent(name=name, agent=agent, condition=condition)
