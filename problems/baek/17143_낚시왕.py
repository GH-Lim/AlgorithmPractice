def direction(r, c, s, d):
    if d == 1 or d == 2:
        s %= 2 * R - 2
        if d == 1:
            s = -s
        r += s
        while r < 1 or r > R:
            if r < 1:
                r = 2 - r
                d = 2
            if r > R:
                r = 2 * R - r
                d = 1
    else:
        s %= 2 * C - 2
        if d == 4:
            s = -s
        c += s
        while c < 1 or c > R:
            if c > C:
                c = 2 * C - c
                d = 4
            if c < 1:
                c = 2 - c
                d = 3
    return r, c, d


R, C, M = map(int, input().split())
king = 0
arr = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
sharks = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
while True:
    while sharks:
        r, c, s, d, z = sharks.pop()
        if len(arr[r][c]) == 0:
            arr[r][c].append([r, c, s, d, z])
        else:
            if arr[r][c][0][4] < z:
                arr[r][c][0] = [r, c, s, d, z]
    king += 1
    for i in range(1, R + 1):
        if len(arr[i][king]):
            cnt += arr[i][king].pop()[4]
            break
    if king == C:
        break

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if len(arr[i][j]) == 0: continue
            elif len(arr[i][j]) == 1:
                r, c, s, d, z = arr[i][j].pop()
                r, c, d = direction(r, c, s, d)
                sharks.append([r, c, s, d, z])

print(cnt)
