-- 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
SELECT
    user_id,
    nickname,
    CONCAT_WS(' ', CITY, STREET_ADDRESS1, STREET_ADDRESS2) AS '전체주소',
    CONCAT_WS('-',SUBSTRING(TLNO,1,3), SUBSTRING(TLNO,4,4),SUBSTRING(TLNO,8,4)) '전화번호'
FROM USED_GOODS_BOARD B
    JOIN USED_GOODS_USER u
    ON b.writer_id = u.user_id
GROUP BY b.writer_id
HAVING COUNT(board_id) >= 3
ORDER BY 1 DESC