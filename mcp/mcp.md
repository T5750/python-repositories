# MCP

## FastAPI-MCP
一个零配置工具，用于自动将 FastAPI 端点公开为模型上下文协议（MCP）工具
- [MCP endpoint](http://127.0.0.1:8000/mcp)
- [FastAPI - OpenAPI](http://127.0.0.1:8000/docs)

### Installation
```sh
pip install fastapi-mcp
pip install uvicorn
uvicorn fastapi_mcp_main:app --reload
```

### Connecting a client to the MCP server
#### Connecting to the MCP Server using SSE
Cursor Settings -> MCP
```json
{
  "mcpServers": {
    "fastapi-mcp": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

### Examples
[examples](https://github.com/tadata-org/fastapi_mcp/blob/main/examples)

## Runtime Environment
- [FastAPI](https://fastapi.tiangolo.com/zh/)
- [FastAPI GitHub](https://github.com/fastapi/fastapi)
- [FastAPI-MCP](https://fastapi-mcp.tadata.com/)
- [FastAPI-MCP GitHub](https://github.com/tadata-org/fastapi_mcp)
- [FastAPI-MCP Quickstart](https://fastapi-mcp.tadata.com/getting-started/quickstart)
- [Uvicorn](https://www.uvicorn.org/)
- [Cursor](https://www.cursor.com/cn)