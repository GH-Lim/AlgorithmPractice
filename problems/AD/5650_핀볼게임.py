import sys
sys.stdin = open('5650.txt', 'r')


def move(d, x, y):
    global score
    while 1:
        x += dx[d]
        y += dy[d]
        if not 0 <= x < N or not 0 <= y < N:
            turn_around()
            return
        if board[x][y] == 0:
            continue
        if d == 0:
            if board[x][y] == 1 or board[x][y] == 2 or board[x][y] == 5:
                turn_around()
                return
            elif board[x][y] == 3:
                d = turn_right(d)
            elif board[x][y] == 4:
                d = turn_left(d)
            elif board[x][y] == -1:
                return
            elif board[x][y] == 0:
                continue
            else:
                for point in WH[board[x][y]]:
                    if (x, y) != point:
                        x = point[0]
                        y = point[1]
                    else:
                        continue
        elif d == 1:
            if board[x][y] == 2 or board[x][y] == 3 or board[x][y] == 5:
                turn_around()
                return
            elif board[x][y] == 4:
                d = turn_right(d)
            elif board[x][y] == 1:
                d = turn_left(d)
            elif board[x][y] == -1:
                return
            elif board[x][y] == 0:
                continue
            else:
                for point in WH[board[x][y]]:
                    if (x, y) != point:
                        x = point[0]
                        y = point[1]
                    else:
                        continue
        elif d == 2:
            if board[x][y] == 3 or board[x][y] == 4 or board[x][y] == 5:
                turn_around()
                return
            elif board[x][y] == 1:
                d = turn_right(d)
            elif board[x][y] == 2:
                d = turn_left(d)
            elif board[x][y] == -1:
                return
            elif board[x][y] == 0:
                continue
            else:
                for point in WH[board[x][y]]:
                    if (x, y) != point:
                        x = point[0]
                        y = point[1]
                    else:
                        continue
        elif d == 3:
            if board[x][y] == 1 or board[x][y] == 4 or board[x][y] == 5:
                turn_around()
                return
            elif board[x][y] == 2:
                d = turn_right(d)
            elif board[x][y] == 3:
                d = turn_left(d)
            elif board[x][y] == -1:
                return
            elif board[x][y] == 0:
                continue
            else:
                for point in WH[board[x][y]]:
                    if (x, y) != point:
                        x = point[0]
                        y = point[1]
                    else:
                        continue


def turn_around():
    global score
    score *= 2
    score += 1


def turn_left(d):
    global score
    d = (d + 3) % 4
    score += 1
    return d


def turn_right(d):
    global score
    d = (d + 1) % 4
    score += 1
    return d


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    WH = {
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }
    for i in range(N):
        for j in range(N):
            if board[i][j] == 6:
                WH[6].append((i, j))
            elif board[i][j] == 7:
                WH[7].append((i, j))
            elif board[i][j] == 8:
                WH[8].append((i, j))
            elif board[i][j] == 9:
                WH[9].append((i, j))
            elif board[i][j] == 10:
                WH[10].append((i, j))
    max_score = 0
    for d in range(4):
        for i in range(N):
            flag = 1
            for j in range(N):
                if flag and board[i][j] == 0:
                    flag = 0
                    score = 0
                    game_over = False
                    move(d, i, j)
                    if max_score < score:
                        max_score = score
                elif board[i][j] != 0:
                    flag = 1
    print('#{} {}'.format(tc, max_score))
