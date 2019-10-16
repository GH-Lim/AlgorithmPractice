from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

R = (0, 0)
B = (0, 0)
O = (0, 0)
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            R = (i, j)
        elif board[i][j] == 'B':
            B = (i, j)
        elif board[i][j] == 'O':
            O = (i, j)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = {}


def bfs(R, B):
    q = deque([(R, B)])
    for cnt in range(1, 11):
        for _ in range(len(q)):
            r, b = q.popleft()
            visited[(r, b)] = 1
            for d in range(4):
                beads = move(r, b, d)
                if beads and beads[0] == O:
                    return cnt
                if beads and beads not in visited:
                    q.append(beads)
    return -1


def move(r, b, d):
    ry, rx = r
    by, bx = b
    r_cnt = 0
    b_cnt = 0
    while board[ry + dy[d]][rx + dx[d]] != '#':
        r_cnt += 1
        ry += dy[d]
        rx += dx[d]
        if (ry, rx) == O:
            break
    while board[by + dy[d]][bx + dx[d]] != '#':
        b_cnt += 1
        by += dy[d]
        bx += dx[d]
        if (by, bx) == O:
            return False
    if (ry, rx) == (by, bx):
        if r_cnt > b_cnt:
            ry -= dy[d]
            rx -= dx[d]
        else:
            by -= dy[d]
            bx -= dx[d]
    r = ry, rx
    b = by, bx
    return r, b


print(bfs(R, B))
