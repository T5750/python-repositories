import uvicorn
from fastapi import FastAPI
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi_mcp import FastApiMCP


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.21.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.21.0/swagger-ui.min.css"
    )


applications.get_swagger_ui_html = swagger_monkey_patch
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 自动生成的 operation_id（类似于 "read_user_users__user_id__get"）
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


# 显式 operation_id（工具将被命名为 "get_user_info"）
@app.get("/users/{user_id}", operation_id="get_user_info")
async def read_user(user_id: int):
    return {"user_id": user_id}


mcp = FastApiMCP(
    app,
    # 可选参数
    name="我的 API MCP",
    description="我的 API 描述",
    base_url="http://127.0.0.1:8000",
    describe_all_responses=True,  # 在工具描述中包含所有可能的响应模式
    describe_full_response_schema=True  # 在工具描述中包含完整的 JSON 模式
)

# 直接将 MCP 服务器挂载到您的 FastAPI 应用
mcp.mount(mount_path="sse")

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
