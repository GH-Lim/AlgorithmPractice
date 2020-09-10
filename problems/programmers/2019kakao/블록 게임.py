def solution(board):
    N = len(board)
    answer = 0
    for j in range(N):
        for i in range(N):
            if board[i][j]:
                break
            board[i][j] = -1

    for i in range(N):
        for j in range(N):
            num, check = checker(board, i, j)
            if check:
                answer += 1
                for x in range(j, j + check):
                    for y in range(i, N):
                        if board[y][x] == num or board[y][x] == 0 or board[y][x] == -1:
                            board[y][x] = -1
                        else:
                            break
    return answer


def checker(board, y, x):
    v = [
        (0, 0), (0, 1),
        (1, 0), (1, 1),
        (2, 0), (2, 1)
    ]
    h = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2)
    ]
    if y < len(board) - 2 and x < len(board) - 1:
        cnt = 0
        temp = 0
        for dy, dx in v:
            ny, nx = y + dy, x + dx
            if board[ny][nx] == -1:
                cnt += 1
                if cnt == 3:
                    break
            elif board[ny][nx]:
                if not temp:
                    temp = board[ny][nx]
                else:
                    if temp != board[ny][nx]:
                        break
            else:
                break
        else:
            return temp, 2

    if y < len(board) - 1 and x < len(board) - 2:
        cnt = 0
        temp = 0
        for dy, dx in h:
            ny, nx = y + dy, x + dx
            if board[ny][nx] == -1:
                cnt += 1
                if cnt == 3:
                    break
            elif board[ny][nx]:
                if not temp:
                    temp = board[ny][nx]
                else:
                    if temp != board[ny][nx]:
                        break
            else:
                break
        else:
            return temp, 3
    return 0, 0

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))