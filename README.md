# twitter-airflow-data-engineering-project

An end-to-end Data Engineering project that automates ETL workflows using Apache Airflow, AWS, Python, and Databricks. This project demonstrates workflow orchestration, task scheduling, data validation, transformation, and monitoring for scalable analytics pipelines.

Architecture Flow

CSV Data Source
↓
Apache Airflow DAG
↓
Data Validation using Python
↓
AWS S3 Data Lake Storage
↓
Databricks / PySpark Transformations
↓
Delta Lake Processed Layer
↓
Analytics & Reporting

Tech Stack

Apache Airflow, Python, PySpark, AWS S3, Databricks, Delta Lake, SQL, ETL/ELT Pipelines

Key Features

- Automated ETL workflow orchestration
- DAG scheduling and dependency management
- Data quality validation checks
- Scalable batch data processing
- Medallion Architecture implementation
- Monitoring and retry handling using Airflow

Workflow Explanation

1. Airflow triggers the ETL pipeline based on schedule.
2. Raw CSV files are ingested into AWS S3.
3. Validation checks ensure schema and data quality.
4. Databricks processes and transforms the data using PySpark.
5. Cleaned data is stored in Delta Lake tables.
6. Processed data becomes available for analytics and reporting.

Project Objective

The objective of this project is to build a scalable and production-style orchestration pipeline that simulates real-world enterprise ETL workflows using modern cloud and big data technologies.

GitHub Repository

https://github.com/vaibhav-5-7
