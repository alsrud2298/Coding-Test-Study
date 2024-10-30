--  대여 시작일을 기준으로 
-- 1. 2022년 8월부터 2022년 10월까지 
-- 2. 총 대여 횟수가 5회 이상인 자동차들에 대해서 
-- 3. 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력

SELECT
    MONTH(start_date) AS month,
    car_id,
    COUNT(history_id) AS records
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id IN ( -- 총 대여 횟수가 5회 이상인 자동차들에 대해
    SELECT
        car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE start_date BETWEEN '2022-08-01 00:00:00' AND '2022-10-31 23:59:59'
    GROUP BY car_id
    HAVING COUNT(history_id) >= 5
) AND start_date BETWEEN '2022-08-01 00:00:00' AND '2022-10-31 23:59:59'
GROUP BY 1,2
HAVING records != 0
ORDER BY month, car_id DESC