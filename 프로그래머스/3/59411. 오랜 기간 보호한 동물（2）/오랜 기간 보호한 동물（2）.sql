-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회
-- 보호 기간 : 입양일 - 보호 시작일 
SELECT
    i.animal_id,
    i.name
FROM ANIMAL_INS i
    LEFT JOIN ANIMAL_OUTS o
    ON i.animal_id = o.animal_id
WHERE o.animal_id IS NOT NULL -- 입양을 간 동물만 추출
ORDER BY o.datetime - i.datetime DESC -- 보호 기간 긴 순으로 정렬
LIMIT  2 -- 2마리만