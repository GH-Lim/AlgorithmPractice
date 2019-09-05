from collections import deque


def bfs(a, b):
    x, y = a, b
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    union = []
    sum_num = 0
    while queue:
        x, y = queue.popleft()
        union.append((x, y))
        sum_num += A[x][y]
        for mode in range(4):
            nx, ny = x + dx[mode], y + dy[mode]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and L <= abs(A[x][y] - A[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    population = sum_num // len(union)
    for x, y in union:
        A[x][y] = population


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, L, R = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
result = 0
while True:
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt == N * N:
        break
    result += 1
print(result)
