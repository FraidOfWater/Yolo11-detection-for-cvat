import io
import base64
import json
import cv2
import numpy as np
from ultralytics import YOLO

def init_context(context):
    context.logger.info("Initializing model...")
    model = YOLO("yolo11n.pt")  # Replace with your model path
    context.user_data.model = model
    context.logger.info("Model initialized.")

def handler(context, event):
    context.logger.info("Processing request...")

    # Check if event.body is already a dictionary
    if isinstance(event.body, dict):
        data = event.body
    else:
        # If not, assume it's a JSON string and parse it
        data = json.loads(event.body)

    image_data = base64.b64decode(data["image"])
    image = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    model = context.user_data.model
    results = model(image)

    detections = []
    for result in results:
        for box, cls, conf in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
            label = model.names[int(cls)]
            detections.append({
                "confidence": float(conf),
                "label": label,
                "points": box.tolist(),
                "type": "rectangle"
            })

    return context.Response(
        body=json.dumps(detections),
        content_type="application/json",
        status_code=200
    )
