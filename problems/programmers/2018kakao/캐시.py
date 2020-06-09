from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            idx = cache.index(city)
            del cache[idx]
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
        cache.append(city)
    return answer