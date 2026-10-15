
-- Contact Center Analytics ETL
-- Synthetic data | Analytical SQL queries
-- SQLite

-- 1. Overall Contact Center KPIs
WITH metrics AS (
    SELECT
        COUNT(*) AS offered,
        SUM(CASE WHEN outcome = 'Handled by agent'
            THEN 1 ELSE 0 END) AS handled,
        SUM(CASE WHEN outcome = 'Abandoned in queue'
            THEN 1 ELSE 0 END) AS abandoned,
        SUM(CASE WHEN outcome = 'Callback requested'
            THEN 1 ELSE 0 END) AS callbacks,
        SUM(CASE WHEN outcome = 'Handled by agent'
            THEN talk_seconds + wrap_seconds ELSE 0 END)
            AS total_handle_seconds,
        SUM(CASE WHEN outcome = 'Handled by agent'
            THEN wait_seconds ELSE 0 END)
            AS total_answer_wait_seconds
    FROM fact_interactions
    WHERE direction = 'Inbound'
)
SELECT
    offered,
    handled,
    abandoned,
    callbacks,
    ROUND(100.0 * abandoned / NULLIF(offered, 0), 2)
        AS abandon_rate_pct,
    ROUND(1.0 * total_handle_seconds / NULLIF(handled, 0), 2)
        AS aht_seconds,
    ROUND(1.0 * total_answer_wait_seconds / NULLIF(handled, 0), 2)
        AS asa_seconds
FROM metrics;


-- 2. Agent Performance
SELECT
    a.agent_id,
    a.agent_name,
    COUNT(*) AS handled,
    ROUND(AVG(i.talk_seconds + i.wrap_seconds), 2)
        AS aht_seconds,
    ROUND(AVG(i.wait_seconds), 2)
        AS asa_seconds
FROM fact_interactions i
JOIN dim_agents a
    ON i.agent_id = a.agent_id
WHERE i.outcome = 'Handled by agent'
GROUP BY a.agent_id, a.agent_name
ORDER BY handled DESC;


-- 3. Daily Interaction Volume
SELECT
    DATE(start_time) AS interaction_date,
    COUNT(*) AS offered,
    SUM(CASE WHEN outcome = 'Handled by agent'
        THEN 1 ELSE 0 END) AS handled,
    SUM(CASE WHEN outcome = 'Abandoned in queue'
        THEN 1 ELSE 0 END) AS abandoned,
    SUM(CASE WHEN outcome = 'Callback requested'
        THEN 1 ELSE 0 END) AS callbacks
FROM fact_interactions
WHERE direction = 'Inbound'
GROUP BY DATE(start_time)
ORDER BY interaction_date;
