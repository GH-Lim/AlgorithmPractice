from collections import deque

N = int(input())

arr = [list(input()) for _ in range(N)]
wood = []
end = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            wood.append([i, j])
        elif arr[i][j] == 'E':
            end.append([i, j])

woods = deque([wood])
cnt = 0
while woods:
    cnt += 1
    for i in

# from collections import deque
# from sys import stdin
#
# input = stdin.readline
#
#
# def out(x, y):
#     return x < 0 or x >= n or y < 0 or y >= n
#
#
# def check(x, y):
#     if out(x, y) or a[x][y] == '1':
#         return False
#     else:
#         return True
#
#
# def one(x, y, z, dx, dy):
#     if not out(x + dx, y + dy) and a[x + dx][y + dy] != '1' and dist[x][y][z] == -1:
#         q.append((x, y, z))
#         dist[x][y][z] = dist[x - dx][y - dy][z] + 1
#
#
# def three(x, y, z, nx, ny, dx, dy):
#     if not out(nx, ny) and dist[nx][ny][z] == -1:
#         if a[nx][ny] != '1' and a[nx - dx][ny - dy] != '1' and a[nx + dx][ny + dy] != '1':
#             q.append((nx, ny, z))
#             dist[nx][ny][z] = dist[x][y][z] + 1
#
#
# def rotate(x, y, z):
#     for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1):
#         nx, ny = x + dx, y + dy
#         if not check(nx, ny):
#             return
#     if dist[x][y][not z] == -1:
#         q.append((x, y, not z))
#         dist[x][y][not z] = dist[x][y][z] + 1
#
#
# def bfs():
#     while q:
#         x, y, z = q.popleft()
#         mx, my = 0, 0
#         if z:
#             mx = 1
#         else:
#             my = 1
#         if a[x][y] == 'E' and a[x - mx][y - my] == 'E' and a[x + mx][y + my] == 'E':
#             print(dist[x][y][z])
#             return
#         if z:
#             one(x - 1, y, z, -1, 0)
#             one(x + 1, y, z, 1, 0)
#             three(x, y, z, x, y + 1, 1, 0)
#             three(x, y, z, x, y - 1, 1, 0)
#             rotate(x, y, z)
#         else:
#             one(x, y - 1, z, 0, -1)
#             one(x, y + 1, z, 0, 1)
#             three(x, y, z, x + 1, y, 0, 1)
#             three(x, y, z, x - 1, y, 0, 1)
#             rotate(x, y, z)
#     print(0)
#
#
# n = int(input())
# a = [list(input().strip()) for _ in range(n)]
# v = []
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 'B':
#             v.append((i, j))
# x, y = v[1]
# _x, _y = v[0]
# z = _x != x
# q = deque()
# dist = [[[-1, -1] for _ in range(n)] for _ in range(n)]
# q.append((x, y, z))
# dist[x][y][z] = 0
# bfs()
#
# 출처: https: // rebas.kr / 774[PROJECTREBAS]