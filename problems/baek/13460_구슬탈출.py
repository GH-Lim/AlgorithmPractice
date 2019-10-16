from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

R = [0, 0]
B = [0, 0]
O = [0, 0]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            R = [i, j]
        elif board[i][j] == 'B':
            B = [i, j]
        elif board[i][j] == 'O':
            O = [i, j]

visited = {}


def bfs(R, B):
    q = deque([[R, B]])
    for _ in range(10):
        for _ in range(len(q)):
            r, b = q.popleft()


def up():
    pass
def down():
    pass
def left():
    pass
def right():
    pass