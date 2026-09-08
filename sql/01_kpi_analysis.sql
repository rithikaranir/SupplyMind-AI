-- Total Revenue
SELECT ROUND(SUM(sales), 2) AS total_revenue
FROM financials;
-- Total Profit
SELECT ROUND(SUM(order_profit), 2) AS total_profit
FROM financials;
-- Total Orders
SELECT COUNT(order_id) AS total_orders
FROM orders;
-- Total Customers
SELECT COUNT(customer_id) AS total_customers
FROM customers;
-- Average Order Value
SELECT ROUND(AVG(order_total), 2) AS avg_order_value
FROM order_items;