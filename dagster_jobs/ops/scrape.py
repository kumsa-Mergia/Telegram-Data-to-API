from dagster import op, Out, Output

@op(out=Out(str))
def scrape_telegram_data():
    raw_path = "data/raw/2025-07-10"
    # your scraping logic...
    return raw_path
