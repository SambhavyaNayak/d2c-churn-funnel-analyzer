WITH funnel AS (
    SELECT 
        event_type,
        COUNT(DISTINCT session_id) AS sessions
    FROM funnel_events
    GROUP BY event_type
)
SELECT * FROM funnel
ORDER BY sessions DESC;