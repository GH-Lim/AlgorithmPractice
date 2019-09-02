import sys
sys.stdin = open('input_shuffle.txt', 'r')


from collections import deque
from copy import deepcopy, copy
# def check_sort(k, cnt):
#     global result
#     if k > cnt or result != 6:
#         return
#     if cards == sort or cards == rev_sort:
#         result = k
#     for i in range(1, N):
#         shuffle(i)
#         check_sort(k + 1, cnt)
#         rev_shuffle(i)
def check_sort():
    queue = deque()
    temp = cards
    queue.append(temp)
    step = 0
    if temp == sort or temp == rev_sort:
        return step
    while queue:
        step += 1
        if step > 5:
            return -1
        for _ in range(len(queue)):
            temp = queue.popleft()
            for i in range(1, N):
                shuffle(i, temp)
                if temp == sort or temp == rev_sort:
                    return step
                queue.append(list(temp))
                rev_shuffle(i, temp)




# def shuffle(x, c):
#     if x == 0:
#         return
#     shuffle(x - 1, c)
#     if x < N//2:
#         for i in range(x):
#             swap(N//2 - x + 2*i, N//2 - x + 2*i + 1, c)
#     else:
#         for i in range(N - x):
#             swap(x - N//2 + 2*i, x - N//2 + 2*i + 1, c)
def shuffle(x, c):
    temp = c
    k = 0
    while k <= x:
        if k < N//2:
            for i in range(k):
                swap(N // 2 - k + 2 * i, N // 2 - k + 2 * i + 1, temp)
        else:
            for i in range(N - k):
                swap(k - N // 2 + 2 * i, k - N // 2 + 2 * i + 1, temp)
        k += 1


# def rev_shuffle(x, c):
#     if x == 0:
#         return
#     if x < N//2:
#         for i in range(x):
#             swap(N//2 - x + 2*i, N//2 - x + 2*i + 1, c)
#     else:
#         for i in range(N - x):
#             swap(x - N//2 + 2*i, x - N//2 + 2*i + 1, c)
#     rev_shuffle(x - 1, c)
def rev_shuffle(x, c):
    temp = c
    k = x
    while k >= 0:
        if k < N//2:
            for i in range(k):
                swap(N // 2 - k + 2 * i, N // 2 - k + 2 * i + 1, temp)
        else:
            for i in range(N - k):
                swap(k - N // 2 + 2 * i, k - N // 2 + 2 * i + 1, temp)
        k -= 1


def swap(a, b, c):
    c[a], c[b] = c[b], c[a]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    sort = sorted(cards)
    rev_sort = list(reversed(sort))
    # result = 6
    # for i in range(6):
    #     if result != 6:
    #         break
    #     check_sort(0, i)
    # if result == 6:
    #     result = -1
    # shuffle(1,cards)
    # print(cards)
    result = check_sort()
    print('#{} {}'.format(tc, result))
