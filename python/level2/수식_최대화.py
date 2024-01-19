from re import split
from itertools import permutations

def solution(expression):
    values = []

    for priority in permutations(['*', '+', '-'], 3):
        operands = list(map(int, split('[\*\+\-]', expression)))
        operators = [c for c in expression if c in '*+-']

        for op in priority:
            while op in operators:
                i = operators.index(op)

                if op == '*':
                    v = operands[i] * operands[i+1]
                elif op == '+':
                    v = operands[i] + operands[i+1]
                else:
                    v = operands[i] - operands[i+1]
                
                # 피연산자 리스트를 업데이트 합니다.
                operands[i] = v
                operands.pop(i+1)

                # 연산자 리스트를 업데이트 합니다.
                operators.pop(i)
        
        values.append(operands[0]) # 어차피 값은 1개 남는다! 
        
    return max(abs(v) for v in values) # 우선순위(priority) 경우의 수별 값이 values에 저장되어 있음