SELECT
    MEMBER_ID
    , MEMBER_NAME
    , GENDER
    , DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
FROM
    MEMBER_PROFILE
WHERE
    EXTRACT(MONTH FROM DATE_OF_BIRTH) = 3
    and GENDER = 'W'
    AND TLNO IS NOT NULL
ORDER BY
    MEMBER_ID
;