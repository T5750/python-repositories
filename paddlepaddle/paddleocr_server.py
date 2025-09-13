import json
import os

import requests
from fastapi import FastAPI, HTTPException
from paddleocr import PaddleOCR
from pydantic import BaseModel

# 初始化FastAPI应用
app = FastAPI(title="PaddleOCR HTTP Service")
# 初始化PaddleOCR实例（全局只初始化一次）
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)
# 确保输出目录存在
os.makedirs("output", exist_ok=True)


# 定义请求体模型
class OCRRequest(BaseModel):
    file: str


# 定义响应模型
class OCRResponse(BaseModel):
    status: str
    message: str
    result: list
    output_image_path: str
    output_json_path: str


@app.post("/ocr", response_model=OCRResponse)
async def perform_ocr(request: OCRRequest):
    try:
        # 从URL下载图片
        response = requests.get(request.file)
        response.raise_for_status()  # 如果请求失败，抛出异常
        # 运行OCR推理
        result = ocr.predict(input=request.file)
        # 处理结果
        all_results = []
        for i, res in enumerate(result):
            # 保存结果到图片和JSON
            img_path = f"output/result_{i}.png"
            json_path = f"output/result_{i}.json"
            res.save_to_img(img_path)
            res.save_to_json(json_path)
            # 读取JSON文件内容
            json_content = None
            if os.path.exists(json_path):
                with open(json_path, 'r', encoding='utf-8') as f:
                    json_content = json.load(f)
            # 提取文本结果
            text_results = []
            for line in res:
                if hasattr(line, 'text'):
                    text_results.append({
                        "text": line.text,
                        "confidence": line.confidence if hasattr(line, 'confidence') else None,
                        "coordinates": line.vertices.tolist() if hasattr(line, 'vertices') else None
                    })
            all_results.append({
                "page": i,
                "text": text_results,
                "image_path": img_path,
                "json_path": json_path,
                "ocrResults": json_content
            })
        return {
            "status": "success",
            "message": "OCR processing completed successfully",
            "result": all_results,
            "output_image_path": "output/",
            "output_json_path": "output/"
        }
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error downloading image: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing OCR: {str(e)}")


@app.get("/")
async def root():
    return {
        "message": "PaddleOCR HTTP Service is running",
        "endpoints": {
            "/ocr": "POST - Perform OCR on an image from URL",
            "/docs": "API documentation"
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
