from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool()
def multiply(a:int,b:int):
    return a*b

mcp.run()