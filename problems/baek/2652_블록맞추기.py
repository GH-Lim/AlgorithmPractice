import sys
sys.stdin = open('input_2652.txt', 'r')


def cnt_clock(a, b):
    next_x = a
    next_y = b
    mode = 0
    while mode < 4:
        if visited[next_x][next_y]:
            break
        else:
            pass
        if 0 <= next_x + dx[mode] < L and 0 <= next_y + dy[mode] < L:
            if plate[next_x+dx[mode]][next_y+dy[mode]] == 0:
                if mode == 3 and next_x != a:
                    break
                elif mode == 3 and next_x == a:
                    visited[next_x][next_y] = True
                mode += 1
                point.append((next_x, next_y))
                # print(point)
            else:
                visited[next_x][next_y] = True
                if mode == 1 and a == next_x + dx[mode]:
                    break
                next_x += dx[mode]
                next_y += dy[mode]
        else:
            mode += 1
            point.append((next_x, next_y))
    point.reverse()


def clock(a, b):
    visited[a][b] = False
    point.append((a, b))
    next_x = a
    next_y = b
    mode = 0
    while mode < 4:
        if visited[next_x][next_y]:
            break
        else:
            pass
        if 0 <= next_x + cdx[mode] < L and 0 <= next_y + cdy[mode] < L:
            if plate[next_x+cdx[mode]][next_y+cdy[mode]] == 0:
                if mode == 3 and next_y != b:
                    break
                mode += 1
                point.append((next_x, next_y))
                # print(point)
            else:
                visited[next_x][next_y] = True
                next_x += cdx[mode]
                next_y += cdy[mode]
        else:
            mode += 1
            point.append((next_x, next_y))


def height(p):
    h = 1
    if p[0][0] - p[5][0]:
        next_index = [min(p[0][0], p[5][0]) + 1, p[0][1]]
    else:
        next_index = [p[0][0], min(p[0][1], p[5][1]) + 1]
    if p[1][0] - p[2][0]:
        if p[1][0] > p[2][0]:
            vector = (-1, 0)
        else:
            vector = (1, 0)
    else:
        if p[1][1] > p[2][1]:
            vector = (0, -1)
        else:
            vector = (0, 1)
    while not plate[next_index[0]+vector[0]][next_index[1]+vector[1]]:
        h += 1
        next_index[0] += vector[0]
        next_index[1] += vector[1]
    point.append(h)


def right_bot(p):
    xs = [a for a, b in p]
    ys = [b for a, b in p]
    return max(xs), max(ys)

L = int(input())
u, v, w, x, y = map(int, input().split())

plate = [list(map(int, input().split())) for _ in range(L)]
visited = [[False]*L for _ in range(L)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cdx = [0, 1, 0, -1]
cdy = [1, 0, -1, 0]
f_point = 0
target_blocks = []

results = []
cnt = 0
for i in range(L):
    for j in range(L):
        if plate[i][j] == 1 and not visited[i][j]:
            point = []
            cnt_clock(i, j)
            clock(i, j)
            rb = right_bot(point)
            for a in range(i, rb[0]+1):
                for b in range(j, rb[1]+1):
                    if not visited[a][b]:
                        visited[a][b] = True
            height(point)
            if u == max(abs(point[2][0] - point[3][0]), abs(point[2][1] - point[3][1])) + 1:
                if w == max(abs(point[0][0] - point[1][0]), abs(point[0][1] - point[1][1])) + 1:
                    if y == max(abs(point[0][0] - point[5][0]), abs(point[0][1] - point[5][1])) - 1:
                        if x == point[6]:
                            results.append([i, j])
                            cnt += 1
print(cnt)
for result in results:
    print(result[0]+1, result[1]+1)
