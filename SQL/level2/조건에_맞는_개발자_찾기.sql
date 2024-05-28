-- 비트연산자를 위해 &연산자 이용
-- SKILL_CODE가 CODE에 포함되어 있다면 &연산자를 적용했을 때 CODE와 동일한 값을 가지게 됨
-- C#과 Python 둘 다 가지는 경우가 있을 수 있어 이런 경우 동일한 행이 2개 나온다. 따라서 DISTINCT 적용!
SELECT DISTINCT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    SKILLCODES A
    INNER JOIN
        DEVELOPERS B
        ON CODE & SKILL_CODE = CODE
WHERE
    NAME IN ('C#', 'Python')
ORDER BY
    ID
;