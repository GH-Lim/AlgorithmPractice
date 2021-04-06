N, M, G, R = map(int, input().split())
ans = 0
arr = [list(map(int, input().split())) for _ in range(N)]

candidates = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            candidates.append((i, j))


from itertools import combinations
from _collections import deque

GREEN = 0
RED = 1
Flower = 2
for comb in combinations(candidates, G + R):
    for green, red in zip(combinations(comb, G), reversed(list(combinations(comb, R)))):
        flowers = 0
        q = deque()
        visited = [[-1] * M for _ in range(N)]
        for y, x in green:
            q.append((y, x))
            visited[y][x] = (GREEN, 0)
        for y, x in red:
            q.append((y, x))
            visited[y][x] = (RED, 0)

        while q:
            y, x = q.popleft()
            if visited[y][x] == Flower:
                continue
            color, cnt = visited[y][x]
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N) or not (0 <= nx < M) or visited[ny][nx] == Flower:
                    continue
                if visited[ny][nx] == -1 and arr[ny][nx] != 0:
                    q.append((ny, nx))
                    visited[ny][nx] = color, cnt + 1
                elif visited[ny][nx] != -1 and visited[ny][nx][0] != color and visited[ny][nx][1] == cnt + 1:
                    visited[ny][nx] = Flower
                    flowers += 1
        ans = max(ans, flowers)

print(ans)