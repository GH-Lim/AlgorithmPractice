from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
candidates = []
blanks = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            candidates.append((i, j))
        elif arr[i][j] == 0:
            blanks += 1
c_len = len(candidates)
ans = -1 if blanks else 0


def comb(cnt, virus, n):
    if cnt == M:
        bfs(virus)
        return
    if c_len - n < M - cnt: return
    comb(cnt + 1, virus + [candidates[n]], n + 1)
    comb(cnt, virus, n + 1)


def bfs(v):
    global ans
    visited = {}
    spread = 0
    q = deque(v)
    cnt = 0
    while q:
        cnt += 1
        if ans != -1 and cnt >= ans:
            return
        for _ in range(len(q)):
            y, x = q.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[ny][nx] != 1 and (ny, nx) not in visited:
                        visited[(ny, nx)] = 1
                        if arr[ny][nx] == 0:
                            spread += 1
                        q.append((ny, nx))
        if spread == blanks:
            ans = cnt
            return


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
comb(0, [], 0)
print(ans)
