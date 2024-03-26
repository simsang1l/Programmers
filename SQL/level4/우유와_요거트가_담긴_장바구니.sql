SELECT
    CART_ID
FROM (
    SELECT DISTINCT
        CART_ID ,
        NAME
    FROM
        CART_PRODUCTS
    WHERE
        NAME LIKE 'Milk%' or NAME LIKE 'Yogurt%'
) a 
GROUP BY
    CART_ID
HAVING COUNT(*) = 2
order by
    CART_ID
;


-- 다른사람 풀이
-- in 안에 있는 것들은 or조건임
SELECT CART_ID
  FROM CART_PRODUCTS
 WHERE NAME IN ('Milk','Yogurt')
 GROUP BY CART_ID
 HAVING COUNT(DISTINCT NAME)=2