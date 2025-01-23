# # 쿼리를 작성하는 목표, 확인할 지표 : 평균 대여 기간이 7일 이상인 자동차 ID, 평균 대여 기간 출력
# # 쿼리 계산 방법 : end_date - start_date 의 평균 구하기 -> WHERE절에서 7일 이상 필터링
# # 데이터의 기간 : X
# # 사용할 테이블 : car_rental_company_rental_history
# # 데이터 특징 : 대여 기간 -> end_date - start_date + 1
# SELECT
#     *
# FROM(
#     SELECT
#         car_id,
#         ROUND(AVG(rental_duration),1) average_duration
#     FROM(
#         SELECT
#             car_id,
#             DATEDIFF(end_date,start_date) rental_duration
#         FROM
#             car_rental_company_rental_history
#     ) sub
#     GROUP BY 1
# ) subsub
# WHERE average_duration >= 7
# ORDER BY 2 DESC, 1 DESC
-- 1은 30일, 5는 83 / 5 = 16.6 
SELECT *
FROM(
    SELECT
        car_id,
        ROUND(AVG(DATEDIFF(end_date,start_date) + 1),1) rental_duration
    FROM
        car_rental_company_rental_history
    GROUP BY 1
) sub
WHERE rental_duration >= 7
ORDER BY
    2 DESC,
    1 DESC