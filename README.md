# health-intelligence-dashboard
An executive-level financial and clinical dashboard for hospital readmission analysis, featuring Looker Studio integration and automated revenue cycle metrics.

# Project 3: The "Health Intelligence" Dashboard

## 🎯 Goal
To provide clinical and financial leadership with a visual "end product" that identifies bottlenecks in revenue collection and hospital readmission patterns.

## 📊 Live Dashboard
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vyncura/health-intelligence-dashboard/blob/main/The_Health_Intelligence_Dashboard.ipynb)

## 🛠️ Tech Stack
- **Python/Pandas:** Data simulation and cleaning.
- **Plotly:** Interactive exploratory analysis.
- **Looker Studio:** Final executive dashboard.
- **GitHub:** Project versioning and documentation.

## 🔍 Key Insights
- **Revenue Capture:** Analysis of Billed vs. Collected amounts.
- **Denial Analysis:** Identifying the top 5 reasons for claim denials to improve billing workflows.
- **Payer Performance:** Tracking 'Days in A/R' to optimize cash flow.

## 🚀 How to Run
1. Clone this repo.
2. Open the `.ipynb` notebook in Google Colab.
3. Run all cells to see the interactive Plotly visualizations.

## Project Documentation (README) Template

## 🏥 Project Name: Automated Healthcare Revenue Integrity Pipeline

Bridging Healthcare and Data Analytics | An open-source pipeline designed to process, clean, and analyze clinical billing files to improve health literacy and prevent revenue leakage.

## 📌 Project Overview
Healthcare organizations often generate vast amounts of billing data (EDI 837/835 files) that remain unanalyzed due to operational bottlenecks. This project demonstrates an automated ETL (Extract, Transform, Load) pipeline built with Python and SQL to parse raw EDI data, identify recoverable revenue leaks, and visualize performance metrics.

## Key Features
Automated Data Ingestion: Python script to securely parse X12/EDI healthcare files.

Data Cleansing & Modeling: Normalization of Claim Adjustment Reason Codes (CARCs).

Database Pipeline: SQLite/BigQuery schema optimization for quick analysis.

Interactive Dashboard: Looker Studio/Plotly reporting views for Practice Managers.

## 🛠️ Tech Stack & Requirements
Language: Python 3.10+

Libraries: pandas, edi-835-parser, sqlalchemy, plotly

Data Warehouse: BigQuery or SQLite

BI / Visualization: Looker Studio or Power BI

## ⚙️ Pipeline Architecture
The data flows through the following stages:

Extract: Secure extraction of 835 and 837 files from local storage/SFTP.

Transform: Parsing segments, mapping CARC codes to human-readable terms, and identifying leakage.

Load: Pushing cleaned data to the SQL database.

## 🚀 Getting Started
Prerequisites
Make sure you have installed the required libraries:

Bash
pip install pandas edi-835-parser sqlalchemy plotly
Quickstart Example
To run the primary revenue audit script:

Python
from edi_835_parser import parse
import pandas as pd

# Load the dummy dataset for demonstration
path = './data/sample_835.txt'
transaction_sets = parse(path)

# Convert to DataFrame
df = transaction_sets.to_dataframe()

# Filter for fixable denial codes (e.g., Missing Info - CARC 16)
denied_claims = df[df['adjustment_reason_code'] == '16']
print(f"Recoverable opportunities identified: {len(denied_claims)}")
## 📊 Analytics & Insights
Included in the /reports directory is the SQL query used to rank insurance payers by Net Collection Rate (NCR):

SQL

SELECT 

    payer_name,
    
    COUNT(claim_id) AS total_claims,
    
    SUM(billed_amount) AS total_billed,
    
    SUM(paid_amount) AS total_paid,
    
    SUM(CASE 
    
        WHEN adj_code IN ('16', '22', '27') THEN adj_amount 
        
        ELSE 0 
        
    END) AS recoverable_leakage
    
FROM healthcare_claims

GROUP BY payer_name

ORDER BY recoverable_leakage DESC;

## 🌍 Open Source & Impact
This pipeline is maintained as open-source to make data-driven decisions accessible to healthcare providers and data analysts in emerging markets.

## Supporting This Project
Your support covers the hosting costs for live dashboards, API subscriptions, and cloud computing investments required to build predictive models.

👉 Support this project and keep these tools free (Replace with your link)

## 📜 License
This project is licensed under the MIT License.

## 📬 Contact / Feedback
For questions, collaboration requests, or suggestions to improve health literacy reporting, please reach out via LinkedIn or file an issue on GitHub.
