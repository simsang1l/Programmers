def solution(array):
    answer = 0
    
    # dictionary에 값과 빈도수 담기
    array_dic = {}
    for idx, num in enumerate(array):
        if num not in array_dic:
            array_dic[num] = 0
        else :
            array_dic[num] += 1
    
    answer_lst = []
    # 빈도수 비교하여 answer 만들기
    for key, value in array_dic.items():
        
        # answer_lst에 최대값에 해당하는 key 들을 담는다
        if max(array_dic.values()) == value:
            answer_lst.append(key)
            
    if len(answer_lst) > 1:
        answer = -1 
    else :
        # 리스트에 값이 한개만 담길 경우에 해당
        answer = answer_lst[0] 
        
    
    return answer