from itertools import combinations
N, M, G, R = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(N)]

yellow = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            yellow.append((i, j))

for candidate in combinations(yellow, G + R):
    pass

def inject(candi, G, R):
    pass