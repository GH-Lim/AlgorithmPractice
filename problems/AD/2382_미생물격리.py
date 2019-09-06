import sys
from pprint import pprint
sys.stdin = open('2382.txt', 'r')

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        x, y, n, d = map(int, input().split())
        arr[x][y] = [[n, d]]
    for i in range(M):
        visited = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if arr[x][y] and not visited[x][y]:
                    if len(arr[x][y]) > 1:
                        arr[x][y].sort(reverse=True)
                        A = list(zip(*arr[x][y]))
                        sn = sum(A[0])
                        sd = A[1][0]
                        arr[x][y] = [[sn, sd]]
                    stack = []
                    sn, sd = arr[x][y].pop()
                    stack.append((x, y, sn, sd))
                    visited[x][y] = 1
                    while stack:
                        x, y, n, d = stack.pop()
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
                            if n // 2 == 0:
                                continue
                            else:
                                if len(arr[nx][ny]) == 1:
                                    nn, nd = arr[nx][ny].pop()
                                    stack.append((nx, ny, nn, nd))
                                d = 1 if d == 2 else 2 if d == 1 else 3 if d == 4 else 4
                                arr[nx][ny] = [[n // 2, d]]
                                visited[nx][ny] = 1
                        else:
                            if not visited[nx][ny]:
                                if len(arr[nx][ny]) > 1:
                                    arr[nx][ny].sort(reverse=True)
                                    A = list(zip(*arr[nx][ny]))
                                    nn = sum(A[0])
                                    nd = A[1][0]
                                    stack.append((nx, ny, nn, nd))
                                elif len(arr[nx][ny]) == 1:
                                    nn, nd = arr[nx][ny].pop()
                                    stack.append((nx, ny, nn, nd))
                                arr[nx][ny] = [[n, d]]
                                visited[nx][ny] = 1
                            else:
                                arr[nx][ny].append([n, d])
                else:
                    visited[x][y] = 1
    cell_num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for cell in arr[i][j]:
                    cell_num += cell[0]
    print(cell_num)


# dx = [0, -1, 1, 0, 0]
# dy = [0, 0, 0, -1, 1]
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     arr = [[[] for _ in range(N)] for _ in range(N)]
#     for _ in range(K):
#         x, y, n, d = map(int, input().split())
#         arr[x][y].append([n, d])
#     stack = []
#     for i in range(M):
#         visited = [[0] * N for _ in range(N)]
#         for x in range(N):
#             for y in range(N):
#                 if arr[x][y] and not visited[x][y]:
#                     if len(arr[x][y]) > 1:
#                         arr[x][y].sort(reverse=True)
#                         A = list(zip(*arr[x][y]))
#                         n = sum(A[0])
#                         d = A[1][0]
#                         arr[x][y] = [[n, d]]
#                     stack.append(arr[x][y].pop())
#                     visited[x][y] = 1
#                     while stack:
#                         n, d = stack.pop()
#                         nx = x + dx[d]
#                         ny = y + dy[d]
#
#                         if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
#                             if n // 2 == 0:
#                                 continue
#                             else:
#                                 d = 1 if d == 2 else 2 if d == 1 else 3 if d == 4 else 4
#                                 arr[nx][ny] = [[n // 2, d]]
#                                 visited[nx][ny] = 1
#                         else:
#                             if not visited[nx][ny]:
#                                 if len(arr[nx][ny]) > 1:
#                                     arr[nx][ny].sort(reverse=True)
#                                     A = list(zip(*arr[nx][ny]))
#                                     nn = sum(A[0])
#                                     nd = A[1][0]
#                                     arr[nx][ny] = [[nn, nd]]
#                                     stack.append(arr[nx][ny].pop())
#                                 elif len(arr[nx][ny]) == 1:
#                                     stack.append(arr[nx][ny].pop())
#                                 arr[nx][ny].append([n, d])
#                                 visited[nx][ny] = 1
#                             else:
#                                 arr[nx][ny].append([n, d])
#                         x = nx
#                         y = ny
#     cell_num = 0
#     for i in range(N):
#         for j in range(N):
#             for cell in arr[i][j]:
#                 cell_num += cell[0]
#     print(cell_num)


#
# dx = [0, -1, 1, 0, 0]
# dy = [0, 0, 0, -1, 1]
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     cells = [list(map(int, input().split())) for _ in range(K)]
