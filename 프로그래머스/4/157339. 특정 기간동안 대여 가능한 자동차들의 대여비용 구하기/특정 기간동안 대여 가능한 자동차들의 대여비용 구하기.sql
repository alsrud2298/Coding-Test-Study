-- 문제 : 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력
-- 정렬 : 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬


-- 11-01 ~ 11-30일에 대여 가능한 차량 리스트
WITH CTE AS(
    SELECT DISTINCT c.CAR_ID
            , c.CAR_TYPE
            , c.DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR AS c
        LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS h -- 차량 한대에 대해서 여러번의 대여 기록 존재 가능
        ON c.car_id = h.car_id AND  c.CAR_TYPE IN ('세단','SUV')
    GROUP BY c.CAR_ID
    HAVING MAX(end_date) < '2022-11-01'
)

SELECT c.CAR_ID
    , c.CAR_TYPE
    , FLOOR(daily_fee * 30 * (1-discount_rate/100)) AS FEE
FROM CTE c
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
    ON c.car_type = d.car_type AND d.duration_type = '30일 이상'
HAVING FEE >= 500000
AND FEE < 2000000
ORDER BY 3 DESC, 2, 1 DESC
