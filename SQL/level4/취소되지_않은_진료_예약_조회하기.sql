SELECT
    APNT_NO,
    PT_NAME,
    A.PT_NO,
    A.MCDP_CD,
    DR_NAME,
    APNT_YMD
FROM
    APPOINTMENT A 
    INNER JOIN 
        DOCTOR D
        ON A.MDDR_ID = D.DR_ID
        AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
        AND APNT_CNCL_YN = 'N'
        AND A.MCDP_CD = 'CS'
    INNER JOIN
        PATIENT P
        ON A.PT_NO = P.PT_NO
ORDER BY
    APNT_YMD
;