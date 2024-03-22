-- 코드를 입력하세요
SELECT
    ANIMAL_TYPE,
    CASE
        WHEN NAME IS NULL THEN 'No name'
        else NAME
    end ,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
order by
    ANIMAL_ID
;