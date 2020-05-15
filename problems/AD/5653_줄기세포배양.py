# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# for tc in range(1, int(input()) + 1):
#     N, M, K = map(int, input().split())
#     plate = [list(map(int, input().split())) for _ in range(N)]
#     cells = {}
#     for i in range(N):
#         for j in range(M):
#             if plate[i][j]:
#                 cells[(i, j)] = [0, plate[i][j], 0]  # state, X, cnt
#     dead_cnt = 0
#     for i in range(K):
#         # 활성화 번식 카운트
#         sub_cells = {}
#         for cell, info in cells.items():
#             y, x = cell
#             if info[0] == 1:
#                 info[2] += 1
#                 if info[1] == info[2]:
#                     info[0] += 1
#                     dead_cnt += 1
#                 for d in range(4):
#                     ny, nx = y + dy[d], x + dx[d]
#                     if (ny, nx) not in cells and (ny, nx) not in sub_cells:
#                         sub_cells[(ny, nx)] = [0, info[1], 0]
#                     elif (ny, nx) not in cells and (ny, nx) in sub_cells:
#                         if sub_cells[(ny, nx)][1] < info[1]:
#                             sub_cells[(ny, nx)][1] = info[1]
#             # 비활 카운트
#             if info[0] == 0:
#                 info[2] += 1
#                 if info[1] == info[2]:
#                     info[2] = 0
#                     info[0] += 1
#         cells.update(sub_cells)
#     print('#%d %d' % (tc, len(cells) - dead_cnt))


# T = int(input())
# for tc in range(1):
#     n, m, k = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     # 좌표 = 생명력, 흐른시간, 상태
#     cells = dict()
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j]:
#                 cells[(i, j)] = [arr[i][j], 0, 1]
#
#     dead_cell = dict()
#     for _ in range(k):
#
#         temp_list = []
#         for (x, y), (life, time, state) in cells.items():
#             cells[(x, y)][1] += 1
#             if cells[(x, y)][1] == life:
#                 # 상태를 바꿔주고
#                 cells[(x, y)][2] += 1
#                 # 시간을 초기화 시켜준다
#                 cells[(x, y)][1] = 0
#             if cells[(x, y)][2] == 3:
#                 dead_cell[(x, y)] = 1
#                 temp_list.append((x, y))
#             # print(cells)
#
#
#         for (x, y) in temp_list:
#             del cells[(x, y)]
#         # print(len(cells), cells)
#         now_list = dict()
#         # 첫 한시간 동안
#         for (x, y), (life, time, state) in cells.items():
#             if state == 2 and time == 0:
#                 for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
#                     xx = x + dx
#                     yy = y + dy
#                     if dead_cell.get((xx, yy)) == None and cells.get((xx, yy)) == None:
#                         if now_list.get((xx, yy)):
#                             now_list[(xx, yy)][0] = max(now_list[(xx, yy)][0], life)
#                         else:
#                             now_list[(xx, yy)] = [life, 0, 1]
#         # print(now_list)
#         cells.update(now_list)
#         print(_ + 1, '시간')
#         print(cells)
#         print(dead_cell)
#         print()
#     print(len(cells))