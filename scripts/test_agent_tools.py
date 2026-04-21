import sys
import os
import asyncio

# Add the project root to PYTHONPATH
sys.path.append(os.getcwd())

import unittest
from backend.agents.specifier import SpecifierAgent
from backend.agents.base import BaseAgent
from google.adk.tools import FunctionTool

class TestAgentToolWiring(unittest.IsolatedAsyncioTestCase):
    async def test_specifier_agent_wiring(self):
        agent = SpecifierAgent()
        
        # Check if tools are registered in the internal list
        self.assertEqual(len(agent.tools), 3)
        for tool in agent.tools:
            self.assertIsInstance(tool, FunctionTool)
        
        # Check tool names
        tool_names = [t.name for t in agent.tools]
        self.assertIn("read_file", tool_names)
        self.assertIn("write_file", tool_names)
        self.assertIn("search_files", tool_names)
        
        # Check if adk_agent can be initialized
        agent._initialize_agent()
        self.assertIsNotNone(agent.adk_agent)
        self.assertEqual(agent.adk_agent.name, "Specifier")
        
        # canonical_tools is an async method
        tools = await agent.adk_agent.canonical_tools()
        self.assertEqual(len(tools), 3)
        
        print("Agent tool wiring verified successfully!")

if __name__ == "__main__":
    unittest.main()
