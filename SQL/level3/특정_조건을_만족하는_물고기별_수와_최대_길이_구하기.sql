SELECT
    FISH_COUNT,
    MAX_LENGTH,
    FISH_TYPE
FROM(
    SELECT
        COUNT(*) AS FISH_COUNT,
        MAX(LENGTH) AS MAX_LENGTH,
        AVG(LENGTH) AS AVG_LENGTH,
        FISH_TYPE
    FROM(
        SELECT
            ID,
            FISH_TYPE,
            IFNULL(LENGTH, 10 ) AS LENGTH,
            TIME
        FROM
            FISH_INFO
    ) A
    GROUP BY
        FISH_TYPE
) A
WHERE
    AVG_LENGTH >= 33
ORDER BY
    FISH_TYPE
;

-- 다른사람 풀이
-- HAVING절 쓰는게 있었지...
select count(id) as fishcount, max(length) as maxlength, fish_type
from fish_info
group by fish_type
having avg(ifnull(length,10)) >= '33'
order by fish_type
;
