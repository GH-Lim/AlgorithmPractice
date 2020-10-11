dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [1, 0, -1, -1, -1, 0, 1, 1]

fish = {}
area = {}
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    fish[a1] = (i, 0, b1)
    fish[a2] = (i, 1, b2)
    fish[a3] = (i, 2, b3)
    fish[a4] = (i, 3, b4)

    area[(i, 0)] = a1
    area[(i, 1)] = a2
    area[(i, 2)] = a3
    area[(i, 3)] = a4

fish[0] = fish.pop(area[(0, 0)])
ans = area[(0, 0)]
area[(0, 0)] = 0

def move(f, a):
    for i in range(1, 17):
        if i not in f:
            continue
        y, x, d = f[i]
        for k in range(8):
            nd = (d + k) % 8
            ny, nx = y + dy[nd], x + dx[nd]
            if (ny, nx) not in a or a[(ny, nx)] == 0:
                continue
            temp = (ny, nx)
            if a[temp] == -1:
                f[i] = (ny, nx, nd)
                a[(y, x)], a[temp] = a[temp], a[(y, x)]
            else:
                _, _, td = f[a[temp]]
                f[i], f[a[temp]] = (ny, nx, nd), (y, x, td)
                a[(y, x)], a[temp] = a[temp], a[(y, x)]
            break


def hunt(eat, f, a):
    global ans
    ans = max(ans, eat)
    move(f, a)

    y, x, d = f[0]
    for i in range(1, 4):
        ny, nx = y + i * dy[d], x + i * dx[d]
        if (ny, nx) not in a:
            break
        if a[(ny, nx)] == -1:
            continue
        tf, ta = f.copy(), a.copy()
        n_eat = ta[(ny, nx)]
        tf[0] = tf.pop(ta[(ny, nx)])
        ta[(y, x)], ta[(ny, nx)] = -1, 0
        hunt(eat + n_eat, tf, ta)


hunt(ans, fish, area)
print(ans)