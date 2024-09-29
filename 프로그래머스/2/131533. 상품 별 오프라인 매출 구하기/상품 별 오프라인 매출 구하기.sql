-- 상품코드 별 매출액(판매가 * 판매량) 합계를 출력

-- 상품 별 판매량 계산
WITH CTE AS (
    SELECT PRODUCT_ID
        , SUM(SALES_AMOUNT) AS sales_cnt
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
)

SELECT PRODUCT_CODE
    , price * sales_cnt AS SALES
FROM PRODUCT p
    JOIN CTE c
    ON p.product_id = c.product_id
ORDER BY 2 DESC, 1
