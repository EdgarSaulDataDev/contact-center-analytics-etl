
-- Contact Center Analytics ETL
-- Synthetic data model | SQLite

CREATE TABLE IF NOT EXISTS dim_agents (
    agent_id TEXT PRIMARY KEY,
    agent_name TEXT NOT NULL,
    team_name TEXT,
    agent_role TEXT
);

CREATE TABLE IF NOT EXISTS fact_interactions (
    interaction_id TEXT PRIMARY KEY,
    agent_id TEXT,
    start_time TEXT NOT NULL,
    end_time TEXT,
    direction TEXT NOT NULL,
    channel TEXT NOT NULL,
    outcome TEXT NOT NULL,
    queue_name TEXT,
    wait_seconds INTEGER DEFAULT 0,
    talk_seconds INTEGER DEFAULT 0,
    wrap_seconds INTEGER DEFAULT 0,
    is_transferred INTEGER DEFAULT 0,
    FOREIGN KEY (agent_id)
        REFERENCES dim_agents(agent_id)
);

CREATE TABLE IF NOT EXISTS fact_agent_events (
    event_id TEXT PRIMARY KEY,
    interaction_id TEXT NOT NULL,
    agent_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_time TEXT NOT NULL,
    duration_seconds INTEGER DEFAULT 0,
    FOREIGN KEY (interaction_id)
        REFERENCES fact_interactions(interaction_id),
    FOREIGN KEY (agent_id)
        REFERENCES dim_agents(agent_id)
);
