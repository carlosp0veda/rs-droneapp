from typing import Optional
from backend.agents.base import BaseAgent, AgentConfig
from backend.agents.tools import read_file_tool, write_file_tool, search_files_tool

class PlannerAgent(BaseAgent):
    """Agent specialized in generating implementation plans and task lists."""
    
    def __init__(self):
        config = AgentConfig(
            name="Planner",
            role="Lead Developer",
            system_instruction=(
                "You are a lead developer. Your goal is to analyze a feature specification "
                "and generate a detailed 'plan.md' and a 'tasks.md'. "
                "Ensure the plan adheres to the Project Constitution and SOLID principles. "
                "Break down tasks into small, independently testable increments."
            )
        )
        super().__init__(config)
        self.register_tool(read_file_tool)
        self.register_tool(write_file_tool)
        self.register_tool(search_files_tool)

    def run(self, spec_content: str, context: Optional[dict] = None) -> str:
        """Process the specification and generate plan/tasks."""
        prompt = f"Analyze the following specification and generate a detailed implementation plan and task list:\n\n{spec_content}"
        if context:
            prompt += f"\nContext: {context}"
        
        return super().run(prompt)
