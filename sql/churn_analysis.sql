WITH last_order AS (
    SELECT 
        user_id,
        MAX(order_date) AS last_purchase
    FROM orders
    GROUP BY user_id
)
SELECT 
    CASE 
        WHEN CURRENT_DATE - last_purchase > 90 THEN 'Churned'
        WHEN CURRENT_DATE - last_purchase > 45 THEN 'At Risk'
        ELSE 'Active'
    END AS customer_status,
    COUNT(*) AS users
FROM last_order
GROUP BY customer_status;