-- 문제 설명이 부족한 것 같다.
-- 반기별 데이터가 GRADE 테이블에 있다보니 평균인지, 합계인지 등... 평균이 정답이긴 하다.
SELECT
    A.EMP_NO,
    B.EMP_NAME,
    CASE
        WHEN AVG(SCORE) >= 96 THEN 'S'
        WHEN AVG(SCORE) >= 90 THEN 'A'
        WHEN AVG(SCORE) >= 80 THEN 'B'
    ELSE 'C'
    END
    AS GRADE,
    CASE
        WHEN AVG(SCORE) >= 96 THEN SAL * 0.2
        WHEN AVG(SCORE) >= 90 THEN SAL * 0.15
        WHEN AVG(SCORE) >= 80 THEN SAL * 0.1
    ELSE 0
    END
    AS BONUS
FROM
    HR_GRADE A
    INNER JOIN
        HR_EMPLOYEES B
        ON A.EMP_NO = B.EMP_NO
    INNER JOIN
        HR_DEPARTMENT C
        ON B.DEPT_ID = C.DEPT_ID
GROUP BY
    A.EMP_NO,
    B.EMP_NAME
ORDER BY
    B.EMP_NO
    
;