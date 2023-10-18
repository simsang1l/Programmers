def solution(todo_list, finished):
    answer = []
    for problem, finish in zip(todo_list, finished):
        if finish == 0 :
            answer.append(problem)
        
    return answer