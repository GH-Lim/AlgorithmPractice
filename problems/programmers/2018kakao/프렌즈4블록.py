def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while True:
        temp = {}
        for i in range(m - 2):
            for j in range(n - 2):
                if board[i][j] == board[i + 1][j]== \
                    board[i][j + 1] == board[i + 1][j + 1] != '0':
                    temp.update({(i, j): 1, (i + 1, j): 1, (i, j + 1): 1, (i + 1, j + 1): 1})
        if not temp:
            break
        for k in temp:
            i, j = k


        answer += len(temp)
        for i in range(m):
            pass

    return answer

print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
