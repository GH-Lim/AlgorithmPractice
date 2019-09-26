def comb(i, cnt):
    global ans
    global count
    if cnt == 3:
        arr = [row[:] for row in o_arr]
        count = 0
        n = N
        while arr:
            shoot(arr, n)
            n -= 1
        ans = max(count, ans)
        return
    if i == M - 1:
        return
    archer[i + 1] = 1
    comb(i + 1, cnt + 1)
    archer[i + 1] = 0
    comb(i + 1, cnt)


def shoot(arr, n):
    global count
    is_change = False
    for i in range(M):
        if archer[i]:  # (N, i) 궁수
            flag = False
            for j in range(1, D + 1):
                k = n - 1                           # k = N - 1  ~  N - D  ~  N - 1
                for l in range(i - j + 1, i + j):   # l = i - D + 1 ~ i + D - 1
                    if 0 <= l < M and 0 <= k:
                        if arr[k][l]:
                            if arr[k][l] == 1:
                                arr[k][l] = 2
                            flag = True
                            break
                    if l < i: k -= 1
                    else: k += 1
                if flag:
                    is_change = True
                    break
    if is_change:
        for i in range(n):
            for j in range(M):
                if arr[i][j] == 2:
                    arr[i][j] = 0
                    count += 1
    arr.pop()


N, M, D = map(int, input().split())
o_arr = [list(map(int, input().split())) for _ in range(N)]

archer = [0] * M
ans = 0
count = 0
comb(-1, 0)

print(ans)
