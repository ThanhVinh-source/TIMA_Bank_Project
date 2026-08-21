from pathlib import Path
import os
import papermill as pm
import pandas as pd
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.types import NVARCHAR

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env", override=True)

NOTEBOOKS = [
    "data_understanding.ipynb",
    "data_cleaning_preprocessing.ipynb",
    "create_dim_fact_table.ipynb",
]

FILES = {
    "Dim_Customer": ROOT / "data/gold/dim_fact_table/dim/Dim_Customer.csv",
    "Dim_Product": ROOT / "data/gold/dim_fact_table/dim/Dim_Product.csv",
    "Dim_Date": ROOT / "data/gold/dim_fact_table/dim/Dim_Date.csv",
    "Dim_Geography": ROOT / "data/gold/dim_fact_table/dim/Dim_Geography.csv",
    "Dim_Geography2": ROOT / "data/gold/dim_fact_table/dim/Dim_Geography2.csv",
    "Fact_Loans": ROOT / "data/gold/dim_fact_table/fact/Fact_Loans.csv",
}

DATES = {
    "Dim_Customer": ["Birthday"],
    "Dim_Date": ["Date"],
    "Fact_Loans": ["application_date"],
}

def run_notebooks():
    run_dir = ROOT / "runs"
    run_dir.mkdir(exist_ok=True)
    for i, nb in enumerate(NOTEBOOKS, start=1):
        pm.execute_notebook(
            input_path=str(ROOT / "notebook" / nb),
            output_path=str(run_dir / f"{i:02d}_{nb}"),
            cwd=str(ROOT / "notebook"),
            kernel_name=os.getenv("PAPERMILL_KERNEL", "python3"),
            log_output=True,
        )

def load_sqlserver():
    url = URL.create(
        "mssql+pymssql",
        username=os.getenv("MSSQL_USER", "sa"),
        password=os.environ["MSSQL_SA_PASSWORD"],
        host=os.getenv("MSSQL_HOST", "localhost"),
        port=int(os.getenv("MSSQL_PORT", "1433")),
        database=os.getenv("MSSQL_DATABASE", "TIMA_BI"),
        query={"charset": "utf8"},
    )
    engine = create_engine(url)
    schema = os.getenv("MSSQL_SCHEMA", "dbo")

    tables = {}
    for table, path in FILES.items():
        df = pd.read_csv(path, encoding="utf-8-sig")
        for col in DATES.get(table, []):
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        if df.empty:
            raise ValueError(f"{table} is empty")
        tables[table] = df

    if tables["Fact_Loans"]["LoanID"].isna().any():
        raise ValueError("Fact_Loans has null LoanID")
    if not tables["Dim_Customer"]["CardNumber"].is_unique:
        raise ValueError("Dim_Customer.CardNumber must be unique")

    for table, df in tables.items():
        dtype = {
            col: NVARCHAR(length=4000)
            for col in df.select_dtypes(include=["object", "string"]).columns
        }
        
        df.to_sql(
            f"stg_{table}",
            engine,
            schema=schema,
            if_exists="replace",
            index=False,
            chunksize=1000,
            dtype=dtype,
        )

    with engine.begin() as con:
        for table in tables:
            con.execute(text(f"DROP TABLE IF EXISTS [{schema}].[{table}]"))
            con.execute(text(f"EXEC sp_rename '{schema}.stg_{table}', '{table}'"))

    print("Loaded tables:", ", ".join(tables.keys()))

def trigger_power_automate():
    url = os.getenv("POWER_AUTOMATE_REFRESH_URL")
    if not url:
        print("SQL loaded. Run Power Automate refresh flow manually.")
        return
    r = requests.post(url, json={"source": "tima-pipeline"})
    r.raise_for_status()
    print("Power Automate refresh triggered.")

if __name__ == "__main__":
    run_notebooks()
    load_sqlserver()
    trigger_power_automate()