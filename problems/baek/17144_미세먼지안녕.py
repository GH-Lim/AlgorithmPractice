from collections import deque
R, C, T = map(int, input().split())

arr = [deque(map(int, input().split())) for _ in range(R)]

cleaner = []
dusts = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] > 0:
                dusts.append((i, j, arr[i][j]))
            else:
                cleaner.append(i)
            arr[i][j] = 0
    # 먼지 확산
    while dusts:
        y, x, v = dusts.pop()
        cnt = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if ny == cleaner[0] or ny == cleaner[1]:
                    if nx == 0:
                        continue
                arr[ny][nx] += v // 5
                cnt += 1
        arr[y][x] += v - cnt * (v // 5)

    # 청정기 작동
    # 위쪽
    r = cleaner[0]
    temp = arr[r].pop()
    temp2 = arr[0].popleft()
    arr[r].appendleft(0)
    while r != 1:
        r -= 1
        arr[r][C - 1], temp = temp, arr[r][C - 1]
    arr[0].append(temp)
    while r != cleaner[0]:
        arr[r][0], temp2 = temp2, arr[r][0]
        r += 1

    # 아래쪽
    r = cleaner[1]
    temp = arr[r].pop()
    temp2 = arr[R - 1].popleft()
    arr[r].appendleft(0)
    while r != R - 2:
        r += 1
        arr[r][C - 1], temp = temp, arr[r][C - 1]
    arr[R - 1].append(temp)
    while r != cleaner[1]:
        arr[r][0], temp2 = temp2, arr[r][0]
        r -= 1

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j]:
            ans += arr[i][j]
print(ans)
