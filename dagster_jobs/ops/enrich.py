from dagster import op

@op
def run_yolo_enrichment():
    import subprocess
    subprocess.run(["python", "../../notebooks/yolo_enrichment.py"], check=True)
