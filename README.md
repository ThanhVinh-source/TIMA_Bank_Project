<div align="center">

# TIMA Bank Credit Risk Analytics Project

### *An end-to-end credit-risk analytics pipeline from CRM data to SQL Server and Power BI*

<h3>🏦 💳 📈 🧹 🧠 🗂️ 🚀</h3>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" />
</p>

<p>
  <img src="https://img.shields.io/badge/scikit--learn-ML%20Models-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat-square" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-Statistical%20Charts-4C72B0?style=flat-square" alt="Seaborn" />
</p>

<p>
  <img src="https://img.shields.io/badge/SQL%20Server-Data%20Warehouse-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/Papermill-Automated%20Notebooks-4B8BBE?style=flat-square" alt="Papermill" />
</p>

<br />

*From raw CRM lending records to cleaned analytical data, risk insights, predictive models, SQL Server tables, and an interactive Power BI dashboard.*

<p>
  <b>🏦 Credit Portfolio</b> &nbsp;•&nbsp;
  <b>🧹 Data Cleaning</b> &nbsp;•&nbsp;
  <b>📊 Exploratory Analytics</b> &nbsp;•&nbsp;
  <b>🧠 Predictive Modeling</b> &nbsp;•&nbsp;
  <b>🗂️ Star Schema</b> &nbsp;•&nbsp;
  <b>📈 Power BI</b>
</p>

<p>
  <a href="https://app.powerbi.com/view?r=eyJrIjoiZDZlZWRmZDMtNGU3Yy00YjMyLTk3MWEtMzNjMDkxZmYwZTU3IiwidCI6IjM3MGZiM2I4LTMzMDYtNDg5MC05MDYzLWNjMDhiZTc4ODI1NyIsImMiOjEwfQ%3D%3D">
    <img src="https://img.shields.io/badge/View%20Published%20Power%20BI%20Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="View Published Power BI Dashboard" />
  </a>
</p>

</div>

---

## Project Overview

An end-to-end data analytics and predictive modeling project for TIMA loan data. The project turns raw CRM lending records into a cleaned analytical dataset, explores customer and loan behavior, builds a dimensional data model, compares machine learning approaches for credit risk classification, and publishes the BI-ready outputs into SQL Server for Power BI reporting.

The work is designed to answer practical lending questions:

- 🧑‍💼 Who are TIMA's core borrowers?
- 💰 Which products drive loan volume and disbursement value?
- ⚠️ Which customer, product, income, geography, and credit-history signals are associated with late payment or bad debt?
- 👥 Which customer segments show a higher observed Risk rate?
- 🤖 Can historical loan information support an early-warning credit risk model?
- 🗂️ How can the cleaned data be reshaped into fact and dimension tables for BI reporting?
- 🔁 How can the refresh flow be automated from notebooks to SQL Server and Power BI?

## Table of Contents

- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Repository Structure](#repository-structure)
- [Dataset Overview](#dataset-overview)
- [Dataset Note](#dataset-note)
- [Notebook Guide](#notebook-guide)
- [Data Pipeline](#data-pipeline)
- [How to Run](#how-to-run)
- [Analytical Themes](#analytical-themes)
- [Modeling Approach](#modeling-approach)
- [Key Findings](#key-findings)
- [Automated Pipeline, SQL Server, and Power BI](#automated-pipeline-sql-server-and-power-bi)
- [Dimensional Model](#dimensional-model)
- [Power BI Dashboard](#power-bi-dashboard)
- [Dependencies](#dependencies)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)

## Project Highlights

| Area | What this project does |
| --- | --- |
| Data understanding | Profiles raw CRM loan data, data types, missing values, duplicates, and inconsistent formats. |
| Data cleaning | Converts dates, monetary values, gender flags, salary, bad debt flags, and late payment flags into analytical formats. |
| Feature engineering | Creates age groups, loan term, processing days, loan-to-income ratio, credit score group, income bracket, disbursement gap, repayment ratio, and standardized loan status. |
| Exploratory analysis | Studies loan amount, requested amount, product mix, loan status, demographics, geography, income, occupation, residence type, and risk variables. |
| Risk analysis | Examines how LoanStatus changes across products, cities, age groups, gender, salary brackets, occupations, residence types, credit score groups, bad debt history, and late payment history. |
| Predictive modeling | Compares Logistic Regression, Random Forest, and XGBoost models for multi-class risk labels and binary Risk/Safety classification. |
| BI-ready data model | Exports fact and dimension tables for reporting, dashboards, and further analytics. |
| Automated pipeline | Uses `scripts/run_pipeline.py` to execute the notebook pipeline, rebuild output tables, and load them into SQL Server. |
| SQL Server delivery | Writes the final `Dim_*` and `Fact_Loans` tables to the configured SQL Server schema. |
| Power BI dashboard | Includes a Power BI report file connected to the dimensional model for portfolio, risk, product, and geography reporting. |

## Repository Structure

```text
TIMA_Bank_Project/
├── data/
│   ├── bronze/
│   │   └── Tima_CRM - Data.csv
│   ├── silver/
│   │   ├── tima_cleaned_data_v1.csv
│   │   └── tima_cleaned_with_clusters.csv
│   └── gold/
│       ├── dim_fact_table/
│       │   ├── dim/
│       │   │   ├── Dim_Customer.csv
│       │   │   ├── Dim_Date.csv
│       │   │   ├── Dim_Geography.csv
│       │   │   ├── Dim_Geography2.csv
│       │   │   └── Dim_Product.csv
│       │   └── fact/
│       │       └── Fact_Loans.csv
│       └── semantic_model/
│           └── powerbi/
│               ├── TIMA_Data analysis dashboard.pbip
│               ├── TIMA_Data analysis dashboard.Report/
│               └── TIMA_Data analysis dashboard.SemanticModel/
├── notebook/
│   ├── data_understanding.ipynb
│   ├── data_cleaning_preprocessing.ipynb
│   ├── data_analysis_and_predictive_modeling.ipynb
│   └── create_dim_fact_table.ipynb
├── runs/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning_preprocessing.ipynb
│   └── 03_create_dim_fact_table.ipynb
├── scripts/
│   └── run_pipeline.py
├── Dashboard/
│   └── TIMA_Data analysis dashboard.pbix
├── docker-compose.yml
├── .env.example
├── .gitignore
├── environment.yml
├── requirements.txt
└── README.md
```

## Dataset Overview

The project works with TIMA CRM loan records. The cleaned analytical file contains approximately 2.3K loan records and 55 columns after preprocessing and feature engineering.

### Main data files

| File | Description |
| --- | --- |
| `data/bronze/Tima_CRM - Data.csv` | Raw CRM export with customer, loan, product, location, income, credit, and repayment fields. |
| `data/silver/tima_cleaned_data_v1.csv` | Cleaned and enriched analytical dataset used for EDA and modeling. |
| `data/silver/tima_cleaned_with_clusters.csv` | Analytical dataset with K-Means customer cluster labels. |
| `data/gold/dim_fact_table/fact/Fact_Loans.csv` | Loan-level fact table for the Data Warehouse and Semantic Model. |
| `data/gold/dim_fact_table/dim/Dim_Customer.csv` | Customer dimension with demographic, job, income, and risk attributes. |
| `data/gold/dim_fact_table/dim/Dim_Product.csv` | Product dimension with credit product and interest payment type. |
| `data/gold/dim_fact_table/dim/Dim_Date.csv` | Date dimension generated from application dates. |
| `data/gold/dim_fact_table/dim/Dim_Geography.csv` | Geography dimension at city and district level. |
| `data/gold/dim_fact_table/dim/Dim_Geography2.csv` | Simplified geography dimension at city level. |

### Automation and reporting files

| File | Description |
| --- | --- |
| `scripts/run_pipeline.py` | Runs the notebook pipeline with Papermill, reloads dimensional CSV outputs into SQL Server, and optionally triggers a Power Automate refresh webhook. |
| `Dashboard/TIMA_Data analysis dashboard.pbix` | Power BI dashboard file built on top of the project outputs. |

### Important original fields

| Field | Meaning |
| --- | --- |
| `LoanID` | Unique loan identifier. |
| `CardNumber` | Customer identity key used for customer-level grouping. |
| `application_date` | Date when the customer applied for the loan. |
| `FromDate`, `ToDate` | Loan period start and end dates. |
| `Số tiền đăng ký vay ban đầu` | Initial requested loan amount. |
| `Tiền giải ngân` | Disbursed loan amount. |
| `Tiền gốc còn lại` | Remaining principal balance. |
| `Trạng thái` | Original loan status from the CRM system. |
| `TS_CREDIT_SCORE_V2` | Internal credit score. |
| `ProductCreditName` | Loan product type. |
| `Salary` | Customer income. |
| `JobName` | Customer occupation. |
| `CityName`, `DistrictName` | Customer geography. |
| `HasBadDebt` | Whether the customer has bad debt history. |
| `HasLatePayment` | Whether the customer has late payment history. |
| `LongestOverdue` | Longest overdue period recorded. |

### Engineered fields

| Field | Description |
| --- | --- |
| `Age` | Customer age calculated from birthday and application date. |
| `AgeGroup` | Age bucket such as `18-25`, `26-35`, `36-45`, and older groups. |
| `LoanTermMonths` | Loan duration in months. |
| `ProcessingDays` | Days between application date and loan start date. |
| `LoanToIncomeRatio` | Requested loan amount divided by monthly salary. |
| `Cần Giải Ngân` | Requested amount minus disbursed amount. |
| `Đã trả/khoản vay đã giải ngân` | Remaining principal divided by disbursed amount. |
| `LowCreditScore` | Binary flag for credit scores below 600. |
| `CreditScoreGroup` | Credit score bucket: Low, Medium, Good, Excellent. |
| `IncomeBracket` | Salary bucket: `<5m`, `5-10m`, `10-15m`, `15-25m`, `>=25m`. |
| `LoanStatus` | Standardized business status: `Hoàn thành`, `Muộn`, `Nợ xấu`, `Đang vay`. |
| `CustomerCluster` | K-Means cluster id generated in the modeling notebook. |
| `CustomerClusterLabel` | Human-readable K-Means cluster label such as `Cluster 0` and `Cluster 1`. |

<a id="dataset-note"></a>

## ⚠️ Dataset Note

> ⚠️ This dataset is used only for learning, analysis, and project demonstration purposes. It is not a production dataset from a real business environment.

Any personal-looking information in the files, such as customer names, card numbers, phone numbers, addresses, company names, income values, and family contact fields, should be understood as sample project data. These details do not represent real individuals and should not be interpreted as actual customer information.

## Notebook Guide

Run the notebooks in this order for the clearest project flow.

| Order | Notebook | Purpose |
| --- | --- | --- |
| 1 | `notebook/data_understanding.ipynb` | Loads the raw CRM file, checks shape, data types, missing values, duplicate records, and performs first-stage cleaning. |
| 2 | `notebook/data_cleaning_preprocessing.ipynb` | Builds analytical features, creates loan status labels, checks final nulls, and exports the cleaned dataset. |
| 3 | `notebook/data_analysis_and_predictive_modeling.ipynb` | Performs EDA, K-Means customer segmentation, risk modeling, hybrid modeling, AUC evaluation, and feature importance analysis. |
| 4 | `notebook/create_dim_fact_table.ipynb` | Converts the cleaned flat dataset into BI-friendly fact and dimension tables. |

For production-style refreshes, `scripts/run_pipeline.py` automates notebooks 1, 2, and 4, then pushes the final dimensional tables into SQL Server. The modeling notebook remains an analytical notebook and is not part of the automated SQL Server load.

## Data Pipeline

```mermaid
flowchart LR
    A["Bronze<br/>Raw CRM data"] --> B["Data understanding<br/>types, nulls, duplicates"]
    B --> C["Silver<br/>cleaning and preprocessing"]
    C --> D["Feature engineering<br/>risk, income, age, loan behavior"]
    D --> E["Silver dataset<br/>tima_cleaned_data_v1.csv"]
    E --> F["EDA, K-Means segmentation<br/>and predictive modeling"]
    F --> M["Clustered Silver dataset<br/>tima_cleaned_with_clusters.csv"]
    E --> G["Gold dimensional model"]
    G --> H["Gold Dim/Fact CSV tables"]
    H --> I["run_pipeline.py<br/>automated delivery"]
    I --> J["SQL Server (Docker)<br/>Dim_* and Fact_Loans"]
    J --> K["Power BI Semantic Model<br/>PBIP/TMDL"]
    K --> N["Power BI dashboard<br/>PBIX/report visuals"]
    I -. optional webhook .-> L["Power Automate<br/>dataset refresh"]
    L -. refresh .-> N
```

## How to Run

### 1. Clone or open the project

```bash
cd "TIMA_Bank_Project"
```

### 2. Create a Python environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

Or using Conda:

```bash
conda env create -f environment.yml
conda activate tima-bank-credit-risk
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

Then open the notebooks from the `notebook/` directory and run them in the recommended order.

### 5. Start SQL Server with Docker

Requires Docker Desktop. This spins up SQL Server in a container and auto-creates the empty `TIMA_BI` database via an init step.

```bash
docker compose up -d
```

### 6. Run the automated SQL Server and Power BI pipeline

Before running the automated pipeline, make sure:

- The SQL Server container is running (`docker compose up -d`).
- `.env` contains `MSSQL_SA_PASSWORD` (host/port/user/database have sensible defaults).
- `pymssql` is installed (listed in requirements).

Run:

```bash
python scripts/run_pipeline.py
```

This command regenerates the Silver cleaned dataset and Gold dimensional outputs, loads the Gold Dim/Fact tables into SQL Server, and optionally triggers Power Automate for Power BI refresh.

### 7. Rebuild outputs manually

To regenerate the cleaned dataset and dimensional tables:

1. Run `notebook/data_understanding.ipynb`.
2. Run `notebook/data_cleaning_preprocessing.ipynb`.
3. Run `notebook/create_dim_fact_table.ipynb`.

To rerun the analysis and models:

1. Make sure `data/silver/tima_cleaned_data_v1.csv` exists.
2. Run `notebook/data_analysis_and_predictive_modeling.ipynb`.

## Analytical Themes

The analysis is organized around four major lenses.

### 1. Loan Core Fields

- Distribution of requested loan amounts and disbursed amounts.
- Difference between requested and approved/disbursed values.
- Outlier behavior in unusually large loan applications.
- Product-level loan count, total disbursement, and average disbursement.
- LoanStatus distribution and non-performing loan ratio.

### 2. Customer Demographics

- Gender distribution.
- Age distribution and age-group concentration.
- City-level borrower concentration.
- Residence type distribution and relationship with repayment behavior.

### 3. Income and Occupation

- Salary distribution and salary outliers.
- Common occupations in the borrower base.
- Loan size differences across income and occupation groups.
- Product preference by income bracket and job type.

### 4. Risk Variables

- Credit score distribution.
- Bad debt history rate.
- Late payment history rate.
- Relationship between risk variables and LoanStatus.
- Interaction effects such as credit score plus bad debt history, age plus income, and product plus income.

## Modeling Approach

The project contains four modeling components: unsupervised customer segmentation, a rule-based multi-class risk experiment, a behavior-based Risk/Safety model, and a hybrid model that adds K-Means signals to Random Forest.

### K-Means Customer Segmentation

K-Means is used to segment borrowers based on credit profile, affordability, product, job, residence type, geography, and borrowing behavior. The model uses standardized numeric variables and one-hot encoded categorical variables.

Selected features include:

- Credit and history: `TS_CREDIT_SCORE_V2`, `HasBadDebt`, `HasLatePayment`, `NumberOfLoans`.
- Affordability and loan behavior: `Salary`, `LoanToIncomeRatio`, `LoanTermMonths`, `Loan_log`.
- Customer profile: `Gender`, `AgeGroup`, `ProductCreditName`, `JobName`, `Hình thức cư trú`, `CityName`.

The K-Means result is weak for this dataset. The best `k` by silhouette score is `2`, but the highest silhouette score is only about `0.0795`. This very low score means the customer groups are not clearly separated in the feature space. In other words, K-Means does not discover strong natural clusters for this mixed credit-customer dataset.

Because of this, K-Means is retained only as an exploratory segmentation and customer-profiling tool. It should not be interpreted as a strong or definitive customer classification method for this project. The likely reason is that the data combines numerical credit variables with many one-hot encoded categorical variables, while K-Means relies on Euclidean distance and works best when clusters are compact and clearly separated.

| k | Silhouette score |
| ---: | ---: |
| 2 | 0.0795 |
| 3 | 0.0355 |
| 4 | 0.0412 |
| 5 | 0.0501 |
| 6 | 0.0596 |
| 7 | 0.0632 |
| 8 | 0.0595 |

Cluster size:

| Cluster | Records | Share |
| --- | ---: | ---: |
| Cluster 0 | 1,528 | 64.12% |
| Cluster 1 | 855 | 35.88% |

Observed repayment-risk profile, excluding active loans:

| Cluster | Observed records | Risk count | Risk rate | Avg credit score | Avg salary | Avg loan-to-income ratio |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Cluster 1 | 818 | 341 | 41.69% | 597.43 | 9,214,584 | 0.94 |
| Cluster 0 | 1,499 | 390 | 26.02% | 584.09 | 10,476,510 | 1.63 |

**High-risk customer persona from K-Means**

Even though K-Means does not produce well-separated clusters, the resulting segments can still be used for exploratory profiling. Cluster 1 has the highest observed `Risk` rate, where `Risk = Late + Non-Performing` and `Safety = Completed`.

| Attribute | Cluster 1 profile |
| --- | --- |
| Observed records | 818 |
| Risk rate | 41.69% |
| Main product | `Cầm cố xe máy` |
| Main job group | `Khác` |
| Main residence type | `Thuê` |
| Main income bracket | `5-10m` |
| Main credit score group | `Low (High Risk)` |
| Main city | `Hà Nội` |
| Average credit score | 597.43 |
| Average salary | 9,214,584 VND |
| Average loan-to-income ratio | 0.94 |
| Bad debt history rate | 10.88% |
| Late payment history rate | 14.55% |

Within Cluster 1, the most concentrated risk pockets are more specific than the cluster label itself:

- Product risk is highest for `Cầm cố Điện thoại` inside Cluster 1, with a 59.51% Risk rate, followed by `Vay theo sim` at 43.97%.
- Ho Chi Minh City borrowers inside Cluster 1 have a 55.27% Risk rate, higher than Hanoi at 36.38%.
- Rental residence (`Thuê`) is both common and risky inside Cluster 1, with a 53.07% Risk rate.
- The dominant customer shape is young working-age borrowers, mostly `18-35`, lower-middle income, low-to-medium credit score, and concentrated in Hanoi and Ho Chi Minh City.

The clustered dataset is exported as `data/silver/tima_cleaned_with_clusters.csv`.

### Track 1: Rule-Based Multi-Class Risk Level

The notebook creates a `Risk_Level` target from `TS_CREDIT_SCORE_V2` and `HasBadDebt`:

| Risk level | Rule |
| --- | --- |
| `Cao (High)` | Conservative fallback for cases that are not Medium or Low, including low credit scores and any bad debt history. |
| `Trung bình (Medium)` | Credit score from 500 to 700 and no bad debt. |
| `Thấp (Low)` | Credit score above 700 and no bad debt. |

**Feature set for Track 1**

These features are selected for the rule-based `Risk_Level` experiment. Since the target is defined from credit score and bad debt logic, the model is expected to learn the rule structure very strongly.

| Feature role | Selected features |
| --- | --- |
| Rule-driving credit variables | `TS_CREDIT_SCORE_V2`, `HasBadDebt` |
| Additional repayment history | `HasLatePayment`, `NumberOfLoans` |
| Financial capacity | `Salary`, `IncomeBracket`, `LoanToIncomeRatio` |
| Loan behavior | `Loan_log`, `LoanTermMonths` |
| Customer profile | `JobName`, `Hình thức cư trú`, `AgeGroup`, `Gender` |
| Product and geography | `ProductCreditName`, `CityName` |

`Loan_log` is created from `Tiền giải ngân` using `log1p` to reduce the impact of very large loan outliers. Categorical fields are one-hot encoded with `pd.get_dummies`, and numerical fields are scaled with `StandardScaler` before training.

Models compared:

- Multinomial Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Tuned Logistic Regression with `RandomizedSearchCV`
- Tuned Random Forest with `RandomizedSearchCV`
- Tuned XGBoost with `RandomizedSearchCV`

Important modeling note: this target is rule-based, and the same rule-driving fields are also included as features. Very high scores in this track mainly show that the models can reproduce the label rule. They should not be interpreted as proof of a fully independent credit-risk prediction system.

Selected observed results:

| Model | Test Accuracy | Test F1 Macro | Test AUC |
| --- | ---: | ---: | ---: |
| Logistic Regression | 0.9727 | 0.9569 | 0.9987 OvR macro |
| Random Forest | 0.9287 | 0.9328 | 0.9735 OvR macro |
| XGBoost Baseline | 1.0000 | 1.0000 | 1.0000 OvR macro |
| Logistic Regression - Tuned | 0.9727 | 0.9569 | 0.9987 OvR macro |
| Random Forest - Tuned | 0.9937 | 0.9864 | 1.0000 OvR macro |
| XGBoost - Tuned | 1.0000 | 1.0000 | 1.0000 OvR macro |

Top features in the tuned XGBoost rule-based model include:

- `TS_CREDIT_SCORE_V2`
- `HasBadDebt`
- `NumberOfLoans`
- `Gender`
- `Salary`
- `ProductCreditName`
- `CityName`
- `Loan_log`
- `LoanTermMonths`
- `LoanToIncomeRatio`

### Track 2: LoanStatus-Based Risk/Safety Classification

The second modeling approach uses observed repayment status:

| Group | Definition |
| --- | --- |
| `Risk` | `Late` or `Non-Performing` |
| `Safety` | `Completed` |

Ongoing loans (`Active`) are excluded from this binary target because the final repayment outcome is not yet known.

Observed class distribution:

| Class | Count |
| --- | ---: |
| Safety | 1,586 |
| Risk | 731 |

**Feature set for Track 2**

These features are selected for the observed repayment-behavior model. Unlike Track 1, this target comes from actual `LoanStatus` outcomes after removing ongoing loans.

| Feature role | Selected features |
| --- | --- |
| Credit history signals | `TS_CREDIT_SCORE_V2`, `HasBadDebt`, `HasLatePayment` |
| Borrowing history | `NumberOfLoans` |
| Affordability signals | `Salary`, `IncomeBracket`, `LoanToIncomeRatio` |
| Loan structure | `Loan_log`, `LoanTermMonths` |
| Product risk signals | `ProductCreditName` |
| Customer and location context | `JobName`, `Hình thức cư trú`, `AgeGroup`, `Gender`, `CityName` |

For this track, ongoing loans are removed before modeling, then the remaining loans are stratified into train/test sets so the `Risk` and `Safety` balance is preserved. The same preprocessing pattern is applied: one-hot encoding for categorical variables and `StandardScaler` for numerical variables.

Selected observed results:

| Model | Test Accuracy | Test F1 Macro | Test AUC |
| --- | ---: | ---: | ---: |
| Logistic Regression - Tuned | 0.7823 | 0.7609 | 0.8245 |
| Random Forest - Tuned | 0.7974 | 0.7784 | 0.8366 |
| XGBoost - Tuned | 0.7845 | 0.7622 | 0.8345 |

For the Risk/Safety target, the tuned Random Forest produced the strongest observed AUC. Its most important features include:

- `LoanTermMonths`
- `ProductCreditName_Vay theo sim`
- `Hình thức cư trú_Thuê`
- `Loan_log`
- `LoanToIncomeRatio`
- `TS_CREDIT_SCORE_V2`
- `NumberOfLoans`
- `CityName_Hồ Chí Minh`
- `Salary`
- `CityName_Hà Nội`

### Hybrid Model (K-Means + Random Forest)

The hybrid model adds K-Means-derived features to the supervised Risk/Safety classifier:

- One-hot cluster membership features such as `KMeansCluster_*`.
- Cluster-distance features such as `KMeansDistance_*`, which measure how close each customer is to each K-Means centroid.
- Original Risk/Safety features from Track 2.

The final hybrid classifier is a tuned Random Forest with balanced subsampling.

| Model | Test Accuracy | Test F1 Macro | Test Precision Risk | Test Recall Risk | Test AUC |
| --- | ---: | ---: | ---: | ---: | ---: |
| Random Forest | 0.7974 | 0.7784 | 0.6429 | 0.8014 | 0.8366 |
| Random Forest + K-Means | 0.7974 | 0.7765 | 0.6477 | 0.7808 | 0.8336 |

Top grouped feature importance for the hybrid model:

| Feature group | Importance |
| --- | ---: |
| `LoanTermMonths` | 0.6000 |
| `KMeansDistance` | 0.1433 |
| `ProductCreditName` | 0.0805 |
| `ResidenceType` | 0.0465 |
| `Loan_log` | 0.0286 |
| `TS_CREDIT_SCORE_V2` | 0.0238 |
| `LoanToIncomeRatio` | 0.0217 |
| `NumberOfLoans` | 0.0191 |

The conclusion is that K-Means does not work well as a clustering method for this dataset, based on the very low silhouette score. Its main value is limited exploratory profiling and risk interpretation, not strong segmentation or material improvement of the supervised Risk/Safety classifier.

### SHAP Model Explainability

SHAP is applied directly to the tuned Random Forest Risk/Safety model to explain predictions for the positive class, `Risk`. Unlike standard feature importance, SHAP shows both the overall strength of each feature and the direction in which feature values push predictions toward `Risk` or `Safety`.

The SHAP summary plots are computed from the full encoded test feature matrix, not from the previous top-20 feature-importance table. The top features shown in the SHAP plots are selected by mean absolute SHAP value.

**Global SHAP insights**

- `LoanTermMonths` is the strongest driver of the model's Risk/Safety decisions. It has the highest SHAP impact at both the individual-feature level and the grouped-feature level.
- Customer context variables also matter. After loan term, the strongest groups are `ResidenceType`, `ProductCreditName`, and `CityName`, showing that housing stability, loan product type, and borrower location help the model separate `Risk` from `Safety`.
- Traditional credit-profile variables such as `TS_CREDIT_SCORE_V2`, `HasLatePayment`, and `HasBadDebt` are still useful, but they are not the dominant signals in this behavior-based model. This differs from Track 1, where credit score and bad-debt history dominate because they are used to create the rule-based target.
- Grouping one-hot encoded variables makes the explanation more business-readable. For example, individual columns such as `ProductCreditName_Vay theo sim` and `Hình thức cư trú_Thuê` are aggregated back into `ProductCreditName` and `ResidenceType`.

Grouped SHAP importance for the tuned Random Forest:

| Feature group | MeanAbsSHAP |
| --- | ---: |
| `LoanTermMonths` | 0.2437 |
| `ResidenceType` | 0.0486 |
| `ProductCreditName` | 0.0400 |
| `CityName` | 0.0315 |
| `NumberOfLoans` | 0.0128 |
| `TS_CREDIT_SCORE_V2` | 0.0119 |
| `JobName` | 0.0110 |
| `LoanToIncomeRatio` | 0.0089 |
| `Loan_log` | 0.0078 |
| `Salary` | 0.0054 |
| `IncomeBracket` | 0.0033 |
| `AgeGroup` | 0.0007 |
| `Gender` | 0.0006 |
| `HasLatePayment` | 0.0005 |
| `HasBadDebt` | 0.0003 |

**Local SHAP example**

For one test customer, the actual label is `Safety`, and the model predicts a `Risk` probability of `0.3078`. Since this probability is below `0.50`, the model classifies the customer as more likely to be `Safety` than `Risk`.

The waterfall explanation starts from the model's average expected risk level, then shows how each feature increases or decreases the final predicted risk probability. Blue SHAP contributions decrease the predicted `Risk` probability, while red contributions increase it.

For this customer, the strongest risk-reducing factors are:

- `LoanTermMonths = 5`, reducing predicted risk by about `0.08`.
- Not being in the `Hình thức cư trú_Thuê` category, reducing predicted risk by about `0.05`.
- Being a `Nhân viên chính thức`, having `NumberOfLoans = 2`, not using the `Vay theo sim` product, and having a credit score of `692`, each pushing the prediction slightly toward `Safety`.

A few variables increase the predicted risk slightly, such as not being in `CityName_Hà Nội` and having a salary of `10,000,000`, but these effects are small compared with the risk-reducing factors. Overall, SHAP explains how the feature contributions reduce this customer's predicted risk from the average level to about `0.3078`, matching the actual `Safety` label.

Business interpretation: the model does not rely only on credit score or historical bad debt. Loan duration, product category, residence type, and location should also be monitored as early-warning indicators. SHAP explains the trained model's behavior, not direct causality.

## Key Findings

### Loan Size and Product Mix

- TIMA loans are heavily concentrated in the small consumer loan segment.
- Typical loans cluster around 5-10 million VND.
- The requested and disbursed amount distributions are strongly right-skewed.
- A small number of very large loans create a long tail and should be handled carefully in modeling.
- Phone pawning and motorcycle pawning dominate loan volume.
- Some high-value products have low frequency but high average disbursement.

### Loan Status and Repayment Risk

- `Hoàn thành` is the largest LoanStatus group, with 1,586 records.
- `Muộn` is also significant, with 525 records.
- `Nợ xấu` accounts for 206 records, giving an observed NPL ratio of about 8.64%.
- The late-loan group is important because it may represent future bad debt risk.

### Customer Profile

- The borrower base is concentrated in young working-age customers, especially the 26-35 age group.
- Male customers are the majority in the dataset.
- Customers are highly concentrated in Hanoi, with Ho Chi Minh City as the second major market.
- Salary is concentrated around lower-middle income bands, especially 5-10 million VND.

### Risk Segmentation

- Low credit score groups contain a much higher share of bad debt.
- Customers with prior bad debt history have a higher observed NPL rate than those without it.
- SIM-based loan products show elevated risk concentration compared with some collateralized products.
- Rental residence status and several unstable occupation groups show higher late or risky behavior.
- Loan size is driven by a combination of income, job stability, age, product type, and collateral value.
- K-Means has weak clustering quality in this dataset: the best silhouette score is only about 0.0795 at `k=2`, meaning the clusters are not clearly separated.
- Despite weak separation, Cluster 1 can still be used as an exploratory higher observed-risk segment, with a 41.69% Risk rate versus 26.02% for Cluster 0.
- The Cluster 1 persona is mainly lower-middle-income, low-credit-score, rental-residence borrowers, concentrated in Hanoi and Ho Chi Minh City.
- The hybrid Random Forest + K-Means model does not outperform the tuned Random Forest baseline overall, but K-Means distance features still rank as the second most important feature group. This makes segmentation useful for explanation and monitoring, even when it does not materially improve predictive performance.

## Automated Pipeline, SQL Server, and Power BI

The project includes `scripts/run_pipeline.py` for a repeatable refresh flow from source data to BI consumption.

### What the pipeline does

1. Executes the core notebook workflow with Papermill:
   - `notebook/data_understanding.ipynb`
   - `notebook/data_cleaning_preprocessing.ipynb`
   - `notebook/create_dim_fact_table.ipynb`
2. Stores executed notebook copies in `runs/` for audit/debugging.
3. Reads the final Gold CSV outputs from `data/gold/dim_fact_table/`.
4. Validates key table quality rules:
   - `Fact_Loans.LoanID` must not contain null values.
   - `Dim_Customer.CardNumber` must be unique.
5. Loads all final tables into SQL Server through `sqlalchemy` and `pymssql`.
6. Optionally calls a Power Automate webhook to refresh the Power BI dataset/report after SQL Server has been updated.

### SQL Server output tables

The pipeline writes these tables to the schema defined by `SQL_SCHEMA`:

| SQL Server table | Source CSV |
| --- | --- |
| `Dim_Customer` | `data/gold/dim_fact_table/dim/Dim_Customer.csv` |
| `Dim_Product` | `data/gold/dim_fact_table/dim/Dim_Product.csv` |
| `Dim_Date` | `data/gold/dim_fact_table/dim/Dim_Date.csv` |
| `Dim_Geography` | `data/gold/dim_fact_table/dim/Dim_Geography.csv` |
| `Dim_Geography2` | `data/gold/dim_fact_table/dim/Dim_Geography2.csv` |
| `Fact_Loans` | `data/gold/dim_fact_table/fact/Fact_Loans.csv` |

During each run, the script first creates `stg_*` tables, then replaces the final tables with the refreshed versions. Because this is a full-refresh load, make sure the target schema is dedicated to this project or that replacing these tables is acceptable.

### Required `.env` settings

Create a local `.env` file in the project root.

```env
# Copy from .env.example. MSSQL_SA_PASSWORD must match the one in docker-compose.yml
MSSQL_SA_PASSWORD=your_strong_password
MSSQL_HOST=localhost
MSSQL_PORT=1433
MSSQL_USER=sa
MSSQL_DATABASE=TIMA_BI
SQL_SCHEMA=dbo
PAPERMILL_KERNEL=python3
POWER_AUTOMATE_REFRESH_URL=
```

## Dimensional Model

The project exports a simple star-schema-style model for BI tools.

```mermaid
erDiagram
    Dim_Customer ||--o{ Fact_Loans : "CardNumber"
    Dim_Product ||--o{ Fact_Loans : "ProductCreditName"
    Dim_Date ||--o{ Fact_Loans : "application_date"
    Dim_Geography2 ||--o{ Fact_Loans : "CityName"
    Dim_Geography2 ||--o{ Dim_Geography : "CityName"

    Dim_Customer {
        string CardNumber
        string FullName
        string Gender
        string AgeGroup
        string JobName
        float Salary
        string CreditScoreGroup
        string IncomeBracket
        int HasBadDebt
    }

    Dim_Product {
        string ProductCreditName
        string InterestPaymentType
    }

    Dim_Date {
        date Date
        int Year
        string Quarter
        int MonthNum
        string MonthName
        int Day
        string DayOfWeek
    }

    Dim_Geography {
        string CityName
        string DistrictName
    }

    Dim_Geography2 {
        string CityName
    }

    Fact_Loans {
        int LoanID
        string CardNumber
        string ProductCreditName
        date application_date
        string CityName
        float requested_amount
        float disbursed_amount
        float remaining_principal
        int LongestOverdue
        int LoanTermMonths
        float LoanToIncomeRatio
        int HasLatePayment
        int HasBadDebt
        string LoanStatus
    }
```

This model supports reporting questions such as:

- Loan volume by month, quarter, city, product, or customer segment.
- Disbursement value by product and geography.
- NPL ratio by product, city, occupation, income bracket, and credit score group.
- Late payment exposure by loan term and loan-to-income ratio.

Geography is provided in two levels:

- `Dim_Geography.csv`: city and district lookup for more detailed geographic analysis.
- `Dim_Geography2.csv`: city-only lookup, which matches the `CityName` field stored in `Fact_Loans.csv`.

## Power BI Dashboard

The repository includes the Power BI report file:

```text
Dashboard/TIMA_Data analysis dashboard.pbix
```

Use this file in Power BI Desktop to review the dashboard, update data-source settings, refresh visuals, and publish to Power BI Service. The expected reporting layer is the SQL Server dimensional model produced by the pipeline:

- `Dim_Customer`
- `Dim_Product`
- `Dim_Date`
- `Dim_Geography` and `Dim_Geography2`
- `Fact_Loans`

Recommended Power BI refresh flow:

1. Run `python scripts/run_pipeline.py`.
2. Confirm the refreshed tables are available in SQL Server.
3. Open or publish `Dashboard/TIMA_Data analysis dashboard.pbix`.
4. Configure the Power BI data source to the same SQL Server database/schema.
5. Refresh manually in Power BI Desktop or use the optional Power Automate webhook for Power BI Service refresh.

## Dependencies

The notebooks use the Python libraries listed in `requirements.txt` and `environment.yml`

The notebook metadata shows a Python 3 kernel. Python 3.10+ is recommended. The automated SQL Server load connects through `pymssql`. SQL Server itself runs in Docker (see `docker-compose.yml`); Docker Desktop is required to start it.

## Limitations

- The dataset is relatively small, with about 2.3K loan records.
- Geographic coverage is highly concentrated, especially in Hanoi, which limits generalization to other markets.
- Some fields have missing or inconsistent values in the raw CRM extract.
- Some very large loan amounts behave as outliers and can strongly influence averages and models.
- The multi-class `Risk_Level` target is rule-based and partially derived from variables used as model inputs.
- The binary Risk/Safety model is more behavior-based, but still needs additional validation before operational use.
- K-Means segmentation is not effective for discovering clearly separated customer groups in this dataset. The highest silhouette score is only about 0.0795 at `k=2`, so the clusters should be treated as exploratory profiles rather than reliable natural customer classes.
- The hybrid Random Forest + K-Means model adds interpretability through segment-distance features, but it does not outperform the tuned Random Forest baseline overall.
- Ongoing loans are excluded from the Risk/Safety target because their final outcome is not yet known.
- A reusable preprocessing pipeline with `sklearn.pipeline` has not yet been implemented.

## Project Summary

This project moves from raw lending operations data to business-ready credit analytics. It cleans and enriches TIMA CRM records, identifies borrower and product risk patterns, builds predictive models, exports a BI-ready dimensional structure, loads it into SQL Server, and connects it to Power BI. The result is a practical foundation for credit portfolio monitoring, customer segmentation, risk warning, and dashboard-driven decision making.
