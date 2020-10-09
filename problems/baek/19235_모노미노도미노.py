# from collections import deque
#
# N = int(input())
#
# green = deque([0] * 4 for _ in range(6))
# blue = deque([0] * 4 for _ in range(6))
# score = 0
#
# gb = {}
# bb = {}
#
# def drop(t, x, y, k):
#     if t == 1:
#         i = 0
#         while i < 6 and not green[i][y]:
#             i += 1
#
#         green[i - 1][y] = k
#
#         j = 0
#         while j < 6 and not blue[j][x]:
#             j += 1
#         blue[j - 1][x] = k
#
#     elif t == 2:
#         i = 0
#         while i < 6 and not green[i][y] and not green[i][y + 1]:
#             i += 1
#         green[i - 1][y] = k
#         green[i - 1][y + 1] = k
#
#         j = 0
#         while j < 6 and not blue[j][x]:
#             j += 1
#         blue[j - 1][x] = k
#         blue[j - 2][x] = k
#
#     elif t == 3:
#         i = 0
#         while i < 6 and not green[i][y]:
#             i += 1
#         green[i - 1][y] = k
#         green[i - 2][y] = k
#
#         j = 0
#         while j < 6 and not blue[j][x] and not blue[j][x + 1]:
#             j += 1
#         blue[j - 1][x] = k
#         blue[j - 1][x + 1] = k
#
# def drop2(t, i, j, color, k):
#     if t == 1:
#         while i < 6 and not color[i][j]:
#             i += 1
#         color[i - 1][j] = k
#
#     elif t == 2:
#         while i < 6 and not color[i][j] and not color[i][j + 1]:
#             i += 1
#         color[i - 1][j] = k
#         color[i - 1][j + 1] = k
#
#     elif t == 3:
#         while i < 6 and not color[i][j]:
#             i += 1
#         color[i - 1][j] = k
#         color[i - 2][j] = k
#
#
# for k in range(1, N + 1):
#     t, x, y = map(int, input().split())
#     drop2(t, 0, y, green, k)
#     t2 = t
#     if t == 2:
#         t2 = 3
#     elif t == 3:
#         t2 = 2
#     drop2(t2, 0, x, blue, k)
#     a = 0
#     while green[1].count(0) < 4:
#         green.pop()
#         green.appendleft([0, 0, 0, 0])
#     while blue[1].count(0) < 4:
#         blue.pop()
#         blue.appendleft([0, 0, 0, 0])
#
#     flag = True
#     while flag:
#         flag = False
#         bot = 5
#         for i in range(2, 6):
#             if green[i].count(0) == 0:
#                 flag = True
#                 del green[i]
#                 green.appendleft([0, 0, 0, 0])
#                 score += 1
#         if flag:
#             visited = set()
#             for ii in range(bot, 2, -1):
#                 for jj in range(4):
#                     temp = green[ii][jj]
#                     if green[ii][jj] and temp not in visited:
#                         if ii + 1 < 6 and green[ii + 1][jj]:
#                             visited.add(temp)
#                             continue
#                         tt = 1
#                         xx = ii
#                         blocks = [(ii, jj)]
#                         if jj + 1 < 4 and green[ii][jj] == green[ii][jj + 1]:
#                             if ii + 1 < 6 and green[ii + 1][jj + 1]:
#                                 visited.add(temp)
#                                 continue
#                             tt = 2
#                             blocks.append((ii, jj + 1))
#                         elif green[ii][jj] == green[ii - 1][jj]:
#                             tt = 3
#                             blocks.append((ii - 1, jj))
#                         for a, b in blocks:
#                             green[a][b] = 0
#                         drop2(tt, xx, jj, green, temp)
#                         visited.add(temp)
#     flag = True
#     while flag:
#         flag = False
#         bot = 5
#         for i in range(2, 6):
#             if blue[i].count(0) == 0:
#                 flag = True
#                 del blue[i]
#                 blue.appendleft([0, 0, 0, 0])
#                 score += 1
#         if flag:
#             visited = set()
#             for ii in range(bot, 2, -1):
#                 for jj in range(4):
#                     temp = blue[ii][jj]
#                     if blue[ii][jj] and temp not in visited:
#                         if ii + 1 < 6 and blue[ii + 1][jj]:
#                             visited.add(temp)
#                             continue
#                         tt = 1
#                         xx = ii
#                         blocks = [(ii, jj)]
#                         if jj + 1 < 4 and blue[ii][jj] == blue[ii][jj + 1]:
#                             if ii + 1 < 6 and blue[ii + 1][jj + 1]:
#                                 visited.add(temp)
#                                 continue
#                             tt = 2
#                             blocks.append((ii, jj + 1))
#                         elif blue[ii][jj] == blue[ii - 1][jj]:
#                             tt = 3
#                             blocks.append((ii - 1, jj))
#                         for a, b in blocks:
#                             blue[a][b] = 0
#                         drop2(tt, xx, jj, blue, temp)
#                         visited.add(temp)
#
#         pass
#     # for i in range(2, 6):
#     #     if green[i].count(0) == 0:
#     #         del green[i]
#     #         green.appendleft([0, 0, 0, 0])
#     #         visited = set()
#     #         for ii in range(i, 2, -1):
#     #             for jj in range(4):
#     #                 temp = green[ii][jj]
#     #                 if green[ii][jj] and temp not in visited:
#     #                     if ii + 1 < 6 and green[ii + 1][jj]:
#     #                         visited.add(temp)
#     #                         continue
#     #                     tt = 1
#     #                     xx = ii
#     #                     blocks = [(ii, jj)]
#     #                     if jj + 1 < 4 and green[ii][jj] == green[ii][jj + 1]:
#     #                         if ii + 1 < 6 and green[ii + 1][jj + 1]:
#     #                             visited.add(temp)
#     #                             continue
#     #                         tt = 2
#     #                         blocks.append((ii, jj + 1))
#     #                     elif green[ii][jj] == green[ii - 1][jj]:
#     #                         tt = 3
#     #                         xx -= 1
#     #                         blocks.append((ii - 1, jj))
#     #                     for a, b in blocks:
#     #                         green[a][b] = 0
#     #                     drop2(tt, xx, jj, green, temp)
#     #                     visited.add(temp)
#     #         score += 1
#     #
#     #     if blue[i].count(0) == 0:
#     #         del blue[i]
#     #         blue.appendleft([0, 0, 0, 0])
#     #         visited = set()
#     #         for ii in range(i, 2, -1):
#     #             for jj in range(4):
#     #                 temp = blue[ii][jj]
#     #                 if blue[ii][jj] and temp not in visited:
#     #                     if ii + 1 < 6 and blue[ii + 1][jj]:
#     #                         visited.add(temp)
#     #                         continue
#     #                     tt = 1
#     #                     xx = ii
#     #                     blocks = [(ii, jj)]
#     #                     if jj + 1 < 4 and blue[ii][jj] == blue[ii][jj + 1]:
#     #                         if ii + 1 < 6 and blue[ii + 1][jj + 1]:
#     #                             visited.add(temp)
#     #                             continue
#     #                         tt = 2
#     #                         blocks.append((ii, jj + 1))
#     #                     elif blue[ii][jj] == blue[ii - 1][jj]:
#     #                         tt = 3
#     #                         xx -= 1
#     #                         blocks.append((ii - 1, jj))
#     #                     for a, b in blocks:
#     #                         blue[a][b] = 0
#     #                     drop2(tt, xx, jj, blue, temp)
#     #                     visited.add(temp)
#     #         score += 1
#     a = 0
#
# print(score)
# remain = 32
# for _ in range(2, 6):
#     remain -= green[_].count(0)
#     remain -= blue[_].count(0)
# print(remain)
from collections import deque

N = int(input())

green = deque([0] * 4 for _ in range(6))
blue = deque([0] * 4 for _ in range(6))
score = 0

def drop2(t, i, j, color, k):
    if t == 1:
        while i < 6 and not color[i][j]:
            i += 1
        color[i - 1][j] = k

    elif t == 2:
        while i < 6 and not color[i][j] and not color[i][j + 1]:
            i += 1
        color[i - 1][j] = k
        color[i - 1][j + 1] = k

    elif t == 3:
        while i < 6 and not color[i][j]:
            i += 1
        color[i - 1][j] = k
        color[i - 2][j] = k


for k in range(1, N + 1):
    t, x, y = map(int, input().split())
    drop2(t, 0, y, green, k)
    t2 = t
    if t == 2:
        t2 = 3
    elif t == 3:
        t2 = 2
    drop2(t2, 0, x, blue, k)


    flag = True
    while flag:
        flag = False
        bot = 2
        for i in range(2, 6):
            if green[i].count(0) == 0:
                flag = True
                del green[i]
                green.appendleft([0, 0, 0, 0])
                score += 1
                bot = i
        if flag:
            visited = set()
            for ii in range(bot, 2, -1):
                for jj in range(4):
                    temp = green[ii][jj]
                    if green[ii][jj] and temp not in visited:
                        if ii + 1 < 6 and green[ii + 1][jj]:
                            visited.add(temp)
                            continue
                        tt = 1
                        xx = ii
                        blocks = [(ii, jj)]
                        if jj + 1 < 4 and green[ii][jj] == green[ii][jj + 1]:
                            if ii + 1 < 6 and green[ii + 1][jj + 1]:
                                visited.add(temp)
                                continue
                            tt = 2
                            blocks.append((ii, jj + 1))
                        elif green[ii][jj] == green[ii - 1][jj]:
                            tt = 3
                            xx -= 1
                            blocks.append((ii - 1, jj))
                        for a, b in blocks:
                            green[a][b] = 0
                        drop2(tt, xx, jj, green, temp)
                        visited.add(temp)
    flag = True
    while flag:
        flag = False
        bot = 2
        for i in range(2, 6):
            if blue[i].count(0) == 0:
                flag = True
                del blue[i]
                blue.appendleft([0, 0, 0, 0])
                score += 1
                bot = i
        if flag:
            visited = set()
            for ii in range(bot, 2, -1):
                for jj in range(4):
                    temp = blue[ii][jj]
                    if blue[ii][jj] and temp not in visited:
                        if ii + 1 < 6 and blue[ii + 1][jj]:
                            visited.add(temp)
                            continue
                        tt = 1
                        xx = ii
                        blocks = [(ii, jj)]
                        if jj + 1 < 4 and blue[ii][jj] == blue[ii][jj + 1]:
                            if ii + 1 < 6 and blue[ii + 1][jj + 1]:
                                visited.add(temp)
                                continue
                            tt = 2
                            blocks.append((ii, jj + 1))
                        elif blue[ii][jj] == blue[ii - 1][jj]:
                            tt = 3
                            xx -= 1
                            blocks.append((ii - 1, jj))
                        for a, b in blocks:
                            blue[a][b] = 0
                        drop2(tt, xx, jj, blue, temp)
                        visited.add(temp)
    while green[1].count(0) < 4:
        green.pop()
        green.appendleft([0, 0, 0, 0])
    while blue[1].count(0) < 4:
        blue.pop()
        blue.appendleft([0, 0, 0, 0])
print(score)
remain = 32
for _ in range(2, 6):
    remain -= green[_].count(0)
    remain -= blue[_].count(0)
print(remain)
