-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력
SELECT
    category,
    SUM(sales) AS total_sales
FROM BOOK_SALES s
    JOIN BOOK b
    ON s.book_id = b.book_id AND s.sales_date BETWEEN '2022-01-01' AND '2022-1-31'
GROUP BY 1
ORDER BY 1
