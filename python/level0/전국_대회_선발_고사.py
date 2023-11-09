def solution(rank, attendance):
    answer = 0
    lst = []
    for idx, (r, a) in enumerate(zip(rank, attendance)):
        if a :
            lst.append([r, idx])
    lst = sorted(lst)[:3]
    
    print(lst)
    for i in range(len(lst)):
        if i == 0 :
            answer += (10000*lst[i][1])
        elif i == 1 :
            answer += (100*lst[i][1])
        elif i == 2:
            answer += lst[i][1]
            
    return answer