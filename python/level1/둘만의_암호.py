def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in skip :
        if i in alphabet:
            alphabet = alphabet.replace(i, '')
        
    new_alphabet = list(alphabet)
    l = len(new_alphabet)
    
    for val in s :
        idx = new_alphabet.index(val)
        answer += (new_alphabet[(idx + index) % l])
    
    return answer