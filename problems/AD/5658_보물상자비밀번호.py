import sys
sys.stdin = open('5658.txt', 'r')

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = deque(input())

    size = N // 4
    results = []
    for r in range(size):
        nums.rotate(1)
        for i in range(4):
            num = ''
            for j in range(i * size, (i + 1) * size):
                num += nums[j]
            if num not in results:
                results.append(num)
    results.sort(reverse=True)
    print('#{} {}'.format(tc, int(results[K - 1], 16)))
