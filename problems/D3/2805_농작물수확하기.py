T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    gain = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2 - i, N//2 + i + 1):
                gain += farm[i][j]
        else:
            for j in range(i - N//2, N//2 * 3 - i + 1):
                gain += farm[i][j]
    print('#{} {}'.format(tc, gain))
