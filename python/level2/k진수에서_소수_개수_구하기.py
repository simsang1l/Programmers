"""
1. k진수로 변환
2. 소수의 개수 세기
"""

def is_prime_number(num):
    num = int(num)
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
    
def change(num, k):
    rev_base = ''
    
    while num > 0:
        num, mod = divmod(num, k)
        rev_base  += str(mod)
        
    return rev_base[::-1]
    
    
def solution(n, k):
    answer = 0
    
    changed_n = change(n, k)
    
    lst = changed_n.split('0')
    print(lst)
    for i in lst:
        if i != '':
            if is_prime_number(i):
                answer += 1
    
    
    return answer


# 다른 사람 풀이
# 깔끔해 보여서 가져와봤다
import math;

def convertNotation(srcNum : int, dstNotation : int) -> str:
    dstStr = "";

    while (srcNum > 0):
        (srcNum, dstDigit) = divmod(srcNum, dstNotation);
        dstStr = str(dstDigit) + dstStr;

    return dstStr;


def checkPrime(num: int) -> int:
    if (num == 1):
        return -1;

    """
    # for divisor in range(2, math.ceil(math.sqrt(num))):
    for divisor in range(2, num):
        if (num % divisor == 0):
            return -1;
    """

    divisor = 2;

    while (divisor ** 2 <= num):
        if (num % divisor == 0):
            return -1;

        divisor += 1;

    return num;

def solution(n : int, k : int) -> int:
    answer = 0;
    primeSet = set();
    pList = convertNotation(n, k).split("0");


    for curP in pList:
        # print(checkPrime(int(curP)));

        if (not curP):
            continue;

        if (curP in primeSet):
            answer += 1;
            continue;

        primeResult = checkPrime(int(curP));

        if (primeResult != -1):
            primeSet.add(primeResult);
            answer += 1;

    return answer;


solution(437674, 3)