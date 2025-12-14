from pathlib import Path
from typing import List, Dict, Any

import requests
from fastapi import FastAPI, HTTPException, File, UploadFile, Query
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel, field_validator
from ultralytics import YOLO

def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui.min.css"
    )

applications.get_swagger_ui_html = swagger_monkey_patch
app = FastAPI()
model = YOLO("models/yolo11n.pt")
UPLOAD_DIR = Path("runs/images")
UPLOAD_DIR.mkdir(exist_ok=True)  # 确保目录存在

class ImageRequest(BaseModel):
    image_url: str  # 图片链接
    conf: float = 0.25  # 置信度阈值，默认0.25

    @field_validator('conf')
    def validate_conf(cls, v):
        if not (0.0 <= v <= 1.0):
            raise ValueError('置信度必须在0.0到1.0之间')
        return v

# 下载到指定目录
def download_image(url, save_dir: Path = UPLOAD_DIR):
    filename = Path(url).name
    save_path = save_dir / filename
    if not save_path.exists():  # 避免重复下载
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    return str(save_path)

# 保存上传的文件
def save_upload_file(file: UploadFile, save_dir: Path = UPLOAD_DIR) -> str:
    try:
        save_path = save_dir / file.filename
        with open(save_path, "wb") as buffer:
            buffer.write(file.file.read())
        return str(save_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"保存文件失败：{str(e)}")

# 解析YOLO预测结果
def parse_yolo_results(results: Any) -> List[Dict[str, Any]]:
    detections = []
    if results and len(results) > 0:
        result = results[0]
        for box in result.boxes:
            x1, y1, x2, y2 = map(float, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            cls_name = result.names[cls_id]
            detections.append({
                "class": cls_name,
                "confidence": round(conf, 4),
                "bbox": {
                    "x1": round(x1, 2),
                    "y1": round(y1, 2),
                    "x2": round(x2, 2),
                    "y2": round(y2, 2)
                }
            })
    return detections

@app.post("/predict")
async def predict(request: ImageRequest):
    try:
        image_path = download_image(request.image_url)
        results = model(image_path, conf=request.conf)
        detections = parse_yolo_results(results)
        return {
            "status": "success",
            "image_url": request.image_url,
            "detections": detections,
            "count": len(detections)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"预测失败：{str(e)}")

@app.post("/predict_upload")
async def predict_upload(
        file: UploadFile = File(...),
        conf: float = Query(0.25, ge=0.0, le=1.0, description="置信度阈值，范围0.0-1.0")
):
    try:
        image_path = save_upload_file(file)
        results = model(image_path, conf=conf)
        detections = parse_yolo_results(results)
        return {
            "status": "success",
            "image_url": image_path,
            "detections": detections,
            "count": len(detections)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"预测失败：{str(e)}")

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
