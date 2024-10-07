-- 노선별로 노선, 총 누계 거리, 평균 역 사이 거리를 노선별로 조회

SELECT 
    route,
    CONCAT(ROUND(SUM(d_between_dist),1),'km') AS total_distance,
    CONCAT(ROUND(AVG(d_between_dist),2),'km') AS average_distance
FROM SUBWAY_DISTANCE
GROUP BY 1
ORDER BY SUM(d_between_dist) DESC