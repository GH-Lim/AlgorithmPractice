def solution(m, n, board):
    answer = 0
    board = [''.join(row) for row in map(list, zip(*board))]
    for row in board:
        print(row)
    print(board)
    for i in range(m - 2):
        for j in range(n - 2):
            temp = {}
            if board[i][j] == board[i + 1][j]== \
                board[i][j + 1] == board[i + 1][j + 1] != '0':
                temp.update({(i, j), (i + 1, j)})

    return answer