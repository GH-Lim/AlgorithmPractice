r, c, k = map(int, input().split())
r, c = r - 1, c - 1

arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())


def R_oper():
    global C
    max_j = 0
    for i in range(R):
        num_cnt = {}
        for j in range(C):
            if arr[i][j] == 0: pass
            elif arr[i][j] in num_cnt:
                num_cnt[arr[i][j]] += 1
            else:
                num_cnt[arr[i][j]] = 1
            arr[i][j] = 0
        sub_j = 0
        temp = [(val, key) for key, val in num_cnt.items()]
        for val, key in sorted(temp):
            arr[i][sub_j], arr[i][sub_j + 1] = key, val
            sub_j += 2
        max_j = max(max_j, sub_j)
    C = max(C, max_j)
    if C > 100: C = 100


def C_oper():
    global R
    max_i = 0
    for j in range(C):
        num_cnt = {}
        for i in range(R):
            if arr[i][j] == 0: pass
            elif arr[i][j] in num_cnt:
                num_cnt[arr[i][j]] += 1
            else:
                num_cnt[arr[i][j]] = 1
            arr[i][j] = 0
        sub_i = 0
        temp = [(val, key) for key, val in num_cnt.items()]
        for val, key in sorted(temp):
            arr[sub_i][j], arr[sub_i + 1][j] = key, val
            sub_i += 2
        max_i = max(max_i, sub_i)
    R = max(R, max_i)
    if R > 100: R = 100


R, C = 3, 3
ans = -1
cnt = 0
while cnt <= 100:
    if arr[r][c] == k:
        ans = cnt
        break
    if R >= C:
        R_oper()
    else:
        C_oper()
    cnt += 1

print(ans)
