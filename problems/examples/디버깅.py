<<<<<<< HEAD
<<<<<<< HEAD
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

walls = set()
cameras = []
detected = set()
blank = 0
directions = {
    1: [(1,), (2,), (3,), (0,)],
    2: [(0, 2), (1, 3)],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    5: [(0, 1, 2, 3)],
}
for i in range(N):
    for j in range(M):
        if office[i][j] == 0: blank += 1
        elif office[i][j] == 6:
            walls.add((i, j))
        else:
            cameras.append((i, j, office[i][j]))
C = len(cameras)


def go(i, j, ds, detect):
    for d in ds:
        y, x = i, j
        while 0 <= y < N and 0 <= x < M and office[y][x] != 6:
            if office[y][x] == 0:
                detect.add((y, x))
            y += dy[d]
            x += dx[d]
    return detect


def solve(k, detect_set):
    global ans
    if k == C or ans == blank:
        ans = max(ans, len(detect_set))
        return
    y, x, n = cameras[k]
    for direction in directions[n]:
        temp = detect_set.copy()
        solve(k + 1, go(y, x, direction, temp))


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0

solve(0, set())

print(blank - ans)
=======
a= {1, 2}
b = {2}
print(a.isdisjoint(b))
print(a)
>>>>>>> 8df44518d12af07f5f1029184e937029b12f688c
=======
a= {1, 2}
b = {2}
print(a.isdisjoint(b))
print(a)
>>>>>>> 8df44518d12af07f5f1029184e937029b12f688c
