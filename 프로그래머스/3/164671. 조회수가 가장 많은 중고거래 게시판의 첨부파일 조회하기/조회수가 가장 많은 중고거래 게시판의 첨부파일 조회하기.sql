--  조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
SELECT
    CONCAT("/home/grep/src/",board_id,"/",file_id,file_name,file_ext) AS file_path
FROM USED_GOODS_FILE
WHERE board_id = (
    SELECT
        board_id
    FROM USED_GOODS_BOARD
    GROUP BY board_id
    ORDER BY VIEWS DESC
    LIMIT 1
)
ORDER BY file_id DESC