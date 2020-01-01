inf = 2e10
for tc in range(1, int(input()) + 1):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n + 2)]
    G = [[inf] * (n + 2) for _ in range(n + 2)]
    for s in range(n + 2):
        for e in range(n + 2):
