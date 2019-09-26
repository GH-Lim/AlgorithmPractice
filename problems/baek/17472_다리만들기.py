def find_island(y, x):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        i_map[y][x] = numbering
        for mode in range(4):
            next_y, next_x = y + dy[mode], x + dx[mode]
            if 0 <= next_y < N and 0 <= next_x < M:
                if i_map[next_y][next_x] == 1:
                    stack.append((next_y, next_x))


def bridge(y, x, n):
    for mode in range(4):
        next_y, next_x = y + dy[mode], x + dx[mode]
        cnt = 0
        while 0 <= next_y < N and 0 <= next_x < M:
            if i_map[next_y][next_x] == n:
                break
            if i_map[next_y][next_x]:
                if cnt > 1:
                    G[n - 2][i_map[next_y][next_x] - 2] = min(cnt, G[n - 2][i_map[next_y][next_x] - 2])
                break
            cnt += 1
            next_y += dy[mode]
            next_x += dx[mode]


def solve():


N, M = map(int, input().split())
i_map = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
numbering = 2
for i in range(N):
    for j in range(M):
        if i_map[i][j] == 1:
            find_island(i, j)
            numbering += 1
G = [[10]*(numbering - 2) for _ in range(numbering - 2)]

for i in range(N):
    for j in range(M):
        if i_map[i][j]:
            bridge(i, j, i_map[i][j])
visited = [0] * (numbering - 2)

