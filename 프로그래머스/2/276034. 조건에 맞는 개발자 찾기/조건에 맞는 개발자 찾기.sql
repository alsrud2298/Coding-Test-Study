# 쿼리를 작성하는 목표, 확인할 지표 : 조건에 맞는 개발자 정보 조회
# 쿼리 계산 방법 : skillcodes + developers -> where name 파이썬, C#으로 필터링
-- 보유하고 있다는 정의 : code의 합이 skill_code의 합보다 작아야?
# Join Key : skill_code

SELECT
    DISTINCT id,
    email,
    first_name,
    last_name
FROM developers
WHERE skill_code & (SELECT SUM(code) FROM skillcodes WHERE name IN ("Python","C#"))
ORDER BY id