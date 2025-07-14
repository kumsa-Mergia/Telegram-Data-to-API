import psycopg2
from dotenv import load_dotenv
import os

class PostgresLoader:
    def __init__(self):
        load_dotenv()
        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=int(os.getenv("PG_PORT", 5432))
        )
        self.cursor = self.conn.cursor()
        self._create_schema_and_table()

    def _create_schema_and_table(self):
        self.cursor.execute("CREATE SCHEMA IF NOT EXISTS external_sources;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS external_sources.yolo_detections (
                message_id BIGINT,
                detected_object_class TEXT,
                confidence_score FLOAT
            );
        """)
        self.conn.commit()

    def insert_detections(self, detections_df):
        for _, row in detections_df.iterrows():
            self.cursor.execute("""
                INSERT INTO external_sources.yolo_detections (
                    message_id, detected_object_class, confidence_score
                ) VALUES (%s, %s, %s);
            """, (
                int(row['message_id']),
                row['detected_object_class'],
                float(row['confidence_score'])
            ))
        self.conn.commit()
        print(f"{len(detections_df)} records inserted.")

    def close(self):
        self.cursor.close()
        self.conn.close()
