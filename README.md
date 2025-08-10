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

## 🚀 How to Run the Project Locally

### Prerequisites
- Install **Docker** and **Docker Compose** on your machine.  
  [Docker Installation Guide](https://docs.docker.com/get-docker/)  
- (Optional) Have **Python 3.8+** installed if you want to run scripts locally.

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dilshad7275/data-engineering-elt-telecom-customer-churn.git
   cd data-engineering-elt-telecom-customer-churn
2. Download the dataset
	- **Download the dataset from Kaggle Telecom Customer Churn Dataset and place the CSV file inside the data/incoming folder.**

3. Start the containers using Docker Compose
	```
    bash
	docker-compose up -d
    ```
      This will start:
    	- **PostgreSQL database (staging and production schemas)**
    	- **Apache Airflow for orchestration**
    	- **Metabase for reporting dashboard**

4. Access the services
   - **Airflow UI: http://localhost:8080**
		- **Default credentials:**
		- **Username: admin**
		- **Password: admin*
   - **Metabase UI: http://localhost:3000**

5. Run the ELT pipeline
	- **The Airflow DAG is scheduled to run every 2 hours by default. You can also trigger it manually from the Airflow UI.**

6. View reports in Metabase
	- **Metabase is connected to the processed PostgreSQL database and provides a dashboard to explore customer churn analytics.**

##Notes
- **Ensure the CSV dataset is correctly placed in the data/incoming folder before running the pipeline.**
- **Logs and other runtime files are stored in the scripts/logs/ folder for troubleshooting.**
- **The pipeline handles ingestion, transformation (including missing values and PII anonymization), and loads the processed data for reporting.**	

## 👤 Author
Dilshad Ahmed – Data Engineer & (Python, Snowflake, SQL, Power BI) Developer

