# Ethiopian Medical Business Data Pipeline & Analytics

## 📌 Project Overview
This project builds an end-to-end data pipeline to extract, transform, enrich, and serve data from Ethiopian medical business Telegram channels. It leverages modern data tools to create a clean, analytical data warehouse, enriched with AI insights, and exposed via an API for business intelligence.

---

## 🛠️ Technologies Used

- **Data Scraping**: Telegram API (Python)
- **Data Lake**: Local JSON files
- **Database**: PostgreSQL
- **Data Transformation**: dbt
- **Image Analysis**: YOLOv8 (Ultralytics)
- **Analytical API**: FastAPI
- **Orchestration**: Dagster

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- Telegram API ID & Hash

### Steps

```bash
# 1. Clone the repository
git clone git@github.com:kumsa-Mergia/Telegram-Data-to-API.git
cd Telegram-Data-to-API

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # For Linux/Mac
# .\venv\Scripts\activate         # For Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. PostgreSQL Setup
#    - Create a database: telegram_db
#    - Create schemas: raw, analytics

# 5. dbt Profile
#    Configure ~/.dbt/profiles.yml to connect dbt to telegram_db
