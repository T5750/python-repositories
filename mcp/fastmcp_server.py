import asyncio

from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")


@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}! - FastMCP"


client = Client(mcp)


async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)


asyncio.run(call_tool("Ford"))

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
