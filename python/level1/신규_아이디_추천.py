import re

def solution(new_id):
    # step 1
    new_id = new_id.lower()
    
    # step 2
    pattern = re.compile('[^a-z0-9\-_.]')
    new_id = pattern.sub('', new_id)
    
    # step 3
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # step 4
    new_id = new_id.strip('.')
    
    # step 5
    if new_id == '':
        new_id += 'a'
    
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')
    
    # step 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    answer = new_id
    
    return answer

# 다른사람 풀이
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer