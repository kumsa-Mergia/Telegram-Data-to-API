from dagster import op

@op
def run_dbt_transformations():
    import subprocess
    subprocess.run(["dbt", "build"], cwd="dbt/telegram_warehouse", check=True)
