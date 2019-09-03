def solve(k):
    global wall
    global safe_area
    global ans
    if wall == 3:
        temp = safe_area
        visited = [[0] * M for _ in range(N)]
        for v in virus:
            spread(*v, visited)
        if safe_area > ans:
            ans = safe_area
        safe_area = temp
        return
    elif k == len(zeros):
        return
    else:
        S[k] = 1
        build_wall(*zeros[k])
        wall += 1
        solve(k + 1)
        destroy(*zeros[k])
        wall -= 1
        S[k] = 0
        solve(k + 1)


def build_wall(x, y):
    field[x][y] = 1
def destroy(x, y):
    field[x][y] = 0


def spread(x, y, v):
    global safe_area
    for mode in range(4):
        next_x = x + dx[mode]
        next_y = y + dy[mode]
        if 0 <= next_x < N and 0 <= next_y < M:
            if field[next_x][next_y] == 0 and not v[next_x][next_y]:
                v[next_x][next_y] = 1
                safe_area -= 1
                if safe_area <= ans:
                    return
                spread(next_x, next_y, v)


N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
zeros = []
virus = []
wall = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            zeros.append((i, j))
        elif field[i][j] == 2:
            virus.append((i, j))
safe_area = len(zeros)
S = [0] * safe_area
safe_area -= 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
solve(0)
print(ans)
