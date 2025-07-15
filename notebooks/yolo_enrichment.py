import sys
import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

# Add project root to sys.path for imports
project_root = os.path.abspath(os.path.join(os.getcwd(), "../"))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.PostgresLoader import PostgresLoader
from src.YOLOImageDetector import YOLOImageDetector

load_dotenv()

def detect_and_store():
    print("🔍 Scanning for images...")
    base_dir = Path("../data/raw")
    all_detections = []

    detector = YOLOImageDetector(model_path="yolov8n.pt")
    for subdir in base_dir.glob("**/images"):
        if not subdir.is_dir():
            continue
        print(f"🔎 Running detection in: {subdir}")
        detections_df = detector.detect_objects_in_folder(str(subdir))
        if not detections_df.empty:
            all_detections.append(detections_df)

    if all_detections:
        result_df = pd.concat(all_detections, ignore_index=True)
        print(f"📦 Total detections: {len(result_df)}")

        loader = PostgresLoader()
        loader.insert_detections(result_df)
        loader.close()
        print("✅ Inserted into PostgreSQL")
    else:
        print("⚠️ No images with detections found.")

if __name__ == "__main__":
    detect_and_store()
