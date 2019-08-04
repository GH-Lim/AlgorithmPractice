import sys

sys.stdin = open('input_1959.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M < N:
        M, N = N, M
        A, B = B, A
    max_result = -100000
    for i in range(M-N+1):
        sum_nums = 0
        for j in range(N):
            sum_nums += A[j] * B[j+i]
        if sum_nums > max_result:
            max_result = sum_nums
    print('#{} {}'.format(tc, max_result))
