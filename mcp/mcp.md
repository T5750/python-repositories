# MCP

MCP 是一个开放协议，它为应用程序向 LLM 提供上下文的方式进行了标准化。你可以将 MCP 想象成 AI 应用程序的 USB-C 接口。就像 USB-C 为设备连接各种外设和配件提供了标准化的方式一样，MCP 为 AI 模型连接各种数据源和工具提供了标准化的接口。

## 核心 MCP 概念
MCP 服务器可以提供三种主要类型的能力：
1. Resources: 可以被 clients 读取的类文件数据（如 API 响应或文件内容）
2. Tools: 可以被 LLM 调用的函数（需要用户批准）
3. Prompts: 预先编写的模板，帮助用户完成特定任务

## FastAPI-MCP
一个零配置工具，用于自动将 FastAPI 端点公开为模型上下文协议（MCP）工具
- MCP endpoint: [http://127.0.0.1:8000/mcp](http://127.0.0.1:8000/mcp)
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

## FastMCP
The fast, Pythonic way to build MCP servers and clients.
- MCP endpoint: [http://127.0.0.1:8000/sse](http://127.0.0.1:8000/sse)

### Installation
```sh
pip install fastmcp
```

### Examples
[examples](https://github.com/jlowin/fastmcp/tree/main/examples)

## Runtime Environment
- [MCP 简介](https://mcp-docs.cn/introduction)
- [FastAPI](https://fastapi.tiangolo.com/zh/)
- [FastAPI GitHub](https://github.com/fastapi/fastapi)
- [FastAPI-MCP](https://fastapi-mcp.tadata.com/)
- [FastAPI-MCP GitHub](https://github.com/tadata-org/fastapi_mcp)
- [FastAPI-MCP Quickstart](https://fastapi-mcp.tadata.com/getting-started/quickstart)
- [Uvicorn](https://www.uvicorn.org/)
- [Cursor](https://www.cursor.com/cn)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)
- [FastMCP Quickstart](https://gofastmcp.com/getting-started/quickstart)
- [FastMCP FastAPI Integration](https://gofastmcp.com/patterns/fastapi)