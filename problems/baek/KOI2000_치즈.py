import sys
sys.stdin = open('input_k2000.txt', 'r')
from pprint import pprint


# def is_air(a, b):
#     for mode in range(4):
#         if (0 <= a + dx[mode] < x) and (0 <= b + dy[mode] < y):
#             if plate[a + dx[mode]][b + dy[mode]] == 0:
#                 plate[a + dx[mode]][b + dy[mode]] = 2
#                 is_air(a + dx[mode], b + dy[mode])
#             else:
#                 pass


def is_air(a, b):
    stack = [(a, b)]
    while stack:
        yy, xx = stack.pop()
        for v in range(4):
            ny, nx = yy + dy[v], xx + dx[v]
            if 0 <= ny < y and 0 <= nx < x:
                if plate[ny][nx] == 0:
                    plate[ny][nx] = 2
                    stack.append((ny, nx))


def air_cheese():
    global count_cheese
    for i in range(1, y-1):
        for j in range(1, x-1):
            if plate[i][j] == 1:
                for mode in range(4):
                    if plate[i + dy[mode]][j + dx[mode]] == 2:
                        plate[i][j] = 3
                        count_cheese -= 1
                        break
            else:
                pass


def melt_cheese():
    for i in range(1, y-1):
        for j in range(1, x-1):
            if plate[i][j] == 3:
                plate[i][j] = 0


y, x = map(int, input().split())
count_cheese = 0
plate = [list(map(int, input().split())) for _ in range(y)]

for row in plate:
    count_cheese += sum(row)
step = 0
last_count = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
plate[0][0] = 2
while count_cheese > 0:
    step += 1
    for i in range(y):
        for j in range(x):
            if plate[i][j] == 2:
                is_air(i, j)
    last_count = count_cheese
    air_cheese()
    if count_cheese == 0:
        break
    melt_cheese()

print(step)
print(last_count)
