SELECT
    MCDP_CD AS `진료과코드`,
    COUNT(*) AS `5월예약건수`
FROM
    APPOINTMENT A
WHERE
    DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY
    MCDP_CD
ORDER BY
    `5월예약건수` ,
    MCDP_CD
;