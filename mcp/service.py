from fastmcp import FastMCP
from tools.file_tools import read_file,write_file,list_files

mcp = FastMCP("HelloWorldServer")

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """
    A simple greeting tool. Solely for testing purpose
    """

    return f"Hello {name}"

# for reading file within the workspace folder
mcp.tool()(read_file)
# for reading file within the workspace folder
mcp.tool()(write_file)
# list files in a directory
mcp.tool()(list_files)


if __name__ == "__main__":
    print("Server starting...")
    mcp.run()
