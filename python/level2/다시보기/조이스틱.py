# 테스트 3, 4, 5, 7, 11, 12, 13, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27 실패
def solution(name):
    answer = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length_alpha = len(alphabet)
    
    for idx, val in enumerate(name) :
        # 각 글자별 조작 횟수
        stat = 0
        alpha = 'A'
        
        # 상하로 움직이기
        for i in range(length_alpha) :
            if alphabet[i] == val :
                # 역순으로 이동할 때가 더 빠를 수 있다. 이 점을 고려
                if i <= length_alpha//2 :                    
                    stat = i
                else :
                    stat = length_alpha - i
                
        # 좌우로 움직이기
        ## 현재있는 상태에서 왼쪽으로 가야하는가 오른쪽으로 가야하는가?
        # 오른을 먼저보자
            # 오른쪽을 봤을 때 알파벳을 변경해야 한다면 오른쪽으로 이동
        # 왼쪽으로 가야할때는?
            # 오른쪽을 봤을 때 알파벳을 변경할 필요가 없다.
            # 왼쪽을 보니 알파벳을 변경할 필요가 있다.
            # 근데 for문은 오른쪽으로만 가는데?
            # 이동으로 횟수를 취급하지 않고 넘어가기?
        if idx + 1 != len(name) and name[idx+1] == 'A':
            answer += stat
            continue
        elif idx + 1 == len(name):
            answer += stat
        else :
            answer += (stat + 1)
    
    return answer

# 좌우로 이동하는걸 보완 해야함
    # BAB 이런 형태 처럼 안거쳐도 되는 경우
    # AABBA 이런 형태 처럼 중간에서 시작할 때
    # BBBABAAA 안거쳐도 되는경우가 여러개일 때
    # 이 정도는 해봐야할듯