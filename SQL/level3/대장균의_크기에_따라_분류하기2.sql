SELECT
    ID,
    CASE
        WHEN RK <= 0.25 THEN 'CRITICAL'
        WHEN RK <= 0.5 THEN 'HIGH'
        WHEN RK <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM(
    SELECT
        PERCENT_RANK() OVER(ORDER BY SEQ) AS RK,
        A.*
    FROM(
        SELECT
            ROW_NUMBER() OVER(ORDER BY SIZE_OF_COLONY DESC) AS SEQ,
            A.*
        FROM
            ECOLI_DATA A
        ) A
) A
ORDER BY
    ID
;

-- 다른 사람 풀이
-- PERCENT_RANL를 사용하지 않는 풀이
-- 전체 데이터 건수를 이용하여 PERCENT_RANK 계산
-- PERCENTAGE값이 코드들 마다 차이가 있는데... 어떤게 맞는지 잘 모르겠다
SELECT ID 
, CASE WHEN ec_rank.rank_per <= 0.25 THEN 'CRITICAL'
  WHEN ec_rank.rank_per >0.25 AND ec_rank.rank_per <= 0.5 THEN 'HIGH'
  WHEN ec_rank.rank_per >0.5 AND ec_rank.rank_per <= 0.75 THEN 'MEDIUM'
  ELSE 'LOW' END AS COLONY_NAME
FROM
(
 SELECT *
 , ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) / (COUNT(*) OVER ()) AS rank_per
 FROM ECOLI_DATA
) ec_rank
ORDER BY ID ASC;