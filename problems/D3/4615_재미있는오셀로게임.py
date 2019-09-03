import sys
sys.stdin = open('4615.txt', 'r')
from collections import deque


def put_stone(a, b, color):
    board[a][b] = color
    cnt[color-1] += 1
    if color == 1:
        opponent = 2
    else:
        opponent = 1
    for mode in range(8):
        if board[a+dx[mode]][b+dy[mode]] == opponent:
            i = 2
            queue = deque()
            queue.append(a+dx[mode])
            queue.append(b+dy[mode])
            while 0 < a + i * dx[mode] <= N and 0 < b + i * dy[mode] <= N:
                if board[a+i*dx[mode]][b+i*dy[mode]] == color:
                    while queue:
                        board[queue.popleft()][queue.popleft()] = color
                        cnt[color-1] += 1
                        cnt[opponent-1] -= 1
                    break
                elif board[a+i*dx[mode]][b+i*dy[mode]] == opponent:
                    queue.append(a+i*dx[mode])
                    queue.append(b+i*dy[mode])
                    i += 1
                else:
                    break
        else:
            continue


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0]*(N+2) for _ in range(N+2)]
    board[N//2+1][N//2] = 1
    board[N//2][N//2+1] = 1
    board[N//2+1][N//2+1] = 2
    board[N//2][N//2] = 2
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    cnt = [2, 2]
    for _ in range(M):
        put_stone(*map(int, input().split()))

    print('#{} {} {}'.format(tc, cnt[0], cnt[1]))
