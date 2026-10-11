from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import pandas as pd

app = FastAPI(
    title="MedIntel API",
    description="Hospital Medicine Demand Analytics",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Local project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
FRONTEND_FILE = PROJECT_DIR / "frontend" / "index.html"


def load_csv(filename):
    path = DATA_DIR / filename

    if not path.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Missing data file: {filename}. Expected location: {path}"
        )

    try:
        return pd.read_csv(path)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Could not read {filename}: {str(exc)}"
        )


@app.get("/")
def home():
    return {
        "project": "MedIntel",
        "status": "running",
        "docs": "/docs",
        "dashboard": "/dashboard"
    }


@app.get("/api/summary")
def summary():
    drugs = load_csv("drug_master.csv")
    monthly = load_csv("monthly_consumption.csv")
    clusters_df = load_csv("kmeans_cluster_summary.csv")

    required_columns = {
        "drug_master.csv": ["drug_id"],
        "monthly_consumption.csv": ["quantity", "month"],
        "kmeans_cluster_summary.csv": ["cluster"]
    }

    dataframes = {
        "drug_master.csv": drugs,
        "monthly_consumption.csv": monthly,
        "kmeans_cluster_summary.csv": clusters_df
    }

    for filename, columns in required_columns.items():
        missing = [
            column for column in columns
            if column not in dataframes[filename].columns
        ]

        if missing:
            raise HTTPException(
                status_code=500,
                detail=f"{filename} is missing columns: {missing}"
            )

    return {
        "total_medicines": int(drugs["drug_id"].nunique()),
        "total_estimated_quantity": float(monthly["quantity"].sum()),
        "months_covered": int(monthly["month"].nunique()),
        "cluster_count": int(clusters_df["cluster"].nunique())
    }


@app.get("/api/medicines")
def medicines():
    df = load_csv("drug_master.csv")
    return df.fillna("").to_dict(orient="records")


@app.get("/api/monthly-consumption")
def monthly_consumption():
    df = load_csv("monthly_consumption.csv")

    required_columns = ["month", "quantity"]
    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise HTTPException(
            status_code=500,
            detail=f"monthly_consumption.csv is missing columns: {missing}"
        )

    result = (
        df.groupby("month", as_index=False)["quantity"]
        .sum()
        .sort_values("month")
    )

    return result.fillna("").to_dict(orient="records")


@app.get("/api/clusters")
def clusters():
    df = load_csv("kmeans_cluster_summary.csv")
    return df.fillna("").to_dict(orient="records")


@app.get("/api/cluster-medicines")
def cluster_medicines():
    df = load_csv("kmeans_results.csv")
    return df.fillna("").to_dict(orient="records")


@app.get("/api/forecast-evaluation")
def forecast_evaluation():
    df = load_csv("forecast_evaluation.csv")

    return {
        "rows": int(len(df)),
        "columns": df.columns.tolist(),
        "sample": df.head(20).fillna("").to_dict(orient="records")
    }


@app.get("/api/high-demand")
def high_demand():
    df = load_csv("high_demand_data.csv")

    return {
        "rows": int(len(df)),
        "columns": df.columns.tolist(),
        "sample": df.head(20).fillna("").to_dict(orient="records")
    }


@app.get("/dashboard", include_in_schema=False)
def dashboard():
    if not FRONTEND_FILE.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Dashboard file not found: {FRONTEND_FILE}"
        )

    return FileResponse(
        path=FRONTEND_FILE,
        media_type="text/html"
    )
