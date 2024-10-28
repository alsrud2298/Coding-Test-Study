-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
SELECT
    member_name,
    review_text,
    DATE_FORMAT(review_date,'%Y-%m-%d') as review_date
FROM REST_REVIEW r
    JOIN MEMBER_PROFILE m
    ON r.member_id = m.member_id
WHERE (m.member_id, 1) IN (
    SELECT
        member_id,
        RANK () OVER (ORDER BY COUNT(review_id) DESC) as rnk
    FROM REST_REVIEW
    GROUP BY member_id
)
ORDER BY 3, 2
