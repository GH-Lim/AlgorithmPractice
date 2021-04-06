from _collections import deque
from heapq import heappush, heappop

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

baby = tuple()
shark = 2
eat = 0
ans = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            baby = (i, j)
            arr[i][j] = 0

q = deque([baby])
visited = {}
visited[baby] = 1
candidate = []
cnt = 0
while q:
    if eat == shark:
        shark += 1
        eat = 0
    for _ in range(len(q)):
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < N) or not (0 <= nx < N) or (ny, nx) in visited:
                continue
            if arr[ny][nx] > shark:
                continue
            if arr[ny][nx] == 0 or arr[ny][nx] == shark:
                q.append((ny, nx))
            elif arr[ny][nx] < shark:
                heappush(candidate, (ny, nx))
            visited[(ny, nx)] = 1
    if candidate:
        i, j = baby = heappop(candidate)
        arr[i][j] = 0
        eat += 1
        ans += cnt + 1
        cnt = 0
        q = deque([baby])
        visited = {}
        visited[baby] = 1
        candidate = []
        continue
    cnt += 1

print(ans)