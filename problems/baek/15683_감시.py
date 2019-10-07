def cctv(y, x, c, n):
    global ans
    if n == len(cameras) - 1:
        ans = min(ans, cnt)
        return
    if c == 1:
        for i in range(4):
            go(y, x, i)
            cctv(*cameras[n + 1], n + 1)
            back(y, x, i)
    if c == 2:
        for i in range(2):
            go(y, x, 2 * i)
            go(y, x, (2 * (i + 1)) % 4)
            cctv(*cameras[n + 1], n + 1)
            back(y, x, 2 * i + 1)
            back(y, x, (2 * (i + 1) + 1) % 4)
    if c == 3:
        for i in range(4):
            go(y, x, i % 4)
            go(y, x, (i + 1) % 4)
            cctv(*cameras[n + 1], n + 1)
            back(y, x, i % 4)
            back(y, x, (i + 1) % 4)
    if c == 4:
        for i in range(4):
            go(y, x, i % 4)
            go(y, x, (i + 1) % 4)
            go(y, x, (i + 2) % 4)
            cctv(*cameras[n + 1], n + 1)
            back(y, x, i % 4)
            back(y, x, (i + 1) % 4)
            back(y, x, (i + 2) % 4)
    if c == 5:
        for i in range(4):
            go(y, x, i)
        cctv(*cameras[n + 1], n + 1)
        for i in range(4):
            back(y, x, i)


def go(y, x, d):
    global cnt
    ny, nx = y + dy[d], x + dx[d]
    while 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
        if office[ny][nx] == 0:
            if visited[ny][nx] == 0:
                cnt -= 1
            visited[ny][nx] += 1
        ny, nx = ny + dy[d], nx + dx[d]


def back(y, x, d):
    global cnt
    ny, nx = y + dy[d], x + dx[d]
    while 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
        if office[ny][nx] == 0:
            visited[ny][nx] -= 1
            if visited[ny][nx] == 0:
                cnt += 1
        ny, nx = ny + dy[d], nx + dx[d]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
office = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
ans = N * M
cameras = []
for n in range(N):
    for m in range(M):
        if office[n][m] == 0:
            cnt += 1
        elif office[n][m] != 6:
            cameras.append((n, m, office[n][m]))
cameras.append((0, 0, 0))
cctv(*cameras[0], 0)

print(ans)
