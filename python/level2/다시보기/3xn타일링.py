# 점화식이 잘 이해가 안간다..하ㅏㅎ..

# f(n) = 가로의 길이가 n인 타일을 채울 수 있는 경우의 수
# f(4) = (n - 2단계의 경우의수) x (n = 2일 때 경우의 수) + 2
#      = f(2) x 3 + 2 = 11
# f(n) = f(n-2) x 3 + f(n-4) x 2 ... f(2)x2 + 2
# n = 4일때 나오는 특수한 경우
def solution(n):
    answer = [0,3,11]
    index = int(n/2)
    if n % 2 != 0: return 0
    if index < 3: return answer[index]

    for i in range(3, index+1):
    	# answer[i:j] -> answer에서 index가 i인 원소부터 j-1인 원소까지의 sub-array
        answer.append((3*answer[i-1]+sum(answer[1:i-1])*2+2)%1000000007)

    return answer[index]

# 다른 사람 풀이 
def solution(n):
    if n % 2:
        return 0
    front = back = 1
    for _ in range(n//2):
        front, back = back, (4*back - front) % 1000000007
    return back