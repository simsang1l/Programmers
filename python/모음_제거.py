def solution(my_string):
    answer = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    for i in vowel :
        my_string = my_string.replace(i, '')
    
    answer = my_string
    
    return answer