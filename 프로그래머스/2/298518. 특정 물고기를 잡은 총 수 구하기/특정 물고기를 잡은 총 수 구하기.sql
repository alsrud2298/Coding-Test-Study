-- bass와 snapper의 수 출력

SELECT
    COUNT(*) fish_count
FROM FISH_INFO i
LEFT JOIN FISH_NAME_INFO fni
ON i.fish_type = fni.fish_type
WHERE fish_name IN ("BASS","SNAPPER")
