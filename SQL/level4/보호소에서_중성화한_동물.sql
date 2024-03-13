SELECT
    A.ANIMAL_ID,
    A.ANIMAL_TYPE,
    A.NAME
FROM
    ANIMAL_INS A
    INNER JOIN
        ANIMAL_OUTS B
        ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE
    A.SEX_UPON_INTAKE LIKE 'Intact%'
    and (B.SEX_UPON_OUTCOME like 'Neutered%' or B.SEX_UPON_OUTCOME like 'Spayed%')
order by
    A.ANIMAL_ID
;