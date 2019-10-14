N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
stack = [(r, c, d)]
cnt = 1
while stack:
    y, x, d = stack.pop()
    arr[y][x] = 2
    for i in range(4):
        d = 3 if d == 0 else d - 1
        ny, nx = y + dy[d], x + dx[d]
        if arr[ny][nx] == 0:
            stack.append((ny, nx, d))
            cnt += 1
            break
    else:
        ny, nx = y + dy[(d + 2) % 4], x + dx[(d + 2) % 4]
        if arr[ny][nx] == 1:
            break
        stack.append((ny, nx, d))
        if arr[ny][nx] == 0:
            cnt += 1
print(cnt)
