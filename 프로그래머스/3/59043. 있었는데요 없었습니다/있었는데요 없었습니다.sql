-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문
SELECT i.animal_id
    , i.name
FROM ANIMAL_INS i
    JOIN ANIMAL_OUTS o
        ON i.animal_id = o.animal_id AND i.datetime > o.datetime
ORDER BY i.datetime