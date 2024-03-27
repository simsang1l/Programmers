-- 코드를 입력하세요
SELECT
    A.ID,
    A.NAME,
    A.HOST_ID
FROM
    PLACES A
    INNER JOIN
        (SELECT
            HOST_ID,
            COUNT(*)
        FROM
            PLACES
        GROUP BY
            HOST_ID
        HAVING
            COUNT(*) > 1
        ) B
        ON A.HOST_ID = B.HOST_ID
ORDER BY
    ID
;
    