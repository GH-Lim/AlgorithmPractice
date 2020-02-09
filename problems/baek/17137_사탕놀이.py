def comb(k, pre):
    global cnt
    if k == n:
        cnt += 1
        return
    for i in range(pre, x[k] + 1):
        comb(k + 1, i)


for tc in range(int(input())):
    n = int(input())

    x = list(map(int, input().split()))
    x.sort()
    cnt = 0
    comb(0, 1)
    print(n*cnt % 1000000007)
