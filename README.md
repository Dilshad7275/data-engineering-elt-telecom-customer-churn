# data-engineering-elt-telecom-customer-churn
End-to-end ETL pipeline for telecom customer churn data — ingestion, transformation, anonymization, and reporting using open-source tools and containerized orchestration.

## 📌 Project Overview

This project demonstrates a complete ELT pipeline that ingests a telecom customer churn dataset, processes it to handle missing values and anonymize Personally Identifiable Information (PII), and stores the transformed data in a reporting-friendly database. The pipeline is fully containerized and orchestrated for scheduled runs, making it ready for production-level deployments.

This project not only solves the assignment problem but also serves as a portfolio-ready demonstration of my skills in Data Engineering, Python, SQL, ETL/ELT design, and workflow orchestration.

## 🏗 Architecture
```
    A[CSV Dataset] -->|Ingest| B[Staging DB - PostgreSQL]
    B -->|Transform & Anonymize| C[Processed DB - PostgreSQL]
    C -->|Generate Reports| D[Reporting Tool]
    subgraph Orchestration
        E[Scheduler] --> B
    end
```

## 🛠️ Tech Stack

- **Programming Language**: Python  
- **ETL Orchestration**: Apache Airflow (orchestration container setup)  
- **Database**: PostgreSQL (Staging & Processed Layers)  
- **Libraries**:  
  - Pandas  
  - SQLAlchemy  
  - Psycopg2  
- **Containerization**: Docker & Docker Compose  
- **Reporting**: Metabase (open-source BI tool)

##  📊 Dataset
- **Name**: Customer Churn Prediction: Analysis
- **Source**: Kaggle – Telecom Customer Churn Insights
- **Description**: Contains customer details, subscription information, service usage metrics, and churn status for telecom customers.

## 🚀 Features
- **Ingest CSV data into staging PostgreSQL**.
- **Transform data by**:
    - **Filling missing values with default values**.
    - **Anonymizing PII (names, phone numbers, etc.)**.
- **Store cleaned data in processed PostgreSQL for reporting**.
- **Hourly ingestion schedule (configurable)**.
- **Containerized for quick deployment**.
- **Integrated reporting dashboard using Metabase**.

## 📂 Folder Structure
```
customer-churn-elt-pipeline/
│-- dags/                 # Airflow DAGs for orchestration
│-- scripts/              # Python scripts for ingestion & transformation
│-- data/                 # CSV dataset
│-- docker-compose.yml    # Container definitions
│-- docker-compose-airflow.yml    # Container definitions
│-- requirements.txt      # Python dependencies
│-- README.md             # Project documentation
```
## Customer Churn Metrics Dashboard Live URL
http://localhost:3000/public/dashboard/1367d86c-c839-44c5-92e7-646d0e901e5d

## 👤 Author
Dilshad Ahmed – Data Engineer & (Python, Snowflake, SQL, Power BI) Developer
