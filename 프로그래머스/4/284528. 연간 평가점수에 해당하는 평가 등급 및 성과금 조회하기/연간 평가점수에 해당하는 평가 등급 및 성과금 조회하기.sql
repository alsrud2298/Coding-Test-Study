-- 사번, 성명, 평가 등급, 성과금 조회

SELECT
    g.emp_no,
    e.emp_name,
    CASE 
        WHEN AVG(score) >= 96 THEN 'S'
        WHEN AVG(score) >= 90 THEN 'A'
        WHEN AVG(score) >= 80 THEN 'B'
        ELSE 'C'
    END AS 'grade',
    CASE
        WHEN AVG(score) >= 96 THEN sal * 0.2
        WHEN AVG(score) >= 90 THEN sal * 0.15
        WHEN AVG(score) >= 80 THEN sal * 0.1
        ELSE 0
    END AS 'bonus'
FROM HR_EMPLOYEES e
JOIN HR_GRADE g
    ON e.emp_no = g.emp_no
GROUP BY 1
ORDER BY 1