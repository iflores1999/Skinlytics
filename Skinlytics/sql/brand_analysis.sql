SELECT
    brand_name,
    AVG(rating) AS average_rating,
    COUNT(product_id) AS product_count
FROM products
WHERE primary_category = 'Skincare'
GROUP BY brand_name
HAVING COUNT(product_id) >= 10
ORDER BY average_rating DESC
LIMIT 10;
