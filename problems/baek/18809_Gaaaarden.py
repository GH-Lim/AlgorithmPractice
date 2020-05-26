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


def inject(candi, G, R, com):
    if G == R == 0:
        start(candi, com)
        return
    if G:
        inject(candi, G - 1, R, com + [0])

    if R:
        inject(candi, G, R - 1, com + [1])

def start(candi, com):
    green = {}
    red = {}
    flower = {}
    for ca, ci in zip(candi, com):
        if ci == 0:
            green[ca] = 1
        else:
            red[ca] = 1

    while True:
        temp = {}
        for g in green:
            pass

        for r in red:
            y, x = r
            for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
            if r in green:
                flower[r] = 1
            pass
