import sys
from pprint import pprint
sys.stdin = open('input_17406.txt', 'r')


def rotate(target, r, s, c):
    r -= 1
    c -= 1
    for shell in range(s):
        left_top_x, left_top_y = r - s + shell, c - s + shell
        next_x, next_y = left_top_x, left_top_y
        mode = 0
        for i in range((2 * (s - shell) + 1) ** 2 - (2 * (s - shell) - 1) ** 2):
            if next_x + dx[mode] > r + s - shell or next_y + dy[mode] > c + s - shell \
                    or next_x + dx[mode] < r - s + shell or next_y + dy[mode] < c - s + shell:
                mode += 1
            next_x += dx[mode]
            next_y += dy[mode]
            target[left_top_x][left_top_y], target[next_x][next_y] = target[next_x][next_y], target[left_top_x][left_top_y]


def permute(nums):
    length = len(nums)
    if length == 1:
        return [nums]
    else:
        result = []
        for i in nums:
            b = [num for num in nums]
            b.remove(i)
            b.sort()
            for j in permute(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
    return result


N, M, K = map(int, input().split())

arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
r = [0 for _ in range(K)]
c = [0 for _ in range(K)]
s = [0 for _ in range(K)]
for k in range(K):
    r[k], c[k], s[k] = map(int, input().split())
min_row = sum(arr[0])
cases = list(range(K))
all_cases = permute(cases)

for case in all_cases:
    sub_arr = [row.copy() for row in arr]
    for k in case:
        rotate(sub_arr, r[k], s[k], c[k])
    for row in sub_arr:
        if sum(row) < min_row:
            min_row = sum(row)

print(min_row)
