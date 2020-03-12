# from collections import deque
#
# for tc in range(1, int(input()) + 1):
#     N, M, K, A, B = map(int, input().split())
#     a = list(map(int, input().split()))  # N 개
#     b = list(map(int, input().split()))  # M 개
#     t = list(map(int, input().split()))  # K 개
#
#     aq = [[0, 0] for _ in range(N + 1)]  # 남은 시간, 고객 번호
#     bq = [0] * (M + 1)
#
#     time, k = 0, 1  # 시간, 고객 번호
#
#     waiting = deque()
#
#     flag = False
#     ans = 0
#
#     while k <= K or flag:
#         flag = False
#         for n in range(1, N + 1):
#             if aq[n][0]:
#                 flag = True
#                 aq[n][0] -= 1
#             if not aq[n][0]:
#                 if aq[n][1]:
#                     waiting.append([n, k])
#                     aq[n][1] = 0
#                 if k <= K and t[k - 1] <= time:
#                     aq[n] = [a[n - 1], k]
#                     k += 1
#
#         for m in range(1, M + 1):
#             if bq[m]:
#                 flag = True
#                 bq[m] -= 1
#             if not bq[m]:
#                 if waiting:
#                     next_k = waiting.popleft()
#                     bq[m] = b[m - 1]
#                     if next_k[0] == A and m == B:
#                         ans += next_k[1]
#         time += 1
#     if not ans:
#         ans = -1
#     print("#%d %d" % (tc, ans))

for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))
    aq = [None] * N
    bq = [None] * M
    wait = []
    s, n, cnt = 0, 0, 0
    take = True
    while take or n < K:
        take = False
        for i in range(N):
            if aq[i]:
                take = True
                aq[i][0] -= 1
                if aq[i][0] == 0:
                    wait.append([aq[i][1], aq[i][2]])
                    aq[i] = None
            if not aq[i]:
                if n < K:
                    if t[n] <= s:
                        aq[i] = [a[i], i + 1, n + 1]
                        n += 1
        for j in range(M):
            if bq[j]:
                take = True
                bq[j] -= 1
                if bq[j] == 0:
                    bq[j] = None
            if not bq[j]:
                if wait:
                    temp = wait.pop(0)
                    bq[j] = b[j]
                    if temp[0] == A and j + 1 == B:
                        cnt += temp[1]
        s += 1

    if not cnt:
        cnt = -1
    print('#{} {}'.format(tc, cnt))