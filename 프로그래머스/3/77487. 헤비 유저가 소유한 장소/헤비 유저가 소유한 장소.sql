-- 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회
SELECT
    id,
    name,
    host_id
FROM PLACES
WHERE host_id IN (
    SELECT -- 유저 별 등록한 공간 id 수 추출
        host_id
    FROM PLACES
    GROUP BY 1
    HAVING COUNT(id) >= 2
)
ORDER BY id
