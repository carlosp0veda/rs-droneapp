from typing import Optional
from backend.agents.base import BaseAgent, AgentConfig
from backend.agents.tools import read_file_tool, write_file_tool, search_files_tool

class SpecifierAgent(BaseAgent):
    """Agent specialized in generating feature specifications."""
    
    def __init__(self):
        config = AgentConfig(
            name="Specifier",
            role="Technical Writer & Architect",
            system_instruction=(
                "You are an expert technical writer and software architect. "
                "Your goal is to generate a comprehensive 'spec.md' for a given feature description. "
                "Follow the project's spec-template.md structure. "
                "Ensure requirements are testable and success criteria are measurable."
            )
        )
        super().__init__(config)
        self.register_tool(read_file_tool)
        self.register_tool(write_file_tool)
        self.register_tool(search_files_tool)

    def run(self, feature_description: str, context: Optional[dict] = None) -> str:
        """Process the feature description and generate a spec."""
        prompt = f"Generate a comprehensive specification for the following feature: {feature_description}"
        if context:
            prompt += f"\nContext: {context}"
        
        return super().run(prompt)
