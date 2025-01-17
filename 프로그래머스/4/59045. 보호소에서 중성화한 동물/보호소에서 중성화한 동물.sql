SELECT
    i.animal_id,
    i.animal_type,
    i.name
FROM animal_ins i
    JOIN animal_outs o
    ON i.animal_id = o.animal_id
WHERE sex_upon_intake LIKE 'Intact%' AND sex_upon_outcome NOT LIKE 'Intact%'