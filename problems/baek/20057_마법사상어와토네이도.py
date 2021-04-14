N = int(input())
sandbox = [list(map(int, input().split())) for _ in range(N)]
y, x = N // 2, N // 2
step = 0
dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
div = [(0, 2, 5), (-1, 1, 10), (1, 1, 10),
       (-2, 1, 7), (2, 1, 7),
       (-2, 2, 2), (2, 2, 2),
       (-3, 1, 1), (3, 1, 1)]
ans = 0


def tornado(i, j, v):
    sand = sandbox[i][j]
    out = 0
    moved = 0
    sandbox[i][j] = 0
    for dv, l, p in div:
        ni, nj = i + dy[(v + dv) % 8] * l, j + dx[(v + dv) % 8] * l
        moved += sand * p // 100
        if 0 <= ni < N and 0 <= nj < N:
            sandbox[ni][nj] += sand * p // 100
        else:
            out += sand * p // 100
    ni, nj = i + dy[v], j + dx[v]
    if 0 <= ni < N and 0 <= nj < N:
        sandbox[ni][nj] += sand - moved
    else:
        out += sand - moved
    return out


d = 0
while (y, x) != (0, 0):
    go = step // 2 + 1
    for i in range(1, go + 1):
        y, x = y + dy[d], x + dx[d]
        ans += tornado(y, x, d)
        if (y, x) == (0, 0):
            break
    d = (d + 2) % 8
    step += 1
print(ans)
