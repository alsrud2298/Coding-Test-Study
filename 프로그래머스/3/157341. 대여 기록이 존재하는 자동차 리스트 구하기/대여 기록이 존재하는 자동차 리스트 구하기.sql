-- 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트
SELECT DISTINCT c.car_id
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    JOIN CAR_RENTAL_COMPANY_CAR c
        ON h.car_id = c.car_id 
        AND c.car_type = '세단'
        AND h.start_date BETWEEN '2022-10-01 00:00:00' AND '2022-10-31 23:59:59'
ORDER BY 1 DESC