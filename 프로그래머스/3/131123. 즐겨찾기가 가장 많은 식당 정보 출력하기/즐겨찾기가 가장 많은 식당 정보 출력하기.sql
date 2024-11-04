-- 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회
SELECT food_type
    , rest_id
    , rest_name
    , favorites
FROM REST_INFO
WHERE (food_type, rest_id, 1) IN (
    SELECT food_type
        , rest_id
        , RANK() OVER (PARTITION BY food_type ORDER BY favorites DESC)
    FROM REST_INFO
)
ORDER BY food_type DESC

