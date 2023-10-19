def solution(arr):
    answer = 0
    lst = []
    
    while True:
        if answer == 0 :
            lst.append(arr.copy())
            
        for i, val in enumerate(arr) :
            if val >= 50 and val % 2 == 0 :
                arr[i] = val//2
            elif val < 50 and val % 2 != 0:
                arr[i] = val*2+1
            else :
                arr[i] = val
                
        lst.append(arr.copy())
        if lst[answer] == lst[answer + 1]:
            break
        answer += 1
            
    return answer