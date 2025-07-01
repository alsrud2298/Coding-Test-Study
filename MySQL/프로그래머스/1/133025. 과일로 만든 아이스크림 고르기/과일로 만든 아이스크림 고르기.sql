-- 상반기 아이스크림 총 주문량이 3,000보다 높으면서, 주 성분이 과일맛인 아이스크림 조회

SELECT
    fh.flavor
FROM FIRST_HALF fh
JOIN ICECREAM_INFO ii
ON fh.flavor = ii.flavor
WHERE fh.total_order >= 3000 AND ii.ingredient_type = 'fruit_based'
ORDER BY
    total_order DESC