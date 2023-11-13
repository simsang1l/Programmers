def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    elif sum(arr1) > sum(arr2):
        answer = 1
    elif sum(arr1) < sum(arr2):
        answer = -1
    
    return answer

# 다른 사람 풀이
# arr1의 길이가 더 길거나 합이 크면 1  뒷부분은 0이 되고 or 이므로 1이됨
# 반대의 경우는 -1이 됨
# 같으면 0이 됨
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))