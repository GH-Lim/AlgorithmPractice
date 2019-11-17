def permH(k, res, plus, minus, mul, div):
    global MAX, MIN
    if k == N - 1:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return
    if plus:
        permH(k + 1, res + nums[k + 1], plus - 1, minus, mul, div)
    if minus:
        permH(k + 1, res - nums[k + 1], plus, minus - 1, mul, div)
    if mul:
        permH(k + 1, res * nums[k + 1], plus, minus, mul - 1, div)
    if div:
        permH(k + 1, int(res / nums[k + 1]), plus, minus, mul, div - 1)


for tc in range(1, int(input()) + 1):
    N = int(input())
    ops = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    MIN = 100000000
    MAX = -100000000
    permH(0, nums[0], *ops)
    print('#%d %d' % (tc, MAX - MIN))
