def comb(k, pre, arr):
    global cnt
    if k == n:
        cnt += 1
        return
    for i in range(pre, x[k] + 1):
        comb(k + 1, i, arr + i*(10**k))


for tc in range(int(input())):
    n = int(input())

    x = list(map(int, input().split()))
    x.sort()
    cnt = 0
    comb(0, 1, 0)
    print(n*cnt % 1000000007)
