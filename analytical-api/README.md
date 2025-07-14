# 📊 Telegram Analytical API – Task 4 (FastAPI)

This FastAPI application provides a set of analytical endpoints powered by enriched data from Telegram messages and YOLOv8 object detection. It queries final dbt models (marts) to serve business insights through clean, well-structured REST endpoints.

---

## 🚀 Features

| Endpoint | Description |
|----------|-------------|
| `GET /api/reports/top-products?limit=10` | Returns the most frequently detected product/object classes (e.g., "person", "bottle"). |
| `GET /api/channels/{channel_name}/activity` | Returns daily posting activity for a specific channel. |
| `GET /api/search/messages?query=paracetamol` | Searches messages for a given keyword (e.g., product names or drug mentions). |

---

## ⚙️ Tech Stack

- **FastAPI** – For building the RESTful API
- **SQLAlchemy** – For database interaction
- **Pydantic** – For response validation
- **PostgreSQL** – As the backend data warehouse (dbt models)
- **Uvicorn** – ASGI server for local development
- **dotenv** – For environment variable management

---

---

## 🌐 Interactive API Docs

Once the app is running, you can access the interactive Swagger UI:

📍 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖼️ Screenshot

> Live preview of the FastAPI Swagger interface:

![Swagger UI Screenshot](https://drive.google.com/uc?id=1098iN2k3qS-BrR6cSe7tJzZHYrGwmdsi)

---

## 📦 Setup Instructions

1. **Install dependencies**:

   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv
````

2. **Create a `.env` file** (in `analytical-api/`):

   ```env
   POSTGRES_HOST=localhost
   POSTGRES_DB=telegram_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   PG_PORT=5432
   ```

3. **Run the API server**:

   ```bash
   uvicorn main:app --reload
   ```

---

## ✅ Task Completion

This application fulfills **Task 4 – Build an Analytical API** requirements:

* Analytical endpoints based on dbt marts
* PostgreSQL + FastAPI integration
* Validated responses using Pydantic
* Swagger documentation auto-generated

---