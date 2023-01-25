def solution(numbers, direction):
    answer = []
    if direction == 'right':
        numbers.insert(0, numbers[-1])
        # 인덱스 -1인 데이터 뽑기(제거?)
        numbers.pop(-1)
        
    elif direction == 'left':
        # insert를 썼었는데 -1자리에 적용하면 한칸 밀리는것 같음..
        numbers.append(numbers[0])
        # 인덱스 0인 데이터 뽑기(제거?)
        numbers.pop(0)
        
    answer = numbers
    
    return answer