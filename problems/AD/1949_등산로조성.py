import sys
sys.stdin = open('1949.txt', 'r')


def dfs(y, x, k, cnt):
    global ans
    ans = max(ans, cnt)
    for v in range(4):
        ny, nx = y + dy[v], x + dx[v]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if arr[y][x] > arr[ny][nx]:
                visited[ny][nx] = 1
                dfs(ny, nx, k, cnt + 1)
                visited[ny][nx] = 0
            else:
                if k and arr[y][x] - 1 >= arr[ny][nx] - K:
                    temp = arr[ny][nx]
                    arr[ny][nx] = arr[y][x] - 1
                    visited[ny][nx] = 1
                    dfs(ny, nx, False, cnt + 1)
                    visited[ny][nx] = 0
                    arr[ny][nx] = temp


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    top_val = max(sum(arr, []))
    tops = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top_val:
                tops.append((i, j))
    ans = 0
    for top in tops:
        y, x = top
        visited[y][x] = 1
        dfs(y, x, True, 1)
        visited[y][x] = 0
    print('#%d %d' % (tc, ans))
