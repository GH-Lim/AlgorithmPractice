def cctv(x, y, c):
    if c == 1:


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cameras = []
for n in range(N):
    for m in range(M):
        if office[n][m] != 0 or office[n][m] != 6:
            cameras.append((n, m, office[n][m]))
