import os
import json
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_PORT = int(os.getenv("PG_PORT", 5432))

conn = None
cursor = None

try:
    print("Attempting to connect to PostgreSQL...")
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("Successfully connected to PostgreSQL!")

    print("Checking/creating 'raw' schema...")
    cursor.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    conn.commit()
    print("Schema 'raw' checked/created.")

    print("Checking/creating 'raw.telegram_messages' table...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw.telegram_messages (
        id BIGINT PRIMARY KEY,
        date TIMESTAMP,
        text TEXT,
        message TEXT,
        sender_id BIGINT,
        media_type TEXT,
        downloaded_image_path TEXT,
        channel_name TEXT
    );
    """)
    conn.commit()
    print("Table 'raw.telegram_messages' checked/created.")

    current_script_dir = Path(__file__).parent
    data_dir = current_script_dir.parent / "data" / "raw"
    print(f"Looking for data in: {data_dir}")


    if not data_dir.exists():
        print(f"Warning: Data directory not found at {data_dir}. Skipping data loading.")
    else:
        files_processed = 0
        records_inserted = 0
        for day_dir in data_dir.iterdir():
            if day_dir.is_dir():
                for file in day_dir.glob("*.json"):
                    print(f"Processing file: {file.name} from {day_dir.name}")
                    try:
                        with open(file, "r", encoding="utf-8") as f:
                            records = json.load(f)
                            files_processed += 1

                            if not isinstance(records, list):
                                if isinstance(records, dict) and 'messages' in records:
                                    records = records['messages']
                                else:
                                    print(f"Warning: Unexpected JSON structure in {file.name}. Skipping file.")
                                    continue

                            for rec in records:
                                channel_name_from_file = file.stem if not rec.get("channel_name") else rec.get("channel_name")
                                cursor.execute("""
                                INSERT INTO raw.telegram_messages (
                                    id, date, text, message, sender_id,
                                    media_type, downloaded_image_path, channel_name)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT (id) DO NOTHING;
                                """, (
                                    rec.get("id"),
                                    rec.get("date"),
                                    rec.get("text"),
                                    rec.get("message"),
                                    rec.get("sender_id"),
                                    rec.get("media_type"),
                                    rec.get("downloaded_image_path"),
                                    channel_name_from_file
                                ))
                                records_inserted += 1 # Increment for each insert attempt
                            conn.commit()
                            print(f"  -> Committed data from {file.name}. Total records inserted (so far): {records_inserted}")
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from {file.name}: {e}. Skipping this file.")
                    except Exception as file_error:
                        print(f"An error occurred while processing {file.name}: {file_error}. Skipping this file.")

        print(f"Finished processing. Total files processed: {files_processed}. Total records attempted for insertion: {records_inserted}.")
    print(" Loaded raw data into PostgreSQL.")

except psycopg2.OperationalError as e:
    print(f"\nFATAL: Error connecting to PostgreSQL: {e}")
    print("Please check your .env file for correct DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, and PG_PORT.")
    print("Also ensure your PostgreSQL server is running and accessible (e.g., check pg_hba.conf).")
except Exception as e:
    print(f"\nFATAL: An unexpected error occurred during database operations: {e}")

finally:
    if cursor:
        cursor.close()
        print("Cursor closed.")
    if conn:
        conn.close()
        print("Connection closed.")