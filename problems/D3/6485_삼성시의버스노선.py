T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0 for _ in range(5000)]
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            bus_stop[i - 1] += 1
    P = int(input())
    result = [0 for _ in range(P)]
    for i in range(P):
        C = int(input())
        result[i] = str(bus_stop[C - 1])
    print('#{} {}'.format(tc, ' '.join(result)))
