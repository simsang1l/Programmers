-- 형질 1번이나 3번을 가지면서 2번은 가지지 않는 개수 찾기
-- 형질 1번은 2진수로 변환했을 때 1을 나타내는 숫자
-- 형질 2번은 2진수로 변환했을 떄 2를 나타내는 숫자
-- 형질 3번은 2진수로 변환했을 떄 4를 나타내는 숫자
-- 비트연산자 &를 적용했을 때 형질을 가지고 있다면 0이 아닌 숫자가 나옴

SELECT
    COUNT(*) AS COUNT
FROM
    ECOLI_DATA A
WHERE
    (1 & GENOTYPE != 0
    OR 4 & GENOTYPE != 0)
    AND 2 & GENOTYPE = 0  
;