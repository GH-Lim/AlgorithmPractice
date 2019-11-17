from collections import deque

N, M, T = map(int, input().split())
plates = [deque([0] * M)]
for _ in range(N):
    plates.append(deque(map(int, input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = N * M
for _ in range(T):
    x, d, k = map(int, input().split())
    r = -1 if d else 1

    for i in [ii for ii in range(N + 1) if ii % x == 0]:
        plates[i].rotate(r * k)

    to_del = set()
    for i in range(1, N + 1):
        for j in range(M):
            if plates[i][j]:
                for d in range(4):
                    ny, nx = i + dy[d], j + dx[d]
                    if ny > N or ny < 1: continue
                    nx = M - 1 if nx == -1 else 0 if nx == M else nx
                    if plates[i][j] == plates[ny][nx]:
                        to_del.add((i, j))
                        break
    if to_del:
        for num in to_del:
            plates[num[0]][num[1]] = 0
            cnt -= 1
        if cnt == 0:
            break
    else:
        sum_num = 0
        for _ in range(1, N + 1):
            sum_num += sum(plates[_])
        avg_num = sum_num / cnt

        for i in range(1, N + 1):
            for j in range(M):
                if plates[i][j]:
                    if plates[i][j] > avg_num:
                        plates[i][j] -= 1
                    elif plates[i][j] < avg_num:
                        plates[i][j] += 1
result = 0
if cnt:
    for _ in range(1, N + 1):
        result += sum(plates[_])
print(result)

