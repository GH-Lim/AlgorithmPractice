import sys
sys.stdin = open('input_k2000.txt', 'r')
from pprint import pprint


def is_air():
    for i in range(1, x-1):
        for j in range(1, y-1):
            if plate[i][j] == 0:
                if plate[i - 1][j] == 2:
                    plate[i][j] = 2
                    continue
                if plate[i][j - 1] == 2:
                    plate[i][j] = 2
                    continue
                if plate[i + 1][j] == 2:
                    plate[i][j] = 2
                    continue
                if plate[i][j + 1] == 2:
                    plate[i][j] = 2
                    continue
            else:
                pass
    for i in range(x-2, 0, -1):
        for j in range(y-2, 0, -1):
            if plate[i][j] == 0:
                if plate[i - 1][j] == 2:
                    plate[i][j] = 2
                    continue
                if plate[i][j - 1] == 2:
                    plate[i][j] = 2
                    continue
                if plate[i + 1][j] == 2:
                    plate[i][j] = 2
                    continue
                if plate[i][j + 1] == 2:
                    plate[i][j] = 2
                    continue
            else:
                pass

    # for i in range(1, y-1):
    #     for j in range(1, x-1):
    #         if plate[j][i] == 0:
    #             if plate[j][i - 1] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #             if plate[j - 1][i] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #             if plate[j][i + 1] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #             if plate[j + 1][i] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #         else:
    #             pass
    #
    # for i in range(y-2, 0, -1):
    #     for j in range(x-2, 0, -1):
    #         if plate[j][i] == 0:
    #             if plate[j][i - 1] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #             if plate[j - 1][i] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #             if plate[j][i + 1] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #             if plate[j + 1][i] == 2:
    #                 plate[j][i] = 2
    #                 continue
    #         else:
    #             pass


def air_cheese():
    global count_cheese
    for i in range(1, x-1):
        for j in range(1, y-1):
            if plate[i][j] == 1:
                if plate[i - 1][j] == 2:
                    plate[i][j] = 3
                    count_cheese -= 1
                    continue
                if plate[i][j - 1] == 2:
                    plate[i][j] = 3
                    count_cheese -= 1
                    continue
                if plate[i + 1][j] == 2:
                    plate[i][j] = 3
                    count_cheese -= 1
                    continue
                if plate[i][j + 1] == 2:
                    plate[i][j] = 3
                    count_cheese -= 1
                    continue
            else:
                pass


def melt_cheese():
    for i in range(1, x-1):
        for j in range(1, y-1):
            if plate[i][j] == 3:
                plate[i][j] = 0


x, y = map(int, input().split())
count_cheese = 0
plate = [list(map(int, input().split())) for _ in range(x)]
for row in plate:
    count_cheese += sum(row)
for i in range(x):
    plate[i][0] = 2
    plate[i][y-1] = 2
for j in range(y):
    plate[0][j] = 2
    plate[x-1][j] = 2

step = 0
last_count = 0
while count_cheese > 0:
    is_air()
    step += 1
    last_count = count_cheese
    air_cheese()
    if count_cheese == 0:
        break
    melt_cheese()

print(step)
print(last_count)
