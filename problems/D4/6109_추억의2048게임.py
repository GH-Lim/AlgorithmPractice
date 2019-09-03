import sys
sys.stdin = open('6109.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*N for _ in range(N)]
    if S == 'up':
        for j in range(N):
            i = 0
            while i < N:
                if board[i][j] == 0:
                    k = 1
                    while i + k < N and board[i + k][j] == 0:
                        k += 1
                    if i + k >= N:
                        break
                    board[i][j], board[i + k][j] = board[i + k][j], board[i][j]
                else:
                    k = 1
                    while i + k < N and board[i + k][j] == 0:
                        k += 1
                    if i + k >= N:
                        break
                    if board[i + k][j] == board[i][j]:
                        board[i][j] *= 2
                        board[i + k][j] = 0
                        i += 1
                    else:
                        i += 1
    elif S == 'down':
        for j in range(N):
            i = N - 1
            while i >= 0:
                if board[i][j] == 0:
                    k = 1
                    while i - k >= 0 and board[i - k][j] == 0:
                        k += 1
                    if i - k < 0:
                        break
                    board[i][j], board[i - k][j] = board[i - k][j], board[i][j]
                else:
                    k = 1
                    while i - k >= 0 and board[i - k][j] == 0:
                        k += 1
                    if i - k < 0:
                        break
                    if board[i - k][j] == board[i][j]:
                        board[i][j] *= 2
                        board[i - k][j] = 0
                        i -= 1
                    else:
                        i -= 1
    elif S == 'left':
        for i in range(N):
            j = 0
            while j < N:
                if board[i][j] == 0:
                    k = 1
                    while j + k < N and board[i][j + k] == 0:
                        k += 1
                    if j + k >= N:
                        break
                    board[i][j], board[i][j + k] = board[i][j + k], board[i][j]
                else:
                    k = 1
                    while j + k < N and board[i][j + k] == 0:
                        k += 1
                    if j + k >= N:
                        break
                    if board[i][j + k] == board[i][j]:
                        board[i][j] *= 2
                        board[i][j + k] = 0
                        j += 1
                    else:
                        j += 1
    else:  # 'right'
        for i in range(N):
            j = N - 1
            while j >= 0:
                if board[i][j] == 0:
                    k = 1
                    while j - k >= 0 and board[i][j - k] == 0:
                        k += 1
                    if j - k < 0:
                        break
                    board[i][j], board[i][j - k] = board[i][j - k], board[i][j]
                else:
                    k = 1
                    while j - k >= 0 and board[i][j-k] == 0:
                        k += 1
                    if j - k < 0:
                        break
                    if board[i][j - k] == board[i][j]:
                        board[i][j] *= 2
                        board[i][j - k] = 0
                        j -= 1
                    else:
                        j -= 1
    print('#{}'.format(tc))
    for row in board:
        for num in row:
            print(num, end=' ')
        print()
