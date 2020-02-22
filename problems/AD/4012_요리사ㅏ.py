from itertools import combinations
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_diff = 50000
    combs = list(combinations(list(range(N)), N // 2))
    for i in range(len(combs) // 2):  # 이터툴즈로 만든 comb 는 좌우 대칭
        A = 0
        B = 0
        for j in range(N//2):
            for k in range(N//2):
                A += arr[combs[i][j]][combs[i][k]]
                B += arr[combs[-1-i][j]][combs[-1-i][k]]
        min_diff = min(abs(A-B), min_diff)

    print('#%d %d' % (tc, min_diff))
