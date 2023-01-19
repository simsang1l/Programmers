# 차이 값 dictionary에 저장
## value 오름차순, key 내림차순으로 dictionary 정렬


def solution(numlist, n):
    answer = []
    sub_dict = {}
    for i in numlist:
        sub_dict[i] = abs(n - i)
    
    sub_dict = sorted(sub_dict.items(), key = lambda item: (item[1], -item[0]))
    print(sub_dict)
    answer = [key for key, value in sub_dict]
    
    return answer