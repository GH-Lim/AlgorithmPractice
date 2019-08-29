import sys
sys.stdin = open('input_shuffle.txt', 'r')


def check_sort(k, cnt):
    global result
    if k > cnt or result != 6:
        return
    if cards == sort or cards == rev_sort:
        result = k
    for i in range(1, N):
        shuffle(i)
        check_sort(k + 1, cnt)
        rev_shuffle(i)


def shuffle(x):
    if x == 0:
        return
    shuffle(x - 1)
    if x < N//2:
        for i in range(x):
            swap(N//2 - x + 2*i, N//2 - x + 2*i + 1)
    else:
        for i in range(N - x):
            swap(x - N//2 + 2*i, x - N//2 + 2*i + 1)


def rev_shuffle(x):
    if x == 0:
        return
    if x < N//2:
        for i in range(x):
            swap(N//2 - x + 2*i, N//2 - x + 2*i + 1)
    else:
        for i in range(N - x):
            swap(x - N//2 + 2*i, x - N//2 + 2*i + 1)
    rev_shuffle(x - 1)


def swap(a, b):
    cards[a], cards[b] = cards[b], cards[a]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    sort = sorted(cards)
    rev_sort = list(reversed(sort))
    result = 6
    for i in range(6):
        if result != 6:
            break
        check_sort(0, i)
    if result == 6:
        result = -1
    print('#{} {}'.format(tc, result))
