DROP TABLE IF EXISTS ml_delivery_prediction;
CREATE TABLE ml_delivery_prediction AS
SELECT s.order_id,
    s.shipping_mode,
    s.scheduled_shipping_days,
    s.actual_shipping_days,
    s.late_delivery_risk,
    o.market,
    o.order_region,
    c.customer_segment,
    p.category_name,
    oi.quantity,
    oi.order_total
FROM shipments AS s
    JOIN orders AS o ON s.order_id = o.order_id
    JOIN customers AS c ON o.order_customer_id = c.customer_id
    JOIN order_items AS oi ON o.order_id = oi.order_id
    JOIN products AS p ON oi.product_id = p.product_id;
SELECT COUNT(*)
FROM ml_delivery_prediction;
SELECT *
FROM ml_delivery_prediction
LIMIT 5;