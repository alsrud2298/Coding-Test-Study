-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회
-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회

WITH CTE1 AS (
    SELECT flavor
        , SUM(TOTAL_ORDER) AS total
    FROM FIRST_HALF
    GROUP BY flavor
), CTE2 AS (
    SELECT flavor
        , SUM(TOTAL_ORDER) AS total
    FROM JULY
    GROUP BY flavor
)

SELECT c1.flavor
FROM CTE1 c1
    JOIN CTE2 c2
        ON c1.flavor = c2.flavor
ORDER BY c1.total + c2.total DESC
LIMIT 3