-- 코드를 입력하세요
WITH RECURSIVE time_range AS (
  SELECT 0 AS hour
  UNION ALL
  SELECT hour + 1
  FROM time_range
  WHERE hour < 23
)
SELECT
    a.HOUR,
    COUNT(b.animal_id)
FROM
    time_range a
    left join
        ANIMAL_OUTS b
        on a.hour = EXTRACT(HOUR FROM DATETIME)
GROUP BY
    a.hour
ORDER BY
    HOUR
;