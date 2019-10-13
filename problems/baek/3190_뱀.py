from collections import deque
N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

turns = {
    0: {
        'L': 2,
        'D': 3
    },
    1: {
        'L': 3,
        'D': 2
    },
    2: {
        'L': 1,
        'D': 0
    },
    3: {
        'L': 0,
        'D': 1
    }
}
for _ in range(K):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = 2  # 사과
snake = deque()
snake.append((0, 0))
arr[0][0] = 1

v = 3
T = 0
L = int(input())
turn_info = []
for _ in range(L):
    X, turn = input().split()
    turn_info.append((int(X), turn))
turn_info.append((1e9, 'L'))
flag = False
for x, t in turn_info:
    while T < x:
        i, j = snake[0]
        ni, nj = i + di[v], j + dj[v]
        T += 1
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
            snake.appendleft((ni, nj))
            if arr[ni][nj] == 0:
                tail_y, tail_x = snake.pop()
                arr[tail_y][tail_x] = 0
            arr[ni][nj] = 1
        else:
            flag = True
            break
    if flag:
        break
    else:
        v = turns[v][t]

print(T)
