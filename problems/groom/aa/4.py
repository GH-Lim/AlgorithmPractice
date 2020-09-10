from collections import deque
N, d = map(int, input().strip().split())
b = [list(map(int, input().strip().split())) for _ in range(N)]

print(sum(sum(b, [])))

1, 5, 13, 25
  4  8  12  16