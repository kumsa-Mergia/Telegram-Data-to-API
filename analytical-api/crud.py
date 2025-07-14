from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def get_top_products(db: Session, limit: int = 10):
    query = text("""
        SELECT detected_object_class, COUNT(*) as count
        FROM fct_image_detections
        GROUP BY detected_object_class
        ORDER BY count DESC
        LIMIT :limit
    """)
    return db.execute(query, {"limit": limit}).fetchall()

def get_channel_activity(db: Session, channel_name: str):
    query = text("""
        SELECT date::date, COUNT(*) as message_count
        FROM fct_messages
        WHERE channel_name = :channel
        GROUP BY date::date
        ORDER BY date::date
    """)
    return db.execute(query, {"channel": channel_name}).fetchall()

def search_messages(db: Session, keyword: str):
    query = text("""
        SELECT id, date, text, channel_name
        FROM fct_messages
        WHERE text ILIKE :pattern
        ORDER BY date DESC
        LIMIT 100
    """)
    return db.execute(query, {"pattern": f"%{keyword}%"}).fetchall()
