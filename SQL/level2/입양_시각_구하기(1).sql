SELECT
    EXTRACT(HOUR FROM DATETIME) AS DT,
    COUNT(*)
FROM
    ANIMAL_OUTS
WHERE
    EXTRACT(HOUR FROM DATETIME) BETWEEN 9 AND 19
GROUP BY 
    DT
ORDER BY
    DT
;