from collections import deque

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [0, -1, 1, -1, 1, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    num_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                num_cnt += 1
                num = 0
                for d in range(8):
                    ny, nx = i + dy[d], j + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == '*':
                        num += 1
                board[i][j] = num
    visited = set()
    zeros = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and (i, j) not in visited:
                zeros += 1
                q = deque([(i, j)])
                visited.add((i, j))
                while q:
                    y, x = q.popleft()
                    for d in range(8):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N:
                            if (ny, nx) not in visited and board[ny][nx] != '*':
                                visited.add((ny, nx))
                                if board[ny][nx] == 0:
                                    q.append((ny, nx))
    print('#%d %d' %(tc, zeros + num_cnt - len(visited)))