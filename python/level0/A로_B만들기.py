def solution(before, after):
    answer = 0
    
    if sorted(before) == sorted(after):
        answer = 1
    else :
        answer = 0
    
    return answer

## 이렇게 했다가 런타임 에러 발생
# def solution(before, after):
#     answer = 0
#     b_dict = {}
#     a_dict = {}
    
#     for i in before :
#         if i not in b_dict:
#             b_dict[i] = 1
#         else :
#             b_dict[i] += 1
    
#     for i in after :
#         if i not in a_dict:
#             a_dict[i] = 1
#         else :
#             a_dict[i] += 1
            
#     for key, value in a_dict.items():
#         if a_dict[key] == b_dict[key]:
#             answer = 1
#         else : 
#             answer = 0
#             break
        
    
#     return answer