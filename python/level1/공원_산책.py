def solution(park, routes):
    answer = []
    start_x = 0
    start_y = 0
    
    for i_idx, i in enumerate(park):
        for j_idx, j in enumerate(i) :
            if j == 'S':
                start_x = j_idx
                start_y = i_idx
                break 
                
    for val in routes:
        current_x = start_x
        current_y = start_y
        
        for idx in range(int(val[2])) :
            if val[0] == 'E' and current_x != len(park[0]) - 1 and park[current_y][current_x + 1] != 'X':
                current_x += 1
                if idx == int(val[2]) - 1:
                    start_x = current_x        
                    
            elif val[0] == 'W' and current_x != 0 and park[current_y][current_x-1] != 'X':
                current_x -= 1
                if idx == int(val[2]) - 1:
                    start_x = current_x
            
            elif val[0] == 'S' and current_y != len(park) - 1 and park[current_y + 1][current_x] != 'X':
                current_y += 1
                if idx == int(val[2]) - 1:
                    start_y = current_y
                    
            elif val[0] == 'N' and current_y != 0 and park[current_y - 1][current_x] != 'X':
                current_y -= 1
                if idx == int(val[2]) - 1:
                    start_y = current_y
            
    answer = [start_y, start_x]
        
    return answer

# 다른 사람 풀이
## 전부 이해가 되진 않는다...

class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction]
        x, y = self.x + (i * distance), self.y + (j * distance)
        # 벗어나는 경우
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
            return park
        # 장애물을 만나는 경우
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]:
            return park
        park[self.x][self.y] = "O"
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park

    # 시작 위치 찾기
    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park)

    dog = Dog(x, y)

    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]