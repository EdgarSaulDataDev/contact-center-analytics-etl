
"""
Automated data quality tests for the
Contact Center Analytics ETL project.
"""

import sqlite3
from pathlib import Path

import pytest



BASE_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture
def connection(tmp_path):
    import sys

    sys.path.insert(0, str(BASE_DIR))

    from src.loading.sqlite_loader import load_database

    temporary_db = tmp_path / "test_contact_center.db"

    load_database(db_path=temporary_db)

    conn = sqlite3.connect(temporary_db)
    conn.execute("PRAGMA foreign_keys = ON")

    yield conn

    conn.close()

def test_agents_count(connection):
    result = connection.execute(
        "SELECT COUNT(*) FROM dim_agents"
    ).fetchone()[0]

    assert result == 3


def test_interactions_count(connection):
    result = connection.execute(
        "SELECT COUNT(*) FROM fact_interactions"
    ).fetchone()[0]

    assert result == 100


def test_unique_interaction_ids(connection):
    total, unique_ids = connection.execute(
        """
        SELECT
            COUNT(*),
            COUNT(DISTINCT interaction_id)
        FROM fact_interactions
        """
    ).fetchone()

    assert total == unique_ids



def test_valid_agent_references(connection):
    invalid_references = connection.execute(
        """
        SELECT COUNT(*)
        FROM fact_interactions AS i
        LEFT JOIN dim_agents AS a
            ON i.agent_id = a.agent_id
        WHERE i.agent_id IS NOT NULL
          AND a.agent_id IS NULL
        """
    ).fetchone()[0]

    assert invalid_references == 0


def test_handled_interactions_have_valid_agents(connection):
    invalid_handled = connection.execute(
        """
        SELECT COUNT(*)
        FROM fact_interactions AS i
        LEFT JOIN dim_agents AS a
            ON i.agent_id = a.agent_id
        WHERE i.outcome = 'Handled by agent'
          AND a.agent_id IS NULL
        """
    ).fetchone()[0]

    assert invalid_handled == 0

def test_outcome_distribution(connection):
    results = dict(
        connection.execute(
            """
            SELECT outcome, COUNT(*)
            FROM fact_interactions
            GROUP BY outcome
            """
        ).fetchall()
    )

    assert results == {
        "Handled by agent": 74,
        "Abandoned in queue": 12,
        "Callback requested": 14,
    }


def test_no_negative_durations(connection):
    invalid_durations = connection.execute(
        """
        SELECT COUNT(*)
        FROM fact_interactions
        WHERE wait_seconds < 0
           OR talk_seconds < 0
           OR wrap_seconds < 0
        """
    ).fetchone()[0]

    assert invalid_durations == 0
