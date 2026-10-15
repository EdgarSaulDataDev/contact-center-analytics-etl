
"""
Contact Center Analytics ETL
Synthetic interaction data generator.

Generates fictional records for portfolio demonstrations.
No real customer or corporate data is used.
"""

import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid4

SEED = 42
TOTAL_INTERACTIONS = 100

random.seed(SEED)

AGENTS = [
    {"agent_id": "AG001", "agent_name": "Alex Rivera",
     "team_name": "Support", "agent_role": "Agent"},
    {"agent_id": "AG002", "agent_name": "Jordan Lee",
     "team_name": "Support", "agent_role": "Agent"},
    {"agent_id": "AG003", "agent_name": "Taylor Morgan",
     "team_name": "Customer Care", "agent_role": "Agent"},
]

OUTCOMES = [
    "Handled by agent",
    "Abandoned in queue",
    "Callback requested",
]


def generate_interactions(count=TOTAL_INTERACTIONS):
    interactions = []
    base_date = datetime(2026, 1, 1, tzinfo=timezone.utc)

    for index in range(count):
        outcome = random.choices(
            OUTCOMES,
            weights=[75, 15, 10],
            k=1
        )[0]

        handled = outcome == "Handled by agent"
        agent = random.choice(AGENTS) if handled else None

        start_time = base_date + timedelta(
            minutes=index * 10
        )

        wait_seconds = random.randint(1, 120)
        talk_seconds = random.randint(60, 900) if handled else 0
        wrap_seconds = random.randint(10, 90) if handled else 0

        interaction = {
            "interaction_id": str(uuid4()),
            "agent_id": agent["agent_id"] if agent else None,
            "start_time": start_time.isoformat(),
            "end_time": (
                start_time + timedelta(
                    seconds=wait_seconds + talk_seconds + wrap_seconds
                )
            ).isoformat(),
            "direction": "Inbound",
            "channel": "Voice",
            "outcome": outcome,
            "queue_name": "Customer Support",
            "wait_seconds": wait_seconds,
            "talk_seconds": talk_seconds,
            "wrap_seconds": wrap_seconds,
            "is_transferred": 0
        }

        interactions.append(interaction)

    return interactions


def main():
    output_dir = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "synthetic"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    interactions = generate_interactions()

    for filename, records in [
        ("agents.json", AGENTS),
        ("interactions.json", interactions)
    ]:
        output_path = output_dir / filename

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=2)

        print(f"Generated: {output_path}")

    print(f"Total interactions: {len(interactions)}")


if __name__ == "__main__":
    main()
