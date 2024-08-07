SELECT
    USER_ID,
    NICKNAME,
    CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2),
    CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8, 4))
FROM
    (SELECT
        WRITER_ID,
        COUNT(*) AS CNT
     FROM
        USED_GOODS_BOARD
     GROUP BY
        WRITER_ID
     HAVING CNT >= 3) A
    INNER JOIN
        USED_GOODS_USER B
        ON A.WRITER_ID = B.USER_ID
ORDER BY
    USER_ID DESC
;