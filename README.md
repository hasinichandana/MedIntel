# MedIntel: Hospital Medicine Demand Analytics

**MedIntel** is a data-driven hospital medicine analytics platform designed to analyze historical medicine consumption, identify usage patterns, group medicines using clustering, and explore future demand through machine-learning models.

The project combines data warehousing, data preprocessing, machine learning, and an interactive web dashboard to support medicine-demand analysis and inventory-planning research.

## 🌐 Live Demo

**Dashboard:** https://medintel-ojfo.onrender.com/dashboard

**API Documentation:** https://medintel-ojfo.onrender.com/docs

> Note: The application is hosted on Render's free service, which may spin down after inactivity and take additional time to respond to the first request.

## ✨ Features

- **Consumption Analytics:** Explore estimated medicine consumption across months and medicines.
- **Medicine Insights:** Inspect medicine-level information and consumption patterns.
- **K-Means Clustering:** Group medicines into four clusters using consumption, cost, and prescription-activity features.
- **Demand Forecasting:** Experiment with machine-learning models to estimate next-month medicine demand.
- **High-Demand Classification:** Analyze records classified as potentially high demand.
- **Model Evaluation:** Examine forecasting and classification evaluation data.
- **Interactive Dashboard:** Navigate through analytics, clustering, evaluation, and data-exploration sections.
- **REST API:** Access dashboard data through FastAPI endpoints.

## 🛠️ Technology Stack

| Component | Technologies |
|---|---|
| Programming | Python, JavaScript, HTML, CSS |
| Backend | FastAPI, Uvicorn |
| Data processing | Pandas, NumPy |
| Machine learning | Scikit-learn |
| Visualization | Chart.js |
| Development | Google Colab, Visual Studio Code |
| Version control | Git, GitHub |
| Deployment | Render |

## 🏗️ Project Structure

```text
MedIntel_Project/
├── backend/
│   └── main.py
├── frontend/
│   └── index.html
├── data/
│   ├── drug_master.csv
│   ├── monthly_consumption.csv
│   ├── kmeans_results.csv
│   ├── kmeans_cluster_summary.csv
│   ├── forecast_evaluation.csv
│   └── high_demand_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset Overview

The project uses hospital-related prescription, medicine, admission, department, and disease data for analysis.

The processed dataset contains:

- **73,109** prescription records.
- **250** distinct medicines.
- **45,000** admission records.
- **11** departments.
- **20** disease categories.
- **72 months** of data, from January 2020 through December 2025.

The derived fact table combines medicine, time, department, and disease information for analytical queries.

### Estimated Consumption

The project derives estimated medicine quantity from prescription dosage, frequency, and duration. Therefore, the consumption values represent calculated estimates based on the available prescription data, not independently verified physical stock usage.

## 🧠 Analytics and Machine Learning

### 1. Data Warehousing and OLAP

The project uses a fact table and dimension tables to organize medicine-related information for multidimensional analysis.

The analytical dimensions include:

- Time
- Medicine
- Department
- Disease

This structure supports examining consumption across different periods and hospital categories.

### 2. K-Means Clustering

K-Means groups medicines into **four clusters** using features such as total quantity, total cost, and prescription count.

The resulting groups help explore similarities in medicine usage and cost patterns.

### 3. Association Rule Mining

The project explores Apriori association-rule mining to investigate possible co-occurrence patterns among medicines. The current experiments did not identify multi-item frequent itemsets at the tested support threshold, so no strong medicine-association patterns are claimed.

### 4. Demand Forecasting

The project evaluates models such as Histogram Gradient Boosting and Random Forest against simple historical-average baselines.

Forecast performance is assessed using:

- **MAE:** Mean Absolute Error
- **RMSE:** Root Mean Squared Error
- **WAPE:** Weighted Absolute Percentage Error

The current experiments show that demand forecasting remains challenging and that predictions may smooth out sudden changes in medicine usage.

### 5. High-Demand Classification

A classification experiment identifies records that meet a medicine-specific high-demand threshold.

Model performance is examined using precision, recall, F1-score, and ROC-AUC. These metrics help assess how well the model identifies potentially high-demand periods.

The results are experimental and should not be interpreted as confirmed stockout alerts.

## 🚀 Run MedIntel Locally

### Prerequisites

- Python 3.10 or later
- Git
- Visual Studio Code or another code editor

### 1. Clone the repository

```bash
git clone https://github.com/hasinichandana/MedIntel.git
cd MedIntel
```


### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend

Run this command from the project root:

```bash
python -m uvicorn backend.main:app --reload
```

### 5. Open the application

- Dashboard: http://127.0.0.1:8000/dashboard
- API documentation: http://127.0.0.1:8000/docs
- API summary: http://127.0.0.1:8000/api/summary
- Monthly consumption: http://127.0.0.1:8000/api/monthly-consumption

Keep the backend terminal running while using the dashboard.

## 🔌 API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Application status |
| `/api/summary` | Overall project statistics |
| `/api/medicines` | Medicine data |
| `/api/monthly-consumption` | Monthly consumption data |
| `/api/clusters` | Cluster summary |
| `/api/cluster-medicines` | Medicine clustering results |
| `/api/forecast-evaluation` | Forecast evaluation records |
| `/api/high-demand` | High-demand classification records |
| `/dashboard` | Interactive dashboard |
| `/docs` | Interactive API documentation |

## 📈 Current Project Scope and Limitations

- Consumption is estimated from prescription information.
- Forecasting and classification are experimental analytical models.
- The current dataset does not independently establish actual stock-on-hand, supplier lead times, or confirmed stockout events.
- The dashboard is intended for academic analysis and demonstration, not as a validated clinical or inventory-control system.
- Model results should be reviewed and validated before any operational use.

## 🔮 Future Enhancements

- Improve forecast accuracy and detect sudden demand spikes.
- Add configurable demand-risk thresholds.
- Introduce authenticated user access and role-based permissions.
- Add richer department and disease analytics.
- Integrate validated stock-on-hand and supplier lead-time data.
- Add automated model retraining and monitoring.
- Improve dashboard accessibility and responsive design.

## 👩‍💻 Development Workflow

The project uses Google Colab for data processing and machine-learning experiments, Visual Studio Code for full-stack development, GitHub for version control, and Render for hosting.

When updating the live application, commit and push changes to GitHub. Render can deploy the latest commit when automatic deployment is enabled.

## ⚠️ Data and Privacy

Before sharing or redistributing any dataset, confirm that you have permission to publish it. Do not commit patient-identifiable information, confidential hospital records, passwords, API keys, or other sensitive information to a public repository.

## 📄 License

No license has been specified yet. All rights and permissions remain with the respective copyright holders unless a license is added to the repository.

---

**MedIntel: Turning historical medicine data into actionable analytical insights.**