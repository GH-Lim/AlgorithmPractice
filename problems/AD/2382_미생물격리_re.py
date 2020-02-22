import sys
sys.stdin = open('2382.txt', 'r')


dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    micros = [list(map(int, input().split())) for _ in range(K)]
    cell_arr = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        for __ in range(len(micros)):
            y, x, A, d = micros.pop()
            ny, nx = y + dy[d], x + dx[d]
            if ny == 0 or ny == N - 1 or nx == 0 or nx == N - 1:
                d = 1 if d == 2 else 2 if d == 1 else 3 if d == 4 else 4  # 방향은 반대로
                cell_arr[ny][nx].append([ny, nx, A//2, d])  # 수는 반감
            else:
                cell_arr[ny][nx].append([ny, nx, A, d])

        for i in range(N):
            for j in range(N):
                if len(cell_arr[i][j]) == 0:
                    continue
                elif len(cell_arr[i][j]) == 1:
                    micros.append(cell_arr[i][j].pop())
                else:
                    cell_arr[i][j].sort(key=lambda a: a[2], reverse=True)
                    d = cell_arr[i][j][0][3]
                    A = sum([micro[2] for micro in cell_arr[i][j]])
                    micros.append([i, j, A, d])
                    cell_arr[i][j] = []

    ans = sum([micro[2] for micro in micros])
    print('#%d %d' % (tc, ans))
