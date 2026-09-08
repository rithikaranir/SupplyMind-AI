--Monthly Revenue Trend
SELECT EXTRACT(
        YEAR
        FROM order_date::timestamp
    ) AS year,
    EXTRACT(
        MONTH
        FROM order_date::timestamp
    ) AS month,
    ROUND(SUM(sales)::numeric, 2) AS monthly_revenue
FROM orders o
    JOIN financials f ON o.order_id = f.order_id
GROUP BY year,
    month
ORDER BY year,
    month;
--Top 10 Products by Revenue
SELECT p.product_name,
    ROUND(SUM(oi.order_total)::numeric, 2) AS revenue
FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;
-- Revenue by Category
SELECT p.category_name,
    ROUND(SUM(oi.order_total)::numeric, 2) AS revenue
FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category_name
ORDER BY revenue DESC;
-- Revenue by Country
SELECT o.order_country,
    ROUND(SUM(f.sales)::numeric, 2) AS revenue
FROM orders o
    JOIN financials f ON o.order_id = f.order_id
GROUP BY o.order_country
ORDER BY revenue DESC
LIMIT 10;