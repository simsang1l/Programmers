SELECT
    concat('/home/grep/src/', A.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT)  AS FILE_PATH
FROM
    (SELECT
        *
     FROM 
        USED_GOODS_BOARD
     ORDER BY
        VIEWS DESC
     LIMIT 1
     )A
    INNER JOIN
        USED_GOODS_FILE B
        ON A.BOARD_ID = B.BOARD_ID
ORDER BY
    FILE_ID DESC
;