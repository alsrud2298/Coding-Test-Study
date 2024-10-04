SELECT
    COUNT(i.fish_type) AS fish_count,
    fish_name
FROM FISH_INFO i
    JOIN FISH_NAME_INFO n
    ON i.fish_type = n.fish_type
GROUP BY 2
ORDER BY 1 DESC