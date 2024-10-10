-- 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는 컬럼
SELECT 
    history_id,
    car_id,
    DATE_FORMAT(start_date,'%Y-%m-%d') AS start_date,
    DATE_FORMAT(end_date,'%Y-%m-%d') AS end_date,
    IF(DATEDIFF(end_date,start_date)>=29,'장기 대여','단기 대여') AS rent_type
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE start_date >= '2022-09-01 00:00:00' AND start_date <= '2022-09-30 23:59:59'
ORDER BY 1 DESC