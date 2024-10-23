-- 목적 : 몇 시에 입양이 가장 활발하게 일어나는지 
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회

SET @hour := -1;

SELECT
    (@hour := @hour + 1) AS HOUR,
    (SELECT COUNT(*)
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
ORDER BY HOUR