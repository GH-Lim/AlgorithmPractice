from collections import deque

for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))  # N 개
    b = list(map(int, input().split()))  # M 개
    t = list(map(int, input().split()))  # K 개

    aq = [[0, 0] for _ in range(N + 1)]  # 남은 시간, 고객 번호
    bq = [0] * (M + 1)

    time, k = 0, 1  # 시간, 고객 번호

    waiting = deque()

    flag = False
    ans = 0

    while k <= K or flag:
        flag = False
        for n in range(1, N + 1):
            if aq[n][0]:
                flag = True
                aq[n][0] -= 1
            if not aq[n][0]:
                if aq[n][1]:
                    waiting.append([n, aq[n][1]])
                    aq[n][1] = 0
                if k <= K and t[k - 1] <= time:
                    aq[n] = [a[n - 1], k]
                    k += 1

        for m in range(1, M + 1):
            if bq[m]:
                flag = True
                bq[m] -= 1
            if not bq[m]:
                if waiting:
                    next_k = waiting.popleft()
                    bq[m] = b[m - 1]
                    if next_k[0] == A and m == B:
                        ans += next_k[1]
        time += 1
    if not ans:
        ans = -1
    print("#%d %d" % (tc, ans))
