C, D, M = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(C)]


def buy(k, sub_M, m):
    global M
    M = max(M, sub_M)
    if k == C or m == 0:
        return
    for i in range(C):
        if m >= f[i][day - 1] and f[i][day - 1] < f[i][day]:
            g = f[i][day] - f[i][day - 1]
            buy(k + 1, sub_M + g * (m // f[i][day - 1]), m % f[i][day - 1])


for day in range(1, D):
    buy(0, M, M)

print(M)
