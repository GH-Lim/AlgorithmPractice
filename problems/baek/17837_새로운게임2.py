N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

board = [[list() for _ in range(N)] for _ in range(N)]
drones = []
for i in range(K):
    y, x, d = map(int, input().split())
    drones.append([y - 1, x - 1, d])
    board[y - 1][x - 1].append(i)

ans = -1
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
for cnt in range(1, 1001):
    for i in range(K):
        y, x, d = drones[i]
        k = 0
        if len(board[y][x]) > 1:
            for j in range(len(board[y][x])):
                if board[y][x][j] == i:
                    k = j
                    break
        temp = board[y][x][k:]
        board[y][x][k:] = []
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 2:
            if arr[ny][nx] == 1:
                temp.reverse()
        else:
            d = 2 if d == 1 else 1 if d == 2 else 4 if d == 3 else 3
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 2:
                if arr[ny][nx] == 1:
                    temp.reverse()
            else:
                ny, nx = y, x
            drones[i][2] = d
        for num in temp:
            drones[num][0], drones[num][1] = ny, nx

        board[ny][nx].extend(temp)
        if len(board[ny][nx]) >= 4:
            ans = cnt
            break
    else:
        continue
    break
print(ans)
