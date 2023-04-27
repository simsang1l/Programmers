SELECT
    BOOK_ID
    , DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d')
FROM
    BOOK
WHERE
    EXTRACT(YEAR FROM PUBLISHED_DATE) = '2021'
    AND CATEGORY = '인문'
ORDER BY
    PUBLISHED_DATE