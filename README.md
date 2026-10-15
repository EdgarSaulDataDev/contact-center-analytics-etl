# Contact Center Analytics ETL

**Python | REST API | ETL | SQL | Data Engineering**

## Overview

Contact Center Analytics ETL is an independent, end-to-end Data Engineering portfolio project designed to extract, transform, validate, and analyze synthetic Contact Center interaction data.

The project demonstrates the development of scalable ETL pipelines using Python, REST APIs, SQL databases, and automated data quality processes.

Its primary objective is to transform raw interaction data into structured analytical datasets and operational performance indicators.

## Project Objectives

- Design and develop an end-to-end ETL pipeline using Python.
- Extract interaction data from a simulated REST API.
- Implement incremental data extraction and pagination.
- Process and normalize JSON datasets.
- Apply data cleaning, transformation, and deduplication.
- Design relational and analytical SQL data models.
- Calculate operational Contact Center KPIs.
- Implement automated data quality and reconciliation checks.
- Generate analytical datasets for reporting and visualization.

## Architecture

The proposed data pipeline follows a modular ETL architecture:

**Synthetic REST API → Python Extraction → Raw JSON → Data Transformation → SQL Database → KPI Analytics → Reporting**

### Architecture Components

| Layer | Technology | Description |
|---|---|---|
| Data Source | FastAPI | Simulated REST API providing synthetic interaction data |
| Extraction | Python / Requests | API integration, pagination, and incremental loading |
| Raw Data | JSON | Storage of extracted interaction records |
| Transformation | Python / Pandas | Data cleaning, normalization, and enrichment |
| Data Quality | Python / Pytest | Validation, deduplication, and reconciliation |
| Data Storage | SQLite / SQL | Relational and analytical data storage |
| Analytics | Python / SQL | Contact Center KPI calculations |
| Reporting | CSV / Dashboard | Analytical datasets and performance reporting |
| Automation | GitHub Actions | Automated testing and validation |

## Technology Stack

- **Python:** ETL development and automation.
- **FastAPI:** Synthetic REST API development.
- **Requests:** REST API communication.
- **Pandas:** Data transformation and processing.
- **SQL / SQLite:** Data modeling, storage, and analytics.
- **Pytest:** Unit testing and data validation.
- **Git / GitHub:** Version control and repository management.
- **GitHub Actions:** Continuous integration and automated testing.

## Planned Features

### 1. REST API Integration

- Extract synthetic Contact Center interactions.
- Handle API pagination.
- Implement retry mechanisms and error handling.
- Support configurable extraction periods.

### 2. Incremental ETL Processing

- Process new interaction records.
- Identify missing processing dates.
- Prevent duplicate records.
- Maintain extraction history and execution logs.

### 3. Data Transformation

- Normalize nested JSON structures.
- Standardize dates, timestamps, and interaction outcomes.
- Process agent activity events.
- Identify transferred interactions.
- Create structured analytical datasets.

### 4. Data Quality and Reconciliation

- Validate record counts.
- Detect duplicate interaction identifiers.
- Verify required fields.
- Reconcile source records against transformed datasets.
- Implement automated validation tests.

### 5. Contact Center Analytics

The project will calculate operational performance indicators, including:

| KPI | Description |
|---|---|
| Offered | Total interactions offered to the contact center |
| Handled | Interactions handled by agents |
| Abandoned | Interactions abandoned while waiting |
| Callback Requested | Interactions requesting a callback |
| Service Level (SLA) | Percentage of eligible interactions answered within a defined target |
| Average Handle Time (AHT) | Average time spent handling interactions |
| Average Speed of Answer (ASA) | Average waiting time before an interaction is answered |
| Average Talk Time (ATT) | Average time spent talking with customers |
| Average Wrap-Up Time | Average post-interaction processing time |
| Transferred | Number of unique interactions involving transfers |
| Abandon Rate | Percentage of offered interactions abandoned |

KPI definitions and calculation rules will be documented and validated using synthetic datasets.

### 6. Reporting and Analytics

- Generate daily operational metrics.
- Consolidate monthly and year-to-date results.
- Export analytical datasets to CSV.
- Develop SQL queries for performance analysis.
- Build a dashboard for visualizing Contact Center KPIs.

## Project Structure

The following structure represents the planned implementation:

```text
contact-center-analytics-etl/
│
├── src/
│   ├── api/
│   │   └── mock_server.py
│   ├── extraction/
│   │   ├── client.py
│   │   └── incremental.py
│   ├── transformation/
│   │   ├── normalize.py
│   │   └── interactions.py
│   ├── quality/
│   │   └── validators.py
│   ├── analytics/
│   │   └── kpi_calculator.py
│   └── pipeline.py
│
├── sql/
│   ├── schema.sql
│   └── analytics_queries.sql
│
├── data/
│   └── synthetic/
│
├── tests/
│   ├── test_extraction.py
│   ├── test_transformations.py
│   ├── test_kpis.py
│   └── test_incremental.py
│
├── dashboard/
│   └── app.py
│
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   └── kpi_definitions.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Development Roadmap

- [ ] Phase 1 — Architecture and data modeling
- [ ] Phase 2 — Synthetic data generation and REST API
- [ ] Phase 3 — Python ETL pipeline development
- [ ] Phase 4 — SQL data storage and analytics
- [ ] Phase 5 — Data quality validation and automated testing
- [ ] Phase 6 — Dashboard and reporting
- [ ] Phase 7 — Documentation and final release

## Project Status

**In Development — Phase 1: Architecture and Data Modeling**

This repository is currently under active development. Features and components will be implemented progressively.

## Data Privacy and Disclaimer

This project is an independent educational and professional portfolio implementation.

All datasets are entirely synthetic and generated specifically for demonstration purposes.

The repository does not contain proprietary source code, confidential business information, production credentials, or real customer data.

The project is not affiliated with or endorsed by any Contact Center software provider or former employer.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
