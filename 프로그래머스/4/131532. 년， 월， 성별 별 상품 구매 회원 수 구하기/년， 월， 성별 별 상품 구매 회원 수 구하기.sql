-- 년, 월, 성별 별로 상품을 구매한 회원수를 집계

SELECT
    YEAR(sales_date) AS year,
    MONTH(sales_date) AS month,
    gender,
    COUNT(DISTINCT u.user_id) AS users
FROM ONLINE_SALE o
    JOIN USER_INFO u
    ON o.user_id = u.user_id
WHERE u.gender IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3