--  평균 길이가 33cm 이상인 물고기들을 종류별로 분류하여 잡은 수, 최대 길이, 물고기의 종류를 출력
WITH FISH_PREPROCESS AS(
    SELECT fish_type
        , CASE WHEN length IS NULL THEN 10
        ELSE length END AS length1
    FROM FISH_INFO
), FISH_AVG AS (
    SELECT fish_type
        , AVG(length1) AS avg_length
    FROM FISH_PREPROCESS
    GROUP BY 1
)

SELECT COUNT(*) AS fish_count
    , MAX(length) AS max_length
    , i.fish_type
FROM FISH_INFO i
    JOIN FISH_AVG a
        ON i.fish_type = a.fish_type AND a.avg_length >= 33
GROUP BY 3
ORDER BY fish_type
