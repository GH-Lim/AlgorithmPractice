from collections import deque
import sys

input = sys.stdin.readline

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
visited = [[[[0, 0] for _ in range(m)] for __ in range(n)] for ___ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while q:
    if cnt == m:
        cnt = 0
        if time:
            day += 1
        time = not time
    for _ in range(len(q)):
        y, x = q.popleft()
        if (y, x) == (n - 1, n - 1): break
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            # if (ny, nx) == (n - 1, n - 1): break
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx][cnt][time]:
                if not maze[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx][cnt][time] = 1
                else:
                    if time:
                        temp = jump_wall(ny, nx, d)
                        if temp:
                            if not visited[temp[0]][temp[1]][cnt][time]:
                                q.append(temp)
                                visited[temp[0]][temp[1]][cnt][time] = 1
    else:
        cnt += 1
        continue
    is_valid = True
    break
print(f'{day} {"moon" if time else "sun"}' if is_valid else -1)
