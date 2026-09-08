-- Revenue by Customer Segment
SELECT c.customer_segment,
    ROUND(SUM(f.sales)::numeric, 2) AS revenue
FROM customers c
    JOIN orders o ON c.customer_id = o.order_customer_id
    JOIN financials f ON o.order_id = f.order_id
GROUP BY c.customer_segment
ORDER BY revenue DESC;
--Top 10 Customers by Spending
SELECT c.customer_id,
    c.customer_first_name,
    c.customer_last_name,
    c.customer_segment,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(f.sales)::numeric, 2) AS total_spent,
    ROUND(AVG(f.sales)::numeric, 2) AS avg_order_value
FROM customers c
    JOIN orders o ON c.customer_id = o.order_customer_id
    JOIN financials f ON o.order_id = f.order_id
GROUP BY c.customer_id,
    c.customer_first_name,
    c.customer_last_name,
    c.customer_segment
ORDER BY total_spent DESC
LIMIT 10;