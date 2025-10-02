# PaddlePaddle
飞桨新一代框架3.0，源于产业实践的开源深度学习平台

## PaddleOCR
### Contents
- [paddleocr_server.py](paddleocr_server.py)
- [paddleocr_client.py](paddleocr_client.py)

### Installation
```sh
pip install paddleocr fastapi uvicorn requests pillow
nohup python paddleocr_server.py >> paddleocr_server.log 2>&1 &
```

## PaddleX
### Contents
- [paddlex_ocr.py](paddlex_ocr.py)

### Installation
```sh
pip install "paddlex[base]"
```

## Runtime Environment
- [PaddlePaddle 3.x](https://pypi.org/project/paddlepaddle/)
- [PaddleOCR 3.x](https://pypi.org/project/paddleocr/)
- [PaddleX 3.x](https://pypi.org/project/paddlex/)

## References
- [PaddleOCR](https://www.paddleocr.ai/)
- [PaddleX 文档](https://paddlepaddle.github.io/PaddleX/latest/index.html)
