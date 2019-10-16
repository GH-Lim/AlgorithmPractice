dice = [0] * 6
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for k in commands:
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < N and 0 <= ny < M:
        if k == 1:
            dice[0], dice[5], dice[2], dice[4] = dice[4], dice[0], dice[5], dice[2]
        elif k == 2:
            dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]
        elif k == 3:
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
        else:
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
        x += dx[k]
        y += dy[k]
        if arr[x][y]:
            dice[2] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[2]
        print(dice[0])

'''
index info
[0] : 윗면
[2] : 바닥
동 : [0][5][2][4] => [4][0][5][2]
서 : [0][5][2][4] => [5][2][4][0]
북 : [0][1][2][3] => [1][2][3][0]
남 : [0][1][2][3] => [3][0][1][2]
'''