def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for i in range(len(num_list)):
        if i % 2 == 0 :
            odd += num_list[i]
        else :
            even += num_list[i]
    answer = max(odd, even)
    
    return answer

# 다른 사람 풀이
# list의 slice이용할 수 있겠군
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))