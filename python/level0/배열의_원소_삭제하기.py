def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    answer = arr
    return answer


# 다른 사람 풀이
# not in을 활용하는 방법도 있다
def solution(arr, delete_list):
    
    return [i for i in arr if i not in delete_list]