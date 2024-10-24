--  생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회
SELECT
    p.product_id,
    p.product_name,
    SUM(f.amount * p.price) AS total_sales
FROM FOOD_ORDER f
    JOIN FOOD_PRODUCT p
    ON f.product_id = p.product_id
    AND f.produce_date BETWEEN '2022-05-01 00:00:00' AND '2022-05-31 23:59:59'
GROUP BY 1,2
ORDER BY 3 DESC, 1