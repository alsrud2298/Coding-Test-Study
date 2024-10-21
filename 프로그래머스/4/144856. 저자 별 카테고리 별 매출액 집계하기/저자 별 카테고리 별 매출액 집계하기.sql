-- 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
SELECT
    a.author_id,
    a.author_name,
    b.category,
    SUM(s.sales * b.price) AS total_sales
FROM BOOK_SALES s
    JOIN BOOK b
        ON s.book_id = b.book_id AND sales_date BETWEEN '2022-01-01 00:00:00' AND '2022-01-31 23:59:59'
    JOIN AUTHOR a
        ON a.author_id = b.author_id
GROUP BY 1,2,3
ORDER BY 1,3 DESC
