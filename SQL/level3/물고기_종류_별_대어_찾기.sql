SELECT
    ID          AS ID,
    FISH_NAME   AS FISH_NAME,
    B.LENGTH    AS LENGTH
FROM
    FISH_INFO A
    INNER JOIN
        (
            SELECT
                FISH_TYPE,
                MAX(LENGTH) AS LENGTH
            FROM
                FISH_INFO A
            GROUP BY
                FISH_TYPE
        ) B
        ON A.FISH_TYPE = B.FISH_TYPE
        AND A.LENGTH = B.LENGTH    
    INNER JOIN
        FISH_NAME_INFO C
        ON A.FISH_TYPE = C.FISH_TYPE
ORDER BY
    ID
;

-- WINDOW 함수를 써서도 가능하겠다.
WITH FISH_RANK_INFO AS (
    SELECT ID, FISH_NAME, LENGTH,
    RANK() OVER (PARTITION BY FISH_TYPE ORDER BY LENGTH DESC) AS LENGTH_RNAK
    FROM FISH_INFO I
    JOIN FISH_NAME_INFO N USING(FISH_TYPE)
)

SELECT ID, FISH_NAME, LENGTH
FROM FISH_RANK_INFO
WHERE LENGTH_RNAK = 1
ORDER BY ID