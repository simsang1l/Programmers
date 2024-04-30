SELECT
    extract(year from YM) as YEAR,
    ROUND(avg(PM_VAL1), 2) as PM10,
    ROUND(avg(PM_VAL2), 2) as `PM2.5`
FROM
    AIR_POLLUTION
WHERE
    LOCATION2 = '수원'
GROUP BY
    YEAR
ORDER BY
    YEAR
;