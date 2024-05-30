-- 1. 재귀함수를 이용해서 GENERATION 구하기
-- 2. GENERATION을 구한 GEN 테이블을 SELF JOIN하여 ID에 맞는 자식 ID 구하기(LEFT JOIN 이용함)
-- 3. LEFT JOIN 했을 때 자식 ID가 없다면(NULL이라면) 해당 ID에는 자식이 없음을 의미
-- 4. 세대별 자식이 없는 ID수 구하기. 단 LEFT JOIN을 해서 부모에 대한 ID가 중복되어 나타날 수 있으므로 중복 제거!
WITH RECURSIVE GEN AS (
    SELECT
        ID,
        PARENT_ID,
        1 AS GENERATION
    FROM
        ECOLI_DATA
    WHERE
        PARENT_ID IS NULL
    UNION ALL
    SELECT
        A.ID,
        A.PARENT_ID,
        GENERATION + 1 AS GENERATION
    FROM 
        ECOLI_DATA A -- 자식
        INNER JOIN
            GEN B -- 부모
            ON A.PARENT_ID = B.ID
)
SELECT
    COUNT(DISTINCT A.ID) AS COUNT,
    A.GENERATION
FROM
    GEN A 
    LEFT JOIN
        GEN B
        ON A.ID = B.PARENT_ID
WHERE
    B.ID IS NULL
GROUP BY
    A.GENERATION
ORDER BY
    A.GENERATION
;