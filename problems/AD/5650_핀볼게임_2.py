import sys
sys.stdin = open('5650.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
block = {
    1: [4, 0, 3, 4],
    2: [4, 4, 1, 0],
    3: [1, 4, 4, 2],
    4: [3, 2, 4, 4],
    5: [4, 4, 4, 4]
}
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    WH = {  # 웜홀
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:  # board 의 번호가 6~10 이면 해당 웜홀에 좌표 추가
                WH[board[i][j]].append((i, j))
    max_score = 0
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if board[i][j] == 0:
                    score = 0
                    x = i
                    y = j
                    while True:
                        x += dx[d]
                        y += dy[d]
                        if x == i and y == j:
                            break
                        if 0 <= x < N and 0 <= y < N:
                            state = board[x][y]
                            if state == -1:
                                break
                            elif state == 0:
                                continue
                            elif 0 < state < 6:
                                if block[state][d] == 4:
                                    score *= 2
                                    score += 1
                                    break
                                else:
                                    d = block[state][d]
                                    score += 1
                            else:
                                for wh in WH[state]:
                                    if wh != (x, y):
                                        x = wh[0]
                                        y = wh[1]
                                        break
                        else:
                            score *= 2
                            score += 1  # 벽에 부딪히면 이동 경로를 그대로 되돌아옴
                            break
                    if max_score < score:
                        max_score = score  # 점수 최신화
    print('#{} {}'.format(tc, max_score))


#
# def move(d, x, y):
#     global score
#     start_x = x
#     start_y = y
#     while True:
#         x += dx[d]
#         y += dy[d]
#         if x == start_x and y == start_y:
#             return
#         if 0 <= x < N and 0 <= y < N:
#             state = board[x][y]
#             if state == -1:
#                 return
#             elif state == 0:
#                 continue
#             elif 0 < state < 6:
#                 d = block[state][d]
#                 score += 1
#             else:
#                 for wh in WH[state]:
#                     if wh != (x, y):
#                         x, y = wh
#                         break
#         else:
#             d = block[5][d]
#             score += 1
#
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# block = {
#     1: [2, 0, 3, 1],
#     2: [2, 3, 1, 0],
#     3: [1, 3, 0, 2],
#     4: [3, 2, 0, 1],
#     5: [2, 3, 0, 1]
# }
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     WH = {
#         6: [],
#         7: [],
#         8: [],
#         9: [],
#         10: []
#     }
#     for i in range(N):
#         for j in range(N):
#             if 6 <= board[i][j] <= 10:
#                 WH[board[i][j]].append((i, j))
#     max_score = 0
#     for d in range(4):
#         for i in range(N):
#             for j in range(N):
#                 if board[i][j] == 0:
#                     score = 0
#                     move(d, i, j)
#                     if max_score < score:
#                         max_score = score
#     print('#{} {}'.format(tc, max_score))
