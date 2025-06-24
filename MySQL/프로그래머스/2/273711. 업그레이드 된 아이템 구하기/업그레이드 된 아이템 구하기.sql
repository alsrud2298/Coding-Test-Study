-- 희귀도가 'RARE'인 아이템들의 다음 업그레이드 아이템 정보 출력
-- 희귀도가 RARE인 ITEM을 부모로 가지는 ITEM 찾기
SELECT
    ITEM_ID,
    ITEM_NAME,
    RARITY
FROM
    ITEM_INFO
WHERE
    ITEM_ID IN (
        SELECT
            ITEM_ID
        FROM ITEM_TREE
        WHERE
            PARENT_ITEM_ID IN (
            SELECT
                ITEM_ID
            FROM ITEM_INFO
            WHERE RARITY = 'RARE'
        )

)
ORDER BY ITEM_ID DESC
