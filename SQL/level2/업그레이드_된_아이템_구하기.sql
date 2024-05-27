SELECT
    ITEM_ID,
    ITEM_NAME,
    RARITY
FROM
    ITEM_INFO
WHERE ITEM_ID IN
    (SELECT
        B.ITEM_ID 
     FROM 
         (
            SELECT
                ITEM_ID
            FROM
                ITEM_INFO 
            WHERE
                RARITY = 'RARE'
        )A
        INNER JOIN
            ITEM_TREE B
            ON A.ITEM_ID = B.PARENT_ITEM_ID
            AND PARENT_ITEM_ID IS NOT NULL
    )
ORDER BY
    ITEM_ID DESC
;