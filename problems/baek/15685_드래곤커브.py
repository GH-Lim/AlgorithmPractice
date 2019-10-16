N = int(input())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

points = {}
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_g = [d]
    for _ in range(g):
        sub_dragon = []
        for i in range(len(dragon_g) - 1, -1, -1):
            d = (dragon_g[i] + 1) % 4
            sub_dragon.append(d)
        dragon_g.extend(sub_dragon)
    points[(y, x)] = 1
    for d in dragon_g:
        y += dy[d]
        x += dx[d]
        points[(y, x)] = 1

ans = 0
for point in points:
    y, x = point
    if (y + 1, x) in points and (y + 1, x + 1) in points and (y, x + 1) in points:
        ans += 1

print(ans)
