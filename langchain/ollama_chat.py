from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}
Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="qwen:0.5b-chat")
chain = prompt | model
output = chain.invoke({"question": "What is LangChain?"})
print(output)
