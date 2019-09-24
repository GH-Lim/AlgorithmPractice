import sys
sys.stdin = open('14888.txt', 'r')


# def perm(n, num):
#     global min_result, max_result
#
#     if n == N - 1:
#         min_result = min(min_result, num)
#         max_result = max(max_result, num)
#         return
#
#     if operators[0]:
#         operators[0] -= 1
#         perm(n + 1, num + nums[n + 1])
#         operators[0] += 1
#
#     if operators[1]:
#         operators[1] -= 1
#         perm(n + 1, num - nums[n + 1])
#         operators[1] += 1
#
#     if operators[2]:
#         operators[2] -= 1
#         perm(n + 1, num * nums[n + 1])
#         operators[2] += 1
#
#     if operators[3]:
#         operators[3] -= 1
#         perm(n + 1, num // nums[n + 1] if num >= 0 else -(-num // nums[n + 1]))
#         operators[3] += 1
def perm(n, num, o1, o2, o3, o4):
    global min_result, max_result

    if n == N - 1:
        min_result = min(min_result, num)
        max_result = max(max_result, num)
        return

    if o1:
        perm(n + 1, num + nums[n + 1], o1 - 1, o2, o3, o4)

    if o2:
        perm(n + 1, num - nums[n + 1], o1, o2 - 1, o3, o4)

    if o3:
        perm(n + 1, num * nums[n + 1], o1, o2, o3 - 1, o4)

    if o4:
        perm(n + 1, num // nums[n + 1] if num >= 0 else -(-num // nums[n + 1]), o1, o2, o3, o4 - 1)


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, //
min_result = 1000000000
max_result = -1000000000
perm(0, nums[0], *operators)

print(max_result)
print(min_result)
