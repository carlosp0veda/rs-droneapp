import os
import glob
from typing import List, Dict, Any, Optional
from google.adk.tools import FunctionTool, ToolContext

def read_file(path: str, tool_context: Optional[ToolContext] = None) -> Dict[str, Any]:
    """Read the contents of a file.
    
    Args:
        path: Absolute path to the file.
        tool_context: The ADK tool context (optional).
    
    Returns:
        A dictionary with 'status' and 'content'. 
        Example: {'status': 'success', 'content': 'file data...'}
    """
    try:
        with open(path, "r") as f:
            content = f.read()
        return {"status": "success", "content": content}
    except Exception as e:
        return {"status": "error", "message": f"Failed to read {path}: {str(e)}"}

read_file_tool = FunctionTool(func=read_file)

def write_file(path: str, content: str, tool_context: Optional[ToolContext] = None) -> Dict[str, Any]:
    """Write content to a file.
    
    Args:
        path: Absolute path to the file.
        content: The content to write.
        tool_context: The ADK tool context (optional).
    
    Returns:
        A dictionary with 'status' and 'message'.
        Example: {'status': 'success', 'message': 'Successfully wrote to ...'}
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        return {"status": "success", "message": f"Successfully wrote to {path}"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to write to {path}: {str(e)}"}

write_file_tool = FunctionTool(func=write_file)

def search_files(pattern: str, root_dir: str = ".", tool_context: Optional[ToolContext] = None) -> Dict[str, Any]:
    """Search for files matching a pattern.
    
    Args:
        pattern: Glob pattern (e.g., "**/*.py").
        root_dir: The directory to search in.
        tool_context: The ADK tool context (optional).
    
    Returns:
        A dictionary with 'status' and 'files'.
        Example: {'status': 'success', 'files': ['file1.py', 'file2.py']}
    """
    try:
        files = glob.glob(os.path.join(root_dir, pattern), recursive=True)
        return {"status": "success", "files": files}
    except Exception as e:
        return {"status": "error", "message": f"Search failed: {str(e)}"}

search_files_tool = FunctionTool(func=search_files)

def list_directory(path: str, tool_context: Optional[ToolContext] = None) -> Dict[str, Any]:
    """List the contents of a directory.
    
    Args:
        path: Absolute path to the directory.
        tool_context: The ADK tool context (optional).
    
    Returns:
        A dictionary with 'status' and 'items'.
        Example: {'status': 'success', 'items': ['dir1', 'file1.txt']}
    """
    try:
        items = os.listdir(path)
        return {"status": "success", "items": items}
    except Exception as e:
        return {"status": "error", "message": f"Failed to list directory {path}: {str(e)}"}

list_directory_tool = FunctionTool(func=list_directory)
