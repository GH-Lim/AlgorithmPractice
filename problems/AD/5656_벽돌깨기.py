def permH(k, li):
    global b_bricks
    if b_bricks == ans:
        return
    if k == N:
        b_bricks = max(drop(li), b_bricks)
        return
    for i in range(W):
        permH(k + 1, li + [i])


def drop(li):
    Arr = [row[:] for row in arr]
    cnt = 0
    for j in li:
        i = 0
        while i != H:
            if Arr[i][j] != 0:
                break
            i += 1
        if i == H:
            continue
        if Arr[i][j] == 1:
            Arr[i][j] = 0
            cnt += 1
            continue
        stack = [(i, j, Arr[i][j])]
        Arr[i][j] = 0
        cnt += 1
        while stack:
            y, x, val = stack.pop()
            for v in range(1, val):
                for m in range(4):
                    ny, nx = y + dy[m] * v, x + dx[m] * v
                    if 0 <= ny < H and 0 <= nx < W:
                        if Arr[ny][nx] > 0:
                            if Arr[ny][nx] > 1:
                                stack.append((ny, nx, Arr[ny][nx]))
                            Arr[ny][nx] = 0
                            cnt += 1
        fall(Arr)
    return cnt


def fall(ar):
    for j in range(W):
        find_top = False
        top_idx = 0
        for i in range(H - 1, -1, -1):
            if not find_top and ar[i][j]: continue
            elif find_top and ar[i][j] == 0: continue

            if not find_top and ar[i][j] == 0:
                top_idx = i
                find_top = True
            elif find_top and ar[i][j]:
                ar[top_idx][j], ar[i][j] = ar[i][j], ar[top_idx][j]
                top_idx -= 1


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    b_bricks = 0
    ans = 0
    for j in range(W):
        for i in range(H - 1, -1, -1):
            if arr[i][j]:
                ans += 1
            else:
                continue
    permH(0, [])
    ans -= b_bricks
    print('#%d %d' % (tc, ans))
