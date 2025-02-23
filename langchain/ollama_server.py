#!/usr/bin/env python
"""Example LangChain server exposes multiple runnables (LLMs in this case)."""

from fastapi import FastAPI
from langchain_ollama.llms import OllamaLLM

from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    OllamaLLM(model="qwen:0.5b-chat"),
    path="/ollama",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
