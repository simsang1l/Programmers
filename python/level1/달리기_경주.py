# 테스트 9 ~ 테스트 13 시간초과
def solution(players, callings):
    answer = []
    
    for name in callings:
        idx = players.index(name)
        players[idx],  players[idx - 1] = players[idx - 1], players[idx]
        
    answer = players
        
    return answer

# dictionary 이용하여 값 바꾸기
def solution(players, callings):
    answer = []
    player_order = {player: idx for idx, player in enumerate(players)}
    order = {idx : player for idx, player in enumerate(players)}
        
    for name in callings :
        current = player_order[name]
        
        player_order[name] = current - 1
        player_order[order[current - 1]] = current
        
        order[current] = order[current - 1]
        order[current - 1] = name
    
    answer = list(order.values())        
        
    return answer