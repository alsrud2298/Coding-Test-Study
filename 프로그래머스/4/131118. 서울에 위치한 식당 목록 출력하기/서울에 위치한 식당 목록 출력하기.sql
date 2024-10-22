-- 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고 결과는 평균점수를 기준으로 내림차순 정렬해주시고, 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬

SELECT
    i.rest_id,
    i.rest_name,
    i.food_type,
    i.favorites,
    i.address,
    ROUND(AVG(r.review_score),2) AS score
FROM REST_REVIEW r
    JOIN REST_INFO i
    ON r.rest_id = i.rest_id
WHERE address LIKE '서울%'
GROUP BY 1,2,3,4,5
ORDER BY 6 DESC, 4 DESC