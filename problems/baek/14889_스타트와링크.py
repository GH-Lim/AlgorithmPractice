from itertools import combinations


N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

comb = list(combinations(range(N), N//2))
min_diff = 999999
for i in range(len(comb) // 2):
    team_1 = comb[i]
    team_2 = [i for i in range(N) if i not in team_1]
    perm_1 = combinations(team_1, 2)
    perm_2 = combinations(team_2, 2)
    abil_1 = 0
    abil_2 = 0
    for x, y in perm_1:
        abil_1 += ability[x][y]
        abil_1 += ability[y][x]
    for x, y in perm_2:
        abil_2 += ability[x][y]
        abil_2 += ability[y][x]
    diff = abs(abil_1 - abil_2)
    min_diff = diff if min_diff > diff else min_diff
print(min_diff)