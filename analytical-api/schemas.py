from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TopProduct(BaseModel):
    detected_object_class: str
    count: int

class ChannelActivity(BaseModel):
    date: datetime
    message_count: int

class MessageSearchResult(BaseModel):
    id: int
    date: datetime
    text: Optional[str]
    channel_name: Optional[str]
