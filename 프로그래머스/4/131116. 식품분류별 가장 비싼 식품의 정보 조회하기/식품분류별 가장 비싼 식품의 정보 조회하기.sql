-- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
   
SELECT 
    category, price AS max_price, product_name
FROM FOOD_PRODUCT
WHERE (category, price) IN (
    SELECT
        category,
        max(price)
    FROM FOOD_PRODUCT
    GROUP BY category
    HAVING category IN ('국','김치','식용유','과자')
)
ORDER BY 2 DESC