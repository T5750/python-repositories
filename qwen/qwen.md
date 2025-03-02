# Qwen

## Contents
- Qwen2.5: [qwen0.5b_demo.py](qwen0.5b_demo.py)

```sh
python web_demo.py --server-name 0.0.0.0 --checkpoint-path D:/models/Qwen/Qwen2.5-0.5B
```

## Installation
```sh
pip install transformers -U
pip install gradio
git lfs install
git clone https://hf-mirror.com/Qwen/Qwen2.5-0.5B
```

## vLLM
```sh
python gradio_openai_chatbot_webserver.py --model Qwen/Qwen2.5-0.5B
```

## References
- [Qwen2.5 GitHub](https://github.com/QwenLM/Qwen2.5)
- [Qwen 快速开始](https://qwen.readthedocs.io/zh-cn/latest/getting_started/quickstart.html)
- [Qwen/Qwen2.5-0.5B](https://hf-mirror.com/Qwen/Qwen2.5-0.5B)
- [Qwen2 网页demo代码](https://github.com/QwenLM/Qwen2.5/blob/main/examples/demo/web_demo.py)
- [gradio_openai_chatbot_webserver.py GitHub](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/gradio_openai_chatbot_webserver.py)