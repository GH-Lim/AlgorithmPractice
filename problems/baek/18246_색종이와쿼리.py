N, M = map(int, input().split())

board = dict()
for _ in range(N):
    y1, x1, y2, x2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if (y, x) not in board:
                board[(y, x)] = 1
            else:
                board[(y, x)] += 1
for _ in range(M):
    ans = 0
    y1, x1, y2, x2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if (y, x) in board:
                ans = max(ans, board[(y, x)])
    print(ans)
