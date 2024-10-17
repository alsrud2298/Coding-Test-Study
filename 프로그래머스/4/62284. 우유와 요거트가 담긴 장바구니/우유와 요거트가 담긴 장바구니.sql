-- 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회
SELECT
    cart_id
FROM(
    SELECT
        cart_id,
        GROUP_CONCAT(name) AS products
    FROM CART_PRODUCTS
    GROUP BY cart_id
) AS cart
WHERE products LIKE '%Milk%' AND products LIKE '%Yogurt%'
ORDER BY 1 


