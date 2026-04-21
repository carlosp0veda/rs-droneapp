import asyncio
from typing import List, Optional, Any, Callable, Dict, Union
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool, BaseTool
from google.adk.tools.base_toolset import BaseToolset
from google.adk.runners import InMemoryRunner
from pydantic import BaseModel, Field


class AgentConfig(BaseModel):
    """Configuration for an ADK agent."""
    name: str
    role: str
    model: str = "gemini-3-flash-preview"
    temperature: float = 0.0
    system_instruction: str

class BaseAgent:
    """Base class for SDLC specialized agents using Google ADK."""
    
    def __init__(self, config: AgentConfig):
        self.config = config
        self.tools: List[Union[BaseTool, BaseToolset]] = []
        self.adk_agent: Optional[LlmAgent] = None

    def _initialize_agent(self):
        """Initialize the ADK agent instance with its configuration and tools."""
        self.adk_agent = LlmAgent(
            name=self.config.name,
            model=self.config.model,
            instruction=self.config.system_instruction,
            tools=self.tools
        )

    def run(self, input_text: str, context: Optional[dict] = None) -> str:
            """Run the agent with the given input using the ADK runtime."""
            import asyncio
            
            if not self.adk_agent:
                self._initialize_agent()
            
            runner = InMemoryRunner(agent=self.adk_agent)
            
            # run_debug returns a list of execution events
            events = asyncio.run(runner.run_debug(input_text))
            
            # Optional: Print out the agent's thought process so you can see it working!
            print("\n--- Agent Execution Trace ---")
            for event in events:
                print(f"Step: {event}")
            print("-----------------------------\n")
            
            # Extract and return the final text response from the very last event
            # (Usually, the last event contains the final generated markdown spec)
            if events and hasattr(events[-1], 'text'):
                return events[-1].text
            else:
                return str(events[-1])
        
    def register_tool(self, tool: Union[Callable, BaseTool, BaseToolset]):
        """Register a tool (function, FunctionTool, or Toolset) for this agent."""
        if isinstance(tool, (BaseTool, BaseToolset)):
            self.tools.append(tool)
        elif callable(tool):
            self.tools.append(FunctionTool(func=tool))
        else:
            raise ValueError(f"Unsupported tool type: {type(tool)}")
