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

## 🧱 About dbt in This Project

[dbt](https://www.getdbt.com/) (data build tool) is used to manage the transformation layer of the pipeline. It enables version-controlled, modular SQL modeling and automated testing.

### Key Features:
- Transforms raw Telegram data into clean, analytics-ready models
- Implements data quality tests (`not_null`, `unique`, `relationships`)
- Generates documentation for models and sources
- Supports reproducible and auditable analytics workflows

Models are organized into:
- `staging`: cleaned and renamed raw data
- `marts`: final analytics tables and fact models

---

## 📂 Project Structure

```

.
├── .github/
│   └── workflows/                # GitHub Actions CI/CD workflows
├── dbt/
│   └── telegram_warehouse/
│       ├── models/
│       │   ├── marts/
│       │   │   └── dim_channels.sql
│       │   │   └── dim_dates.sql
│       │   │   └── fct_messages.sql
│       │   │   
│       │   ├── staging/
│       │   │   └── schema.yml
│       │   │   └── stg_telegram_messages.sql
│       │   │   └── stg_yolo_detections.sql
│       │   └── fact/
│       │   │   └── schema.yml
│       │   │   └── fct_image_detections.sql
│       │   ├── sources.yml
│       └── dbt_project.yml
├── notebook/
│   └── 1.0-telegram-scraper.ipynb  # Jupyter notebook for initial data exploration
│   └── 3.0-image-detection.ipynb 
├── script/
│   ├── scrape_telegram.py         # Script to scrape data from Telegram
│   ├── load_json_to_postgres.py   # Loads scraped JSON data into PostgreSQL
│   └── detect_objects_yolo.py
├── src/
│   └── telegram_scraper.py        # TelegramScraper class implementation
├── .gitignore                     # Files and folders to ignore in Git
├── Dockerfile                     # Docker build instructions
├── README.md                      # Project overview and setup instructions
├── docker-compose.yml             # Multi-container setup for services
└── requirements.txt               # Python dependencies

````

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
````

```
