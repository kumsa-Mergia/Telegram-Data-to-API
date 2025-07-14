from ultralytics import YOLO
from pathlib import Path
import pandas as pd

class YOLOImageDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)
        self.results = []

    def detect_objects_in_folder(self, root_folder):
        self.results = []
        root_path = Path(root_folder)

        for image_path in root_path.rglob("*"):
            if image_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                try:
                    result = self.model(str(image_path))[0]
                    message_id = image_path.stem

                    for box in result.boxes:
                        self.results.append({
                            "message_id": int(message_id) if message_id.isdigit() else None,
                            "detected_object_class": self.model.names[int(box.cls[0])],
                            "confidence_score": float(box.conf[0])
                        })
                except Exception as e:
                    print(f" Failed to process {image_path.name}: {e}")

        return pd.DataFrame(self.results)
