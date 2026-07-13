SELECT
    CASE
        WHEN price_usd < 25 THEN 'Under $25'
        WHEN price_usd >= 25 AND price_usd < 50 THEN '$25-$50'
        WHEN price_usd >= 50 AND price_usd < 100 THEN '$50-$100'
        ELSE 'Over $100'
    END AS price_range,

    ROUND(AVG(rating), 2) AS average_rating,
    COUNT(product_id) AS product_count

FROM products

WHERE primary_category = 'Skincare'
    AND price_usd IS NOT NULL
    AND rating IS NOT NULL

GROUP BY price_range

ORDER BY average_rating DESC;