# Contact Center Analytics ETL

![CI Pipeline](https://github.com/EdgarSaulDataDev/contact-center-analytics-etl/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Pytest](https://img.shields.io/badge/Testing-Pytest-green)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

**Contact Center Analytics ETL** is a Python-based data engineering portfolio project designed to demonstrate the development of a reproducible Extract, Transform, Load (ETL) pipeline for contact center operational analytics.

The project generates synthetic interaction data, processes and loads structured records into a relational SQLite database, and provides SQL queries for analyzing operational performance.

Automated data quality tests and GitHub Actions continuous integration help validate the reliability and consistency of the pipeline.

All datasets are artificially generated. The project does not use proprietary contact center information, production credentials, or confidential business data.

## Project Objectives

- Design and implement a modular ETL pipeline using Python.
- Generate reproducible synthetic datasets for development and testing.
- Model relational data for contact center operational reporting.
- Load structured data into SQLite with referential integrity.
- Support repeatable pipeline executions without accumulating duplicate records.
- Develop SQL queries for operational performance indicators.
- Implement automated data quality validation using Pytest.
- Execute the pipeline and tests automatically through GitHub Actions.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data generation, ETL processing, and pipeline orchestration |
| SQLite | Relational data storage |
| SQL | Data modeling, transformations, and analytical queries |
| JSON | Synthetic source data |
| Pytest | Automated data quality testing |
| Git | Source code version control |
| GitHub | Repository hosting |
| GitHub Actions | Continuous integration |
| GitHub Codespaces | Cloud-based development environment |

## ETL Architecture

```text
Synthetic Data Generator
         |
         v
    JSON Sources
    |          |
 agents.json   interactions.json
    |          |
    +-----+----+
          |
          v
   Python ETL Loader
          |
          v
   SQLite Database
          |
          +--------------------+
          |                    |
          v                    v
   SQL Analytics         Data Quality Tests
          |                    |
          v                    v
   Operational KPIs       Pytest Validation
                               |
                               v
                         GitHub Actions
```

The current pipeline follows a modular architecture:

**1. Data Generation**

Generates deterministic synthetic agent and interaction records.

**2. Data Loading**

Reads JSON files, initializes the SQLite schema, and loads records into relational tables.

**3. Data Validation**

Validates record counts, outcome distribution, identifiers, referential integrity, and duration values.

**4. Analytical Queries**

Provides SQL queries for evaluating contact center performance.

**5. Continuous Integration**

Runs the ETL pipeline and automated tests on GitHub Actions.

## Project Structure

```text
contact-center-analytics-etl/
|
|-- .github/
|   |-- workflows/
|       |-- ci.yml
|
|-- data/
|   |-- synthetic/
|
|-- sql/
|   |-- schema.sql
|   |-- analytics_queries.sql
|
|-- src/
|   |-- generator/
|   |   |-- generate_data.py
|   |
|   |-- loading/
|   |   |-- sqlite_loader.py
|   |
|   |-- pipeline.py
|
|-- tests/
|   |-- test_data_quality.py
|
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
```

Generated JSON files and the SQLite database are excluded from version control.

## Data Model

The SQLite schema contains three tables.

### dim_agents

Stores synthetic contact center agent information.

| Column | Description |
|---|---|
| agent_id | Unique agent identifier |
| agent_name | Agent display name |
| team_name | Assigned team |
| agent_role | Agent role |

### fact_interactions

Stores interaction-level operational information.

| Column | Description
