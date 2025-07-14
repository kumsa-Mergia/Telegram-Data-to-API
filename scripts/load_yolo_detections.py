import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Step 1: Load environment variables from .env
load_dotenv()

# Step 2: Read YOLO detection CSV
df = pd.read_csv("data/yolo_detections.csv")

# Step 3: Build PostgreSQL connection URL from .env variables
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
PG_PORT = os.getenv("PG_PORT")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{PG_PORT}/{POSTGRES_DB}"

# Step 4: Connect and upload
engine = create_engine(DATABASE_URL)

# Step 5: Write to 'raw.yolo_detections' table
df.to_sql("yolo_detections", engine, schema="raw", index=False, if_exists="replace")

print("✅ YOLO detections loaded successfully into raw.yolo_detections")
