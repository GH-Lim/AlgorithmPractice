from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))
combs = combinations(chickens, M)
result = 9999
for comb in combs:
    sum_min = 0
    for x1, y1 in homes:
        min_d = 9999
        for x2, y2 in comb:
            d = abs(x1 - x2) + abs(y1 - y2)
            if d < min_d:
                min_d = d
        sum_min += min_d
    if sum_min < result:
        result = sum_min
print(result)
