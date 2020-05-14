N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

def divide(x, y, d1, d2, ans):
    while True:
        while True:
            lx, ly, rx, ry = x + d1, y - d1, x + d2, y + d2
            if rx == n-1 or ry == n:
                break
            bx, by = x + d1 + d2, y - d1 + d2
            if bx >= n or by >= n or by < 0:
                break
            ans = min(ans, find_min(x, y, lx, ly, rx, ry, by))
            d2 += 1
        d1 += 1
        if x + d1 == n-1 or y - d1 == -1:
            break
        d2 = 1

    return ans

def find_min(x, y, lx, ly, rx, ry, by):
    cnt1, cnt2, cnt3, cnt4, d = 0, 0, 0, 0, 0
    for i in range(lx):
        for j in range(y+1):
            if [i, j] == [x + d, y - d]:
                d += 1
                break
            cnt1 += a[i][j]

    d = 1
    for i in range(rx+1):
        for j in range(n-1, y, -1):
            if [i, j] == [x + d, y + d]:
                d += 1
                break
            cnt2 += a[i][j]

    d = 0
    for i in range(lx, n):
        for j in range(by):
            if [i, j] == [lx + d, ly + d]:
                d += 1
                break
            cnt3 += a[i][j]

    d = 1
    for i in range(rx+1, n):
        for j in range(n-1, by-1, -1):
            if [i, j] == [rx + d, ry - d]:
                d += 1
                break
            cnt4 += a[i][j]

    cnt5 = nsum - cnt1 - cnt2 - cnt3 - cnt4
    max_cnt = max(cnt1, cnt2, cnt3, cnt4, cnt5)
    min_cnt = min(cnt1, cnt2, cnt3, cnt4, cnt5)
    return max_cnt - min_cnt

n = int(input())

a, nsum = [], 0
for _ in range(n):
    row = list(map(int, input().split()))
    nsum += sum(row)
    a.append(row)

ans = 100000
for i in range(n-2):
    for j in range(1, n-1):
        d1, d2 = 1, 1
        ans = divide(i, j, d1, d2, ans)
print(ans)