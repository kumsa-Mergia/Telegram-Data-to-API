import os
import json
import datetime
import logging
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from telethon import TelegramClient


class TelegramScraper:
    def __init__(self, session_name="scraper_session"):
        load_dotenv()
        self.api_id = int(os.getenv("TELEGRAM_API_ID"))
        self.api_hash = os.getenv("TELEGRAM_API_HASH")
        self.client = TelegramClient(session_name, self.api_id, self.api_hash)
        self.base_dir = Path("../data/raw")

        # Set up logging
        log_dir = Path("logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            filename=log_dir / "scraper.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    async def connect(self):
        await self.client.start()
        logging.info("✅ Telegram client connected.")

    async def disconnect(self):
        await self.client.disconnect()
        logging.info("🔌 Telegram client disconnected.")

    async def scrape_channel(self, channel_url: str, limit: int = 100):
        try:
            entity = await self.client.get_entity(channel_url)
            messages = []
            today = datetime.date.today().isoformat()

            # Prepare output directory
            out_dir = self.base_dir / today
            out_dir.mkdir(parents=True, exist_ok=True)

            # Channel name for safe filename
            name = entity.username or entity.title.replace(" ", "_").replace("/", "_")

            # Prepare image output path
            image_dir = out_dir / "images" / name
            image_dir.mkdir(parents=True, exist_ok=True)

            async for msg in self.client.iter_messages(entity, limit=limit):
                msg_dict = {
                    "id": msg.id,
                    "date": str(msg.date),
                    "text": msg.text or "",
                    "message": msg.message or "",
                    "sender_id": getattr(msg.sender_id, 'user_id', None) if msg.sender_id else None,
                    "media_type": type(msg.media).__name__ if msg.media else None,
                }

                # Save image if available
                if msg.media and hasattr(msg.media, "photo"):
                    image_filename = f"{msg.id}.jpg"
                    image_path = image_dir / image_filename
                    try:
                        await self.client.download_media(msg.media, file=image_path)
                        msg_dict["downloaded_image_path"] = str(image_path)
                    except Exception as e:
                        logging.warning(f"⚠️ Failed to download image {msg.id} from {name}: {e}")

                messages.append(msg_dict)

            # Save messages to JSON
            file_path = out_dir / f"{name}.json"
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(messages, f, ensure_ascii=False, indent=2)

            logging.info(f"📦 Scraped {len(messages)} messages from {name}")
            return name, len(messages)

        except Exception as e:
            logging.error(f"❌ Failed to scrape {channel_url}: {e}")
            return channel_url, 0

    async def scrape_multiple(self, channel_urls: list, limit: int = 100):
        await self.connect()
        summary = []
        for url in channel_urls:
            try:
                name, count = await self.scrape_channel(url, limit)
                print(f"[✓] {name}: {count} messages")
                summary.append((name, count))
            except Exception as e:
                print(f"[!] Failed for {url} - {str(e)}")
                logging.error(f"[!] Failed for {url} - {e}")
        await self.disconnect()
        return summary