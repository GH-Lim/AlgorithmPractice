from collections import deque


def jump_wall(ny, nx, d):
    jy, jx = ny + dy[d], nx + dx[d]
    while 0 <= jy < n and 0 <= jx < n:
        if not maze[jy][jx]:
            return jy, jx
        jy += dy[d]
        jx += dx[d]
    return False


n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

day, time = 1, False # 낮 false 밤 true
is_valid = False
cnt = 0
q = deque([(0, 0)])
visited = {}
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while q:
    if cnt == m:
        cnt = 0
        if time:
            day += 1
        time = not time
    sub_visited = {}
    for _ in range(len(q)):
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if (ny, nx) == (n - 1, n - 1): break
            if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in sub_visited:
                if not maze[ny][nx]:
                    if not time or (ny, nx) not in visited:
                        # 낮 or 밤에는 안가본 곳만
                        q.append((ny, nx))
                        sub_visited[(ny, nx)] = 1
                        visited[(ny, nx)] = 1
                else:
                    if time:
                        temp = jump_wall(ny, nx, d)
                        if temp and temp not in visited:
                            if temp == (n - 1, n - 1): break
                            q.append(temp)
                            visited[temp] = 1
                            sub_visited[temp] = 1
        else: continue # 출구 못찾았으면
        break
    else:
        cnt += 1
        continue
    is_valid = True
    break
print(f'{day} {"moon" if time else "sun"}' if is_valid else -1)
