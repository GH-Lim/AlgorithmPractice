import sys
sys.stdin = open('input_k2000.txt', 'r')
from pprint import pprint


def is_air(a, b):
    for mode in range(4):
        if (0 <= a + dx[mode] < x) and (0 <= b + dy[mode] < y):
            if plate[a + dx[mode]][b + dy[mode]] == 0:
                plate[a + dx[mode]][b + dy[mode]] = 2
                is_air(a + dx[mode], b + dy[mode])
            else:
                pass


def air_cheese():
    global count_cheese
    for i in range(1, x-1):
        for j in range(1, y-1):
            if plate[i][j] == 1:
                for mode in range(4):
                    if plate[i + dx[mode]][j + dy[mode]] == 2:
                        plate[i][j] = 3
                        count_cheese -= 1
                        break
            else:
                pass


def melt_cheese():
    for i in range(1, x-1):
        for j in range(1, y-1):
            if plate[i][j] == 3:
                plate[i][j] = 0


x, y = map(int, sys.stdin.readline().split())
count_cheese = 0
plate = [list(map(int, sys.stdin.readline().split())) for _ in range(x)]

for row in plate:
    count_cheese += sum(row)
step = 0
last_count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
plate[0][0] = 2
while count_cheese > 0:
    step += 1
    for i in range(x):
        for j in range(y):
            if plate[i][j] == 2:
                is_air(i, j)
    last_count = count_cheese
    air_cheese()
    if count_cheese == 0:
        break
    melt_cheese()

print(step)
print(last_count)
