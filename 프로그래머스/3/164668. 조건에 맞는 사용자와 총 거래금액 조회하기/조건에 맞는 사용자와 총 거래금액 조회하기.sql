-- 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회
-- 1. writer_id 별 완료된 거래 금액 구하기
-- 2. 해당 유저 정보 출력
SELECT
    u.user_id,
    u.nickname,
    total_sales
FROM USED_GOODS_USER u
    JOIN(SELECT
            writer_id,
            SUM(price) as total_sales
        FROM USED_GOODS_BOARD
        WHERE status = 'DONE'
        GROUP BY writer_id) b
        ON u.user_id = b.writer_id AND total_sales >= 700000
ORDER BY total_sales 
