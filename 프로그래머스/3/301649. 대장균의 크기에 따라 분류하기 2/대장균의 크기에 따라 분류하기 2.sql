SELECT
    id,
    CASE 
        WHEN pct <= 25 THEN "CRITICAL"
        WHEN pct <= 50 THEN "HIGH"
        WHEN pct <= 75 THEN "MEDIUM"
        ElSE "LOW" END colony_name  
FROM(
    SELECT
        id,
        PERCENT_RANK() OVER(ORDER BY size_of_colony DESC) * 100 as pct
    FROM ECOLI_DATA
) sub
ORDER BY id
