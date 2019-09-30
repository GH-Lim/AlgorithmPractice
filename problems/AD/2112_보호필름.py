import sys
sys.stdin = open('2112.txt', 'r')
# 0 은 0 투입, 1 은 1 투입, 2 는 놔둔다.
# def inject(d, p):
#     global flag
#     global cnt
#     global min_cnt
#     if min_cnt == 1:
#         return
#     if p == 2:
#         pass
#     else:
#         cnt += 1
#         if cnt >= min_cnt:
#             return
#         film[d] = injection[p]
#     if d == D - 1:
#         if check():
#             min_cnt = cnt if cnt < min_cnt else min_cnt
#         return
#     inject(d + 1, 2)
#
#     inject(d + 1, 1)
#     cnt -= 1
#     film[d + 1] = sub_film[d + 1]
#
#     inject(d + 1, 0)
#     cnt -= 1
#     film[d + 1] = sub_film[d + 1]
#
#
# def check():
#     for j in range(W):
#         k = 1
#         for i in range(D - 1):
#             if film[i][j] == film[i + 1][j]:
#                 k += 1
#             else:
#                 k = 1
#             if k >= K:
#                 break
#         if k < K:
#             return False
#     return True
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     D, W, K = map(int, input().split())
#     film = [list(map(int, input().split())) for _ in range(D)]
#     sub_film = [film[_][:] for _ in range(D)]
#     injection = [
#         [0] * W,
#         [1] * W
#     ]
#
#     flag = False
#     cnt = 0
#     min_cnt = 999
#     if check():
#         min_cnt = 0
#     else:
#         inject(0, 2)
#         inject(0, 1)
#         cnt -= 1
#         film[0] = sub_film[0]
#         inject(0, 0)
#     print('#{} {}'.format(tc, min_cnt))

def inject(d, p, cnt):
    global min_cnt
    if min_cnt == 1:
        return
    if p == 2:
        pass
    else:
        film[d] = injection[p]
    if d == D - 1:
        if check():
            min_cnt = min(min_cnt, cnt)
        return
    inject(d + 1, 2, cnt)

    if cnt + 1 < min_cnt:
        inject(d + 1, 1, cnt + 1)
        film[d + 1] = sub_film[d + 1]
    if cnt + 1 < min_cnt:
        inject(d + 1, 0, cnt + 1)
        film[d + 1] = sub_film[d + 1]


def check():
    for j in range(W):
        k = 1
        for i in range(D - 1):
            if film[i][j] == film[i + 1][j]:
                k += 1
            else:
                k = 1
            if k >= K:
                break
        if k < K:
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    sub_film = [film[_][:] for _ in range(D)]
    injection = [
        [0] * W,
        [1] * W
    ]
    min_cnt = 999
    inject(-1, 2, 0)
    print('#{} {}'.format(tc, min_cnt))
