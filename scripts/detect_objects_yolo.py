import os
import pandas as pd
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

image_dir = "data/images/"
results = []

for image_name in os.listdir(image_dir):
    if image_name.endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(image_dir, image_name)
        prediction = model(image_path)[0]
        message_id = image_name.split(".")[0]  # Assumes image is named {message_id}.jpg

        for box in prediction.boxes:
            results.append({
                "message_id": message_id,
                "detected_object_class": model.names[int(box.cls[0])],
                "confidence_score": float(box.conf[0])
            })

df = pd.DataFrame(results)
df.to_csv("data/yolo_detections.csv", index=False)
print("Saved detections to data/yolo_detections.csv")