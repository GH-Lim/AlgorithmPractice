from itertools import combinations
from collections import deque
from sys import stdin

input = stdin.readline

N, M, G, R = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(N)]

yellow = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            yellow.append((i, j))


def inject(candi, G, R, com):
    global answer
    if G == R == 0:
        answer = max(answer, start(candi, com))
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

    flag = True
    while flag:
        flag = False
        temp_g = {}
        temp_r = {}
        for g in green:
            y, x = g
            for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and garden[ny][nx] != 0 and (ny, nx) not in flower\
                        and (ny, nx) not in green and (ny, nx) not in red and (ny, nx) not in temp_g:
                    flag = True
                    temp_g[(ny, nx)] = 1
        if not flag:
            break
        for r in red:
            y, x = r
            for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if (ny, nx) in temp_g:
                    flower[(ny, nx)] = 1
                    temp_g.pop((ny, nx))
                else:
                    if 0 <= ny < N and 0 <= nx < M and garden[ny][nx] != 0 and (ny, nx) not in flower\
                            and (ny, nx) not in green and (ny, nx) not in red and (ny, nx) not in temp_r:
                        temp_r[(ny, nx)] = 1
        green.update(temp_g)
        red.update(temp_r)

    return len(flower)


answer = 0
for candidate in combinations(yellow, G + R):
    inject(candidate, G, R, [])

print(answer)
