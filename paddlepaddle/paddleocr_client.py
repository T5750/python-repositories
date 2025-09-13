import base64
import requests

API_URL = "http://localhost:8080/ocr"
file_path = "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png"

# with open(file_path, "rb") as file:
#     file_bytes = file.read()
#     file_data = base64.b64encode(file_bytes).decode("ascii")

payload = {"file": file_path, "fileType": 1}

response = requests.post(API_URL, json=payload)

assert response.status_code == 200
result = response.json()["result"]
for res in result:
    print(res["ocrResults"]["rec_texts"])
    # ocr_img_path = f"ocr_{i}.jpg"
    # with open(ocr_img_path, "wb") as f:
    #     f.write(base64.b64decode(res["ocrImage"]))
    # print(f"Output image saved at {ocr_img_path}")