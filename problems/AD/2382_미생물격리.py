import sys
from pprint import pprint
sys.stdin = open('2382.txt', 'r')

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    stack = []
    cells = [list(map(int, input().split())) for _ in range(K)]
    for i in range(M):
        for cell in cells:
            x, y, n, d = cell
            x += dx[d]
            y += dy[d]
            if x == 0 or x == N - 1 or y == 0 or y == N - 1:
                n //= 2
                d = 1 if d == 2 else 2 if d == 1 else 3 if d == 4 else 4
            else:
                if (x, y) not in stack:
                    stack.append((x, y))
                else:

    print()
