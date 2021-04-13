from sys import stdin

input = stdin.readline
N, M, K = map(int, input().split())
fireball = {}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball[(r - 1, c - 1)] = [[m, s, d]]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    moved_fireball = {}
    for key, val in fireball.items():
        y, x = key
        while val:
            m, s, d = val.pop()
            ny, nx = (y + dy[d] * s) % N, (x + dx[d] * s) % N
            if (ny, nx) not in moved_fireball:
                moved_fireball[(ny, nx)] = []
            moved_fireball[(ny, nx)].append([m, s, d])
    for key, val in moved_fireball.items():
        y, x = key
        size = len(val)
        if size > 1:
            sum_m = 0
            sum_s = 0
            next_d = [[0, 2, 4, 6], [1, 3, 5, 7]]
            nd = 0
            flag = -1
            while val:
                m, s, d = val.pop()
                if flag < 0:
                    flag = d % 2
                sum_m += m
                sum_s += s
                if flag != d % 2: nd = 1
            sum_m //= 5
            if sum_m:
                sum_s //= size
                for d in next_d[nd]:
                    if (y, x) not in fireball:
                        fireball[(y, x)] = []
                    fireball[(y, x)].append([sum_m, sum_s, d])
        else:
            fireball[(y, x)] = val
ans = 0
for val in fireball.values():
    for m, s, d in val:
        ans += m
print(ans)
