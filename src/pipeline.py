
"""
Contact Center Analytics ETL
End-to-end synthetic data pipeline.
"""

import sqlite3
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_script(script_path, step_name):
    print(f"\n[START] {step_name}", flush=True)

    subprocess.run(
        [PYTHON, str(BASE_DIR / script_path)],
        cwd=BASE_DIR,
        check=True
    )

    print(f"[SUCCESS] {step_name}", flush=True)


def validate_database():
    db_path = BASE_DIR / "data" / "contact_center.db"

    with sqlite3.connect(db_path) as connection:
        agents = connection.execute(
            "SELECT COUNT(*) FROM dim_agents"
        ).fetchone()[0]

        interactions = connection.execute(
            "SELECT COUNT(*) FROM fact_interactions"
        ).fetchone()[0]

        outcomes = connection.execute(
            """
            SELECT outcome, COUNT(*)
            FROM fact_interactions
            GROUP BY outcome
            ORDER BY outcome
            """
        ).fetchall()

    print("\n[VALIDATION] Database results")
    print(f"Agents: {agents}")
    print(f"Interactions: {interactions}")

    for outcome, count in outcomes:
        print(f"{outcome}: {count}")

    if agents != 3 or interactions != 100:
        raise ValueError(
            "Data validation failed: unexpected record counts"
        )

    print("[SUCCESS] Data validation passed")


def main():
    print("=" * 50)
    print("CONTACT CENTER ANALYTICS ETL")
    print("=" * 50)

    run_script(
        "src/generator/generate_data.py",
        "Generate synthetic data"
    )

    run_script(
        "src/loading/sqlite_loader.py",
        "Load data into SQLite"
    )

    validate_database()

    print("\n[SUCCESS] ETL pipeline completed")


if __name__ == "__main__":
    main()
