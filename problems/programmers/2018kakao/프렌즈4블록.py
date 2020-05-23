def solution(m, n, board):
    answer = 0
    board = list(''.join(row) for row in map(list, zip(*board)))
    while True:
        temp = {}
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != '0' and board[i][j] == board[i + 1][j] == \
                        board[i][j + 1] == board[i + 1][j + 1]:
                    v = board[i][j]
                    temp.update({(i, j): v, (i + 1, j): v, (i, j + 1): v, (i + 1, j + 1): v})
        if not temp:
            break
        for k, v in temp.items():
            i, j = k
            board[i] = board[i][:j] + '0' + board[i][j + 1:]
        for i in range(n):
            board[i] = board[i].replace('0', '').zfill(m)
        answer += len(temp)

    return answer


# print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(
    solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"])
)