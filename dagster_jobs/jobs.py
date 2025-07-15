from dagster import job
from dagster_jobs.ops.scrape import scrape_telegram_data
from dagster_jobs.ops.load import load_raw_to_postgres
from dagster_jobs.ops.transform import run_dbt_transformations
from dagster_jobs.ops.enrich import run_yolo_enrichment

@job
def telegram_data_enrichment_job():
    path = scrape_telegram_data()
    load_raw_to_postgres(path)
    run_dbt_transformations()
    run_yolo_enrichment()
