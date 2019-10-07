import sys
sys.stdin = open('1244.txt', 'r')
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


# def swap(n, swap_num, num_list):
#     global max_num
#     if n == swap_cnt:
#         max_num = max(swap_num, max_num)
#         return
#
#     not_swap = True
#     not_dup = True
#     for i in range(n, len(num) - 1):
#         for j in range(i + 1, len(num)):
#             if num_list[i] < num_list[j] == max(num_list[i + 1:]):
#                 not_swap = False
#                 sub_num = num_list[:]
#                 sub_num[i], sub_num[j] = sub_num[j], sub_num[i]
#                 swap(n + 1, int(''.join(sub_num)), sub_num)
#             elif num_list[i] == num_list[j]:
#                 not_dup = False
#     if not_swap:
#         sub_num = num_list[:]
#         if not_dup:
#             sub_num[-1], sub_num[-2] = sub_num[-2], sub_num[-1]
#             swap(n + 1, int(''.join(num)), sub_num)
#         else:
#             swap(n + 1, swap_num, sub_num)


def swap(step, i, num_list):
    global max_num
    if step == swap_cnt:
        max_num = max(max_num, int(''.join(num_list)))
        return
    target = num_list[i]
    max_digit = max(num_list[i + 1:])
    if target < max_digit:
        for j in range(i + 1, len(num)):
            if num_list[j] == max_digit:
                sub_list = num_list[:]
                sub_list[i], sub_list[j] = sub_list[j], sub_list[i]
                swap(step + 1, i + 1, sub_list)
    else:
        if i == len(num_list) - 2:
            if len(num_list) == len(set(num_list)):
                if (swap_cnt - step) % 2:
                    sub_list = num_list[:]
                    sub_list[-1], sub_list[-2] = sub_list[-2], sub_list[-1]
                    swap(swap_cnt, i, sub_list)
                else:
                    swap(swap_cnt, i, num_list)
            else:
                swap(swap_cnt, i, num_list)
        else:
            swap(step, i + 1, num_list)


for tc in range(1, int(input()) + 1):
    num, swap_cnt = input().split()
    num = list(num)
    swap_cnt = int(swap_cnt)
    max_num = 0
    swap(0, 0, num[:])

    print('#%d %d' % (tc, max_num))

# for tc in range(1, int(input()) + 1):
#     num, swap_cnt = input().split()
#     num, swap_cnt = list(map(int, num)), int(swap_cnt)
#
#     prizes = []
#     for i in range(len(num) - 1):
#         for j in range(i + 1, len(num)):
#             if num[i] <= num[j]:
#                 prize = 0
#                 for k in range(len(num)):
#                     if len(num) - k == i:
#                         prize += num[j] * 10 ** k
#                     elif len(num) - k == j:
#                         prize += num[j] * 10 ** k
#                     else:
#                         prize += num[len(num) - k] * 10 ** k

# for tc in range(1, int(input()) + 1):
#     num, swap_cnt = input().split()
#     visit_num = [list(num)]
#     prizes = []
#     for swap in range(int(swap_cnt)):
#         for v in visit_num:
#             for i in range(len(v) - 1):
#                 for j in range(i + 1, len(v)):
#                     if v[i] <= v[j]:
#                         v[i]
