-- '경제' 카테고리에 속하는 도서들의 도서 ID(BOOK_ID), 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE) 리스트를 출력
-- 1. BOOK, AUTHOR 테이블 author_id 기준으로 JOIN

SELECT BOOK_ID
    , AUTHOR_NAME
    , DATE_FORMAT(published_date,'%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK b
    LEFT JOIN AUTHOR a ON b.author_id = a.author_id
WHERE category = '경제'
ORDER BY 3