# from itertools import combinations
# from sys import stdin
#
# input = stdin.readline
#
# N, M, G, R = map(int, input().split())
#
# garden = [list(map(int, input().split())) for _ in range(N)]
#
# yellow = []
# for i in range(N):
#     for j in range(M):
#         if garden[i][j] == 2:
#             yellow.append((i, j))
#
#
# def inject(candi, G, R, com):
#     global answer
#     if G == R == 0:
#         answer = max(answer, start(candi, com))
#         return
#     if G:
#         inject(candi, G - 1, R, com + [0])
#
#     if R:
#         inject(candi, G, R - 1, com + [1])
#
#
# def start(candi, com):
#     green = {}
#     red = {}
#     flower = {}
#     i = 1
#     for ca, ci in zip(candi, com):
#         if ci == 0:
#             green[ca] = i
#         else:
#             red[ca] = i
#
#     flag = True
#     while flag:
#         flag = False
#         for g in list(green):
#             y, x = g
#             for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < M and garden[ny][nx] != 0 and (ny, nx) not in flower\
#                         and (ny, nx) not in green and (ny, nx) not in red:
#                     flag = True
#                     green[(ny, nx)] = i + 1
#         if not flag:
#             break
#         for r in list(red):
#             y, x = r
#             for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                 ny, nx = y + dy, x + dx
#                 if (ny, nx) in green and green[(ny, nx)] == i + 1:
#                     flower[(ny, nx)] = 1
#                     green.pop((ny, nx))
#                 else:
#                     if 0 <= ny < N and 0 <= nx < M and garden[ny][nx] != 0 and (ny, nx) not in flower\
#                             and (ny, nx) not in green and (ny, nx) not in red:
#                         red[(ny, nx)] = i + 1
#         i += 1
#     return len(flower)
#
#
# answer = 0
# for candidate in combinations(yellow, G + R):
#     inject(candidate, G, R, [])
#
# print(answer)

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
    flower = 0
    sub_garden = {}
    q = deque([])
    for ca, ci in zip(candi, com):
        if ci == 0:
            sub_garden[ca] = (0, 0)
            q.append((*ca, 0, 0))
        else:
            sub_garden[ca] = (1, 0)
            q.append((*ca, 1, 0))
    flag = True
    while q:
        flag = False
        # for _ in range(len(q)):
        y, x, col, step = q.popleft()
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and garden[ny][nx] != 0:
                if (ny, nx) not in sub_garden:
                    if col == 0:
                        flag = True
                    sub_garden[(ny, nx)] = (col, step + 1)
                    q.append((ny, nx, col, step + 1))
                else:
                    if sub_garden[(ny, nx)][1] == step + 1 and sub_garden[(ny, nx)][0] != col:
                        if sub_garden[(ny, nx)][0] == 2:
                            print('?')
                        sub_garden[(ny, nx)] = (2, 0)
                        flower += 1
    print('===========')
    return flower


answer = 0
for candidate in combinations(yellow, G + R):
    inject(candidate, G, R, [])

print(answer)

