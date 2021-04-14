N, Q = map(int, input().split())
N = 2 ** N
ice_board = [list(map(int, input().split())) for _ in range(N)]
L_list = list(map(int, input().split()))

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]


def ft_rotate(y_s, x_s, l):
    n = 2 ** l
    for i in range(n // 2):
        for j in range(n // 2):
            ice_board[y_s + i][x_s + j], \
            ice_board[y_s + j][x_s + n - 1 - i], \
            ice_board[y_s + n - 1 - i][x_s + n - 1 - j], \
            ice_board[y_s + n - 1 - j][x_s + i] \
                = ice_board[y_s + n - 1 - j][x_s + i], \
                  ice_board[y_s + i][x_s + j], \
                  ice_board[y_s + j][x_s + n - 1 - i], \
                  ice_board[y_s + n - 1 - i][x_s + n - 1 - j]


def near_ice(y, x):
    cnt = 0
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and ice_board[ny][nx] > 0:
            cnt += 1
    return cnt


def firestorm(l):
    for i in range(0, N, 2 ** l):
        for j in range(0, N, 2 ** l):
            ft_rotate(i, j, l)
    melt = []
    for i in range(N):
        for j in range(N):
            if ice_board[i][j] > 0 and near_ice(i, j) < 3:
                melt.append((i, j))
    for i, j in melt:
        ice_board[i][j] -= 1


def dfs(y, x):
    cnt = 1
    stack = [(y, x)]
    visited[y][x] = 1
    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and ice_board[ny][nx] and not visited[ny][nx]:
                stack.append((ny, nx))
                cnt += 1
                visited[ny][nx] = 1
    return cnt


for L in L_list:
    firestorm(L)
ans = 0
for i in range(N):
    for j in range(N):
        if ice_board[i][j] and not visited[i][j]:
            ans = max(ans, dfs(i, j))
print(sum(sum(ice_board, [])))
print(ans)
