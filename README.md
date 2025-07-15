#  Ethiopian Medical Business Data Pipeline & Analytics

## 🚀 Project Overview

This project implements a complete end-to-end **data pipeline** to extract, process, enrich, and serve medical business data from **Ethiopian Telegram channels**. It integrates **modern data engineering tools**, enabling analytical exploration and AI-powered insights via a robust API.

The final output is an enriched, queryable **PostgreSQL data warehouse**—ideal for data science, reporting, and business intelligence.

---

## 🧰 Tech Stack Overview

| Layer             | Tool/Framework              | Purpose                                       |
| ----------------- | --------------------------- | --------------------------------------------- |
| 📥 Data Ingestion | `Telegram API` (via Python) | Extract chat messages and media from channels |
| 📂 Data Lake      | Local `.json` files         | Raw data storage                              |
| 🧱 Data Warehouse | `PostgreSQL`                | Structured storage for analytics              |
| 🧹 Transformation | `dbt` (Data Build Tool)     | Clean, model, and test data                   |
| 🧠 Enrichment     | `YOLOv8` (Ultralytics)      | Detect objects in shared images using AI      |
| 🌐 API Access     | `FastAPI`                   | Serve insights via RESTful endpoints          |
| ⏱️ Orchestration  | `Dagster`                   | Schedule and monitor pipeline jobs            |

---

## 📦 dbt: Modular, Auditable Transformations

This project uses [**dbt**](https://www.getdbt.com/) to transform raw scraped data into trusted, analytics-ready models.

### 🧠 Features:

* Modular SQL transformations with Jinja
* Built-in testing: `not_null`, `unique`, `relationships`
* Auto-generated documentation (`dbt docs`)
* Reproducible and version-controlled

### 📁 Model Layers:

* `staging/` 
* `marts/`
* `fact/`

---

## 📁 Project Structure

```bash
.
├── .github/workflows/               # CI/CD via GitHub Actions
├── analytical-api/                 # FastAPI for analytics endpoints
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── dagster_jobs/                   # Dagster orchestration jobs
│   ├── jobs.py
│   ├── schedules.py
│   └── ops/
│       ├── scrape.py
│       ├── load.py
│       ├── transform.py
│       └── enrich.py
├── dbt/telegram_warehouse/         # dbt project: models, sources, tests
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   ├── fact/
│   │   └── schema.yml
│   ├── sources.yml
│   └── dbt_project.yml
├── notebook/                       # Jupyter notebooks for EDA & testing
│   ├── 1.0-telegram-scraper.ipynb
│   └── 3.0-image-detection.ipynb
│   └── yolo_enrichment.py
├── script/                         # Standalone utility scripts
│   ├── scrape_telegram.py
│   ├── load_json_to_postgres.py
│   └── detect_objects_yolo.py
├── src/                            # Core logic (OOP)
│   └── telegram_scraper.py
├── .env                            # Environment variables (API keys, DB)
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml                  # Dagster config (via `[tool.dagster]`)
├── README.md
└── requirements.txt
```

---

## ⚙️ Getting Started

### ✅ Prerequisites

* Python 3.8+
* PostgreSQL (e.g., v13+)
* Telegram API credentials (`api_id`, `api_hash`)

---

### 🧪 Installation & Setup

```bash
# 1. Clone the repository
git clone git@github.com:kumsa-Mergia/Telegram-Data-to-API.git
cd Telegram-Data-to-API

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate         # Linux/macOS
# .\venv\Scripts\activate        # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

### 🛠️ PostgreSQL Setup

1. Create a new database named `telegram_db`
2. Create two schemas:

   * `raw` for raw Telegram and YOLO data
   * `analytics` for dbt models

---

### 🧩 dbt Setup

```bash
# Navigate to dbt project directory
cd dbt/telegram_warehouse/

# Create your dbt profile (~/.dbt/profiles.yml)
# Then run the following:
dbt debug           # Validate profile
dbt build           # Run models and tests
dbt docs generate   # Generate documentation
dbt docs serve      # Open docs on localhost
```
## 🖼️ Screenshot  Open docs on localhost
![docs UI Screenshot](https://drive.google.com/uc?id=1_1jGMeuUkmxi6TEJarTHDdYkeurDbT01)


### 🚀 Run the Analytical API (FastAPI)

The API exposes YOLO-enriched message data and analytics from PostgreSQL for consumption by dashboards or other services.

```bash
# Navigate to the API directory
cd analytical-api

# Run the FastAPI server
uvicorn main:app --reload
```

* The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Interactive API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
## 🖼️ Screenshot   Analytical API (FastAPI)
![FastAPI UI Screenshot](https://drive.google.com/uc?id=13Bv52zCdfmXCyC8gjmaaxVOZYzy4UcQ-)



### 🌀 Dagster Setup & Orchestration

```bash
# Run Dagster UI from the project root
dagster dev -w workspace.yaml
```

This command:

* Launches the **Dagster webserver** and **daemon** for local development.
* Loads pipeline definitions from your `workspace.yaml` configuration.
* Exposes the orchestration dashboard at:
  [http://127.0.0.1:3000](http://127.0.0.1:3000)

**Tip**: Make sure you’ve defined your `@job`s inside `dagster_jobs/jobs.py` and pointed to it correctly in your `workspace.yaml`.

---
## 🖼️ Screenshot Dagster UI
![Dagster UI Screenshot](https://drive.google.com/uc?id=1N5cGdi5xV5BWAj6iuYpS8flCPyGqNGhD)

---

## 👨‍💻 Author

**Kumsa Mergia**
🔗 [GitHub](https://github.com/kumsa-Mergia) | 🌍 Ethiopia

---

