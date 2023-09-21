def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        for i in range(s, e+1):
            if i == 0 :
                if i % 1 == 0 :
                    arr[i] = arr[i] + 1
            else : 
                if i % k == 0 :
                    arr[i] = arr[i] + 1
                
    answer = arr
        
    return answer