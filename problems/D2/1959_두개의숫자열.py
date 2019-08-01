T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M < N:
        M, N = N, M
        A, B = B, A
    max_result = 0

    for i in range(N):
        result = 0
        for j in range(M-N+1):
            result += (A[i] * B[i+j])
        if result > max_result:
            max_result = result
    print('#{} {}'.format(tc, max_result))
