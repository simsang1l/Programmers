def solution(my_string):
    answer = ''
    string_dict = {}

    for i in my_string :
        # keyword dictionary에 몇번 나왔는지 세기
        if i in string_dict :
            string_dict[i] += 1
        else :
            string_dict[i] = 1
        
        # 2번 이상 나올경우 아무 값도 출력하지 않는다
        if string_dict[i] < 2:
            answer += i
        else :
            answer += ''
        
        
    
    return answer