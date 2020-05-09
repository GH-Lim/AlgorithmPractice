inf = 1e9

def solution(board):
    N = len(board)
    answer = 0
    arr = [[inf] * N for _ in range(N)]
    arr[0][0] = 0
    q = [(0, 0, 0, 0), (0, 0, 0, 1)]
    while q:
        val, y, x, arrow = q.pop()
        if y == N-1 and x == N-1:
            return val
        for dy, dx in [(0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not board[ny][nx]:
                if arrow and val + 100 < arr[ny][nx]:
                    arr[ny][nx] = val + 100
                    q.append((arr[ny][nx], ny, nx, 1))
                elif not arrow and val + 600 < arr[ny][nx]:
                    arr[ny][nx] = val + 600
                    q.append((arr[ny][nx], ny, nx, 1))
        for dy, dx in [(1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not board[ny][nx]:
                if not arrow and val + 100 < arr[ny][nx]:
                    arr[ny][nx] = val + 100
                    q.append((arr[ny][nx], ny, nx, 0))
                elif arrow and val + 600 < arr[ny][nx]:
                    arr[ny][nx] = val + 600
                    q.append((arr[ny][nx], ny, nx, 0))
        q.sort(key=lambda x: -x[0])
    return arr[N-1][N-1]

print(solution(
    [
        [0, 0, 0, 1, 0],

        [0, 1, 0, 1, 0],

        [0, 0, 0, 0, 0],

        [0, 1, 0, 1, 0],

        [0, 0, 0, 1, 0],
    ]
))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))