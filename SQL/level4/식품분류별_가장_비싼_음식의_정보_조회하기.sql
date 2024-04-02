-- 코드를 입력하세요
SELECT
    A.CATEGORY,
    MAX_PRICE,
    PRODUCT_NAME
FROM
    (SELECT
        CATEGORY , 
        MAX(PRICE) AS MAX_PRICE
    FROM
        FOOD_PRODUCT
    WHERE
        CATEGORY IN ('과자', '김치', '국', '식용유')
    GROUP BY
        CATEGORY
    ) A
    INNER JOIN
        FOOD_PRODUCT B
        ON A.CATEGORY = B.CATEGORY
        AND A.MAX_PRICE = B.PRICE
ORDER BY
    MAX_PRICE DESC
;