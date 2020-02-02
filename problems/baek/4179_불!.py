# from collections import deque
# from sys import stdin
#
# input = stdin.readline
#
# R, C = map(int, input().split())
# maze = [input() for _ in range(R)]
#
# fire = set()
# visited = set()
# jh = deque()
# for i in range(R):
#     for j in range(C):
#         if maze[i][j] == 'J':
#             jh.append((i, j))
#             visited.add((i, j))
#         elif maze[i][j] == 'F':
#             fire.add((i, j))
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# cnt = 0
# while jh:
#     cnt += 1
#     n_fire = set()
#     for fy, fx in fire:
#         for d in range(4):
#             nfy, nfx = fy + dy[d], fx + dx[d]
#             if 0 <= nfy < R and 0 <= nfx < C and maze[nfy][nfx] != '#':
#                 if (nfy, nfx) in fire: continue
#                 n_fire.add((nfy, nfx))
#     fire = fire.union(n_fire)
#     for _ in range(len(jh)):
#         jy, jx = jh.popleft()
#         for d in range(4):
#             njy, njx = jy + dy[d], jx + dx[d]
#             if 0 <= njy < R and 0 <= njx < C:
#                 if maze[njy][njx] != '#' and (njy, njx) not in visited:
#                     if (njy, njx) in fire: continue
#                     jh.append((njy, njx))
#                     visited.add((njy, njx))
#             else:
#                 break
#         else: continue
#         break
#     else: continue
#     break
# else:
#     cnt = 'IMPOSSIBLE'
# print(cnt)

from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int, input().split())
a = [list(input().strip()) for _ in range(R)]
dist = [[0]*C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        if a[i][j] == 'J':
            sx, sy = i, j
        elif a[i][j] == 'F':
            q.append((i, j, 1))
            dist[i][j] = 1

def bfs():
    q.append((sx, sy, 0))
    dist[sx][sy] = 1
    while q:
        x, y, f = q.popleft()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                if f:
                    continue
                print(dist[x][y])
                return
            if not dist[nx][ny] and a[nx][ny] != '#':
                q.append((nx, ny, f))
                dist[nx][ny] = dist[x][y]+1
    print("IMPOSSIBLE")

bfs()


# 출처: https://rebas.kr/744 [PROJECT REBAS]