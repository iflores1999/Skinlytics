SELECT
    secondary_category,
    ROUND(AVG(rating), 2) AS average_rating,
    COUNT(product_id) AS product_count

FROM products

WHERE primary_category = 'Skincare'
    AND secondary_category IS NOT NULL
    AND rating IS NOT NULL

GROUP BY secondary_category

HAVING COUNT(product_id) >= 10

ORDER BY average_rating DESC

LIMIT 10;