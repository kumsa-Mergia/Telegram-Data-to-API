from dagster import op

@op
def load_raw_to_postgres(path: str):
    print(f"📥 Loading data from: {path}")
    import subprocess
    subprocess.run(["python", "script/load_json_to_postgres.py"], check=True)
