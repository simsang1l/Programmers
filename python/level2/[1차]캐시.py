# cache에 없으면 cache miss
# cache에 있다면 cache hit!

def solution(cacheSize, cities):
    answer = 0
    cities = [c.upper() for c in cities]
    cache = []
    
    if cacheSize == 0 :
        return len(cities) * 5
    else :
        for city in cities :
            if not city in cache :
                # cache miss
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else :
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
            else :
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
                
    return answer