-- 부서별로 부서 ID, 영문 부서명, 평균 연봉을 조회

SELECT
    d.dept_id,
    d.dept_name_en,
    ROUND(AVG(sal),0) AS AVG_SAL
FROM HR_DEPARTMENT d
    JOIN HR_EMPLOYEES e
    ON d.dept_id = e.dept_id
GROUP BY 1,2
ORDER BY 3 DESC