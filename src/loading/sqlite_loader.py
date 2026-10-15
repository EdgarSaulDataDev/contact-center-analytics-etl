
"""
Contact Center Analytics ETL
Load synthetic JSON data into SQLite.
"""

import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "synthetic"
DB_PATH = BASE_DIR / "data" / "contact_center.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"


def load_json(filename, data_dir=DATA_DIR):
    with (Path(data_dir) / filename).open(encoding="utf-8") as file:
        return json.load(file)


def load_database(db_path=DB_PATH, data_dir=DATA_DIR):
    db_path = Path(db_path)
    agents = load_json("agents.json", data_dir)
    interactions = load_json("interactions.json", data_dir)

    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        connection.executescript(schema)

        for agent in agents:
            connection.execute(
                """
                INSERT OR REPLACE INTO dim_agents
                (agent_id, agent_name, team_name, agent_role)
                VALUES (?, ?, ?, ?)
                """,
                (
                    agent["agent_id"],
                    agent["agent_name"],
                    agent["team_name"],
                    agent["agent_role"],
                ),
            )

        for item in interactions:
            connection.execute(
                """
                INSERT OR REPLACE INTO fact_interactions (
                    interaction_id, agent_id, start_time,
                    end_time, direction, channel, outcome,
                    queue_name, wait_seconds, talk_seconds,
                    wrap_seconds, is_transferred
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item["interaction_id"],
                    item["agent_id"],
                    item["start_time"],
                    item["end_time"],
                    item["direction"],
                    item["channel"],
                    item["outcome"],
                    item["queue_name"],
                    item["wait_seconds"],
                    item["talk_seconds"],
                    item["wrap_seconds"],
                    item["is_transferred"],
                ),
            )

        connection.commit()

        for table in ("dim_agents", "fact_interactions"):
            count = connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]

            print(f"{table}: {count} records")

    print(f"Database created: {db_path}")


def main():
    load_database()


if __name__ == "__main__":
    main()
