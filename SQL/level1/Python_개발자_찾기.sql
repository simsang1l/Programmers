SELECT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPER_INFOS
WHERE
    SKILL_1 = 'Python'
    OR SKILL_2 = 'Python'
    OR SKILL_3 = 'Python'
ORDER BY
    ID
;

-- 다른 사람 풀이
-- 일반적으로 알고있는 IN과 반대의 방법도 가능했던거군??
SELECT id, email, first_name, last_name
FROM developer_infos
WHERE 'PYTHON' IN (skill_1, skill_2, skill_3)
ORDER BY id