SELECT
    A.FLAVOR
FROM
    (SELECT
        FLAVOR
     , TOTAL_ORDER
    FROM
        FIRST_HALF
    WHERE
        TOTAL_ORDER >= 3000) A 
    INNER JOIN
        (SELECT
            FLAVOR
        FROM
            ICECREAM_INFO
         WHERE
            INGREDIENT_TYPE = 'fruit_based'
        ) B 
    ON A.FLAVOR = B.FLAVOR
ORDER BY
    TOTAL_ORDER DESC
;