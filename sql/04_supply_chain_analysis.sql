-- Delivery Performance Analysis
SELECT delivery_status,
    COUNT(*) AS total_shipments,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(),
        2
    ) AS percentage
FROM shipments
GROUP BY delivery_status
ORDER BY total_shipments DESC;
-- Late Delivery by Shipping Mode
SELECT shipping_mode,
    COUNT(*) AS total_shipments,
    SUM(late_delivery_risk) AS late_shipments,
    ROUND(
        SUM(late_delivery_risk) * 100.0 / COUNT(*),
        2
    ) AS late_percentage
FROM shipments
GROUP BY shipping_mode
ORDER BY late_percentage DESC;
CREATE VIEW unique_locations AS
SELECT DISTINCT order_country,
    order_region,
    market
FROM locations;
--Regional delivery risk analysis
SELECT l.order_region,
    COUNT(*) AS total_shipments,
    SUM(s.late_delivery_risk) AS late_shipments,
    ROUND(
        SUM(s.late_delivery_risk) * 100.0 / COUNT(*),
        2
    ) AS late_percentage
FROM shipments s
    JOIN orders o ON s.order_id = o.order_id
    JOIN unique_locations l ON o.order_country = l.order_country
GROUP BY l.order_region
ORDER BY late_percentage DESC;