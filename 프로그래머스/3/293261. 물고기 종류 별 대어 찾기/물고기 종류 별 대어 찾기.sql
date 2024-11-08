-- 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력
SELECT id
    , fish_name
    , length
FROM FISH_INFO i
    JOIN FISH_NAME_INFO n
        ON i.fish_type = n.fish_type
WHERE (i.fish_type, length) IN (
    SELECT fish_type
        , MAX(length)
    FROM FISH_INFO
    GROUP BY fish_type)
ORDER BY id