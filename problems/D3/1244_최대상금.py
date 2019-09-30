# import sys
# sys.stdin = open('1244.txt', 'r')
# def swap(n):
#     global max_num
#     if n == swap_cnt:
#         num_ = int(''.join(num))
#         max_num = max(num_, max_num)
#         return
#     not_swap = True
#     for i in range(len(num) - 1):
#         for j in range(i, len(num)):
#             if i != j and num[i] <= num[j]:
#                 not_swap = False
#                 num[i], num[j] = num[j], num[i]
#                 swap(n + 1)
#                 num[i], num[j] = num[j], num[i]
#     if not_swap:
#         num[-1], num[-2] = num[-2], num[-1]
#         swap(n + 1)
#         num[-1], num[-2] = num[-2], num[-1]


def swap(n, swap_num):
    global max_num
    if max_num > swap_num:
        return
    if n == swap_cnt:
        max_num = max(swap_num, max_num)
        return
    not_swap = True
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if i != j and num[i] <= num[j]:
                not_swap = False
                num[i], num[j] = num[j], num[i]
                swap(n + 1, int(''.join(num)))
                num[i], num[j] = num[j], num[i]
    if not_swap:
        num[-1], num[-2] = num[-2], num[-1]
        swap(n + 1, int(''.join(num)))
        num[-1], num[-2] = num[-2], num[-1]


for tc in range(1, int(input()) + 1):
    num, swap_cnt = input().split()
    num = list(num)
    # num = list(map(int, num))
    swap_cnt = int(swap_cnt)
    max_num = 0
    swap(0, 0)

    print('#%d %d' % (tc, max_num))
