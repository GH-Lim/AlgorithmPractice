def solution(board):
    N = len(board)
    answer = 0

    for j in range(N):
        for i in range(N):
            if board[i][j]:
                break
            board[i][j] = 'x'

def block_check(board, y, x):
    v = [
        (0, 0), (0, 1),
        (1, 0), (1, 1),
        (2, 0), (2, 1)
    ]
    h = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
    ]

    if y + 2 < len(board) and x + 1 < len(board):
        for dy, dx in v:
            ny, nx = y + dy, x + dx
            if 'x'
            if board[ny][nx] == 'x':



print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))