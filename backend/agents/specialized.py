from typing import Optional
from backend.agents.base import BaseAgent, AgentConfig
from backend.agents.tools import read_file_tool, write_file_tool, search_files_tool

class CoderAgent(BaseAgent):
    """Agent specialized in writing code based on tasks."""
    
    def __init__(self):
        config = AgentConfig(
            name="Coder",
            role="Software Engineer",
            system_instruction=(
                "You are a skilled software engineer. Your goal is to implement feature code "
                "based on the provided plan and tasks. Follow SOLID principles and the Project Constitution."
            )
        )
        super().__init__(config)
        self.register_tool(read_file_tool)
        self.register_tool(write_file_tool)
        self.register_tool(search_files_tool)

    def run(self, task_description: str, context: Optional[dict] = None) -> str:
        """Implement the given task."""
        prompt = f"Implement the following task based on the plan:\n\n{task_description}"
        if context:
            prompt += f"\nContext: {context}"
        
        return super().run(prompt)

class ReviewerAgent(BaseAgent):
    """Agent specialized in reviewing code for quality and compliance."""
    
    def __init__(self):
        config = AgentConfig(
            name="Reviewer",
            role="Senior Architect",
            system_instruction=(
                "You are a senior architect. Your goal is to review code changes for "
                "correctness, security, and adherence to the DroneApp Constitution. "
                "Provide clear, actionable feedback."
            )
        )
        super().__init__(config)
        self.register_tool(read_file_tool)
        self.register_tool(search_files_tool)

    def run(self, code_diff: str, context: Optional[dict] = None) -> str:
        """Review the given code changes."""
        prompt = f"Review the following code changes:\n\n{code_diff}"
        if context:
            prompt += f"\nContext: {context}"
        
        return super().run(prompt)
