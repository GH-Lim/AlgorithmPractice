from collections import deque
from heapq import heappush, heappop
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shark = (0, 0, 2, 0)  # 좌표, 크기, 먹은 물고기 수

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = (i, j, 2, 0)
            arr[i][j] = 0
            break
    else: continue
    break

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
visited = {}

q = deque()
# heappush(q, shark)
q.append(shark)
visited[(shark[0], shark[1])] = 1
ans = 0
cnt = 0
candidates = []
while q:
    for _ in range(len(q)):
        y, x, size, eat = q.popleft()
        if eat == size:
            size += 1
            eat = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                if arr[ny][nx] == 0 or arr[ny][nx] == size:
                    # heappush(q, (ny, nx, size, eat))
                    q.append((ny, nx, size, eat))
                    visited[(ny, nx)] = 1
                elif arr[ny][nx] < size:
                    heappush(candidates, (ny, nx))
    if candidates:
        ny, nx = heappop(candidates)
        arr[ny][nx] = 0
        ans = cnt + 1
        q.clear()
        q.append((ny, nx, size, eat + 1))
        visited.clear()
        candidates.clear()
        visited[(ny, nx)] = 1
    cnt += 1

print(ans)
