-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일
SELECT
    name,
    datetime
FROM ANIMAL_INS
WHERE animal_id NOT IN (
    SELECT animal_id
    FROM ANIMAL_OUTS
)
ORDER BY datetime
LIMIT 3