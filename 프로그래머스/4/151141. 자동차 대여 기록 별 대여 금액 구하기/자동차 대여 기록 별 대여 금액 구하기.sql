--  자동차 종류가 '트럭'인 자동차의 대여 기록 별로 대여 금액(컬럼명: FEE) 추출

-- 1. 자동차 대여 일 수 계산
WITH CTE_duration_type AS (
    SELECT 
        *,
        CASE WHEN duration BETWEEN 7 AND 29 THEN '7일 이상'
            WHEN duration BETWEEN 30 AND 89 THEN '30일 이상'
            WHEN duration >= 90 THEN '90일 이상'
            ELSE '7일 미만'
        END AS DURATION_TYPE
    FROM(
        SELECT
            history_id,
            car_id,
            start_date,
            end_date,
            DATEDIFF(END_DATE,START_DATE) + 1  AS duration
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) as duration_tbl
)

SELECT 
    HISTORY_ID,
    IF(p.duration_type IS NULL, FLOOR(duration*daily_fee),FLOOR(duration * daily_fee * (100-discount_rate)/100)) as FEE
FROM CTE_duration_type d
    JOIN CAR_RENTAL_COMPANY_CAR c
    ON d.car_id = c.car_id AND c.car_type = '트럭'
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    ON c.car_type = p.car_type AND d.duration_type = p.duration_type
ORDER BY 2 DESC, 1 DESC