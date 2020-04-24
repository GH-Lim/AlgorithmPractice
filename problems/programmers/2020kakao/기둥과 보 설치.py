# # a : 0 (기둥), 1 (보), 2 (기둥 + 보)
# # b : 0 (삭제), 1 (설치)
# def solution(n, build_frame):
#     n += 1
#     answer = []
#     wall = list([2] * n for _ in range(n))
#
#     for x, y, a, b in build_frame:
#         if b:  # 설치
#             if check(x, y, a, wall):
#                 wall[y][x] = a
#         else:  # 삭제
#             temp = wall[y][x]
#             wall[y][x] = 2  # 일단 지워보고
#             for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]:
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < n and 0 <= nx < n:
#                     if wall[ny][nx] == 0 or wall[ny][nx] == 1:
#                         if not check(nx, ny, wall[ny][nx], wall):
#                             wall[y][x] = temp
#                             break
#
#
#     for y in range(n):
#         for x in range(n):
#             if wall[y][x] != 2:
#                 answer.append([x, y, wall[y][x]])
#     answer.sort()
#     print(answer)
#     return answer
#
#
# def check(x, y, a, wall):
#     if a:  # 보
#         if y == 0: return False
#         if wall[y - 1][x] == 0 or wall[y - 1][x + 1] == 0:  # 한 쪽 끝 부분이 기둥 위에 있거나
#             return True
#         elif wall[y][x - 1] == 1 and wall[y][x + 1] == 1:  # 양쪽 끝 부분이 다른 보와 동시에 연결
#             return True
#         else:
#             return False
#     else:  # 기둥
#         if y == 0: return True  # 바닥 위에 있거나
#         if wall[y][x] == 1 or wall[y][x - 1] == 1:  # 보의 한쪽 끝 부분 위에 있거나
#             return True
#         if wall[y - 1][x] == 0:  # 다른 기둥 위에
#             return True
#         else:
#             return False

# a : 0 (기둥), 1 (보)
# b : 0 (삭제), 1 (설치)
def solution(n, build_frame):
    n += 1
    answer = []
    wall = {}
    for x, y, a, b in build_frame:
        if b:  # 설치
            if check(x, y, a, wall):
                wall[(x, y, a)] = 1
        else:  # 삭제
            wall.pop((x, y, a))
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (0, 0)]:
                ny, nx = y + dy, x + dx
                if (nx, ny, 0) in wall:
                    if not check(nx, ny, 0, wall):
                        wall[(x, y, a)] = 1
                        break
                if (nx, ny, 1) in wall:
                    if not check(nx, ny, 1, wall):
                        wall[(x, y, a)] = 1
                        break

    answer = list(map(list, wall.keys()))
    answer.sort()
    print(answer)
    return answer


def check(x, y, a, wall):
    if a:  # 보
        if y == 0: return False
        if (x, y - 1, 0) in wall or (x + 1, y - 1, 0) in wall:  # 한 쪽 끝 부분이 기둥 위에 있거나
            return True
        elif (x - 1, y, 1) in wall and (x + 1, y, 1) in wall:  # 양쪽 끝 부분이 다른 보와 동시에 연결
            return True
        else:
            return False
    else:  # 기둥
        if y == 0: return True  # 바닥 위에 있거나
        if (x, y, 1) in wall or (x - 1, y, 1) in wall:  # 보의 한쪽 끝 부분 위에 있거나
            return True
        if (x, y - 1, 0) in wall:  # 다른 기둥 위에
            return True
        else:
            return False

n = 5
b = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(n, b)

# # a : 0 (기둥), 1 (보)
# # b : 0 (삭제), 1 (설치)
# def solution(n, build_frame):
#     n += 1
#     answer = []
#     wall = set()
#     for x, y, a, b in build_frame:
#         if b:  # 설치
#             if check(x, y, a, wall):
#                 wall.add((x, y, a))
#         else:  # 삭제
#             wall.remove((x, y, a))
#             for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (0, 0)]:
#                 ny, nx = y + dy, x + dx
#                 if (nx, ny, 0) in wall:
#                     if not check(nx, ny, 0, wall):
#                         wall.add((x, y, a))
#                         break
#                 if (nx, ny, 1) in wall:
#                     if not check(nx, ny, 1, wall):
#                         wall.add((x, y, a))
#                         break
#
#     answer = list(map(list, wall))
#     answer.sort()
#     return answer
#
#
# def check(x, y, a, wall):
#     if a:  # 보
#         if y == 0: return False
#         if (x, y - 1, 0) in wall or (x + 1, y - 1, 0) in wall:  # 한 쪽 끝 부분이 기둥 위에 있거나
#             return True
#         elif (x - 1, y, 1) in wall and (x + 1, y, 1) in wall:  # 양쪽 끝 부분이 다른 보와 동시에 연결
#             return True
#         else:
#             return False
#     else:  # 기둥
#         if y == 0: return True  # 바닥 위에 있거나
#         if (x, y, 1) in wall or (x - 1, y, 1) in wall:  # 보의 한쪽 끝 부분 위에 있거나
#             return True
#         if (x, y - 1, 0) in wall:  # 다른 기둥 위에
#             return True
#         else:
#             return False

# # a : 0 (기둥), 1 (보), 2 (기둥 + 보)
# # b : 0 (삭제), 1 (설치)
# def solution(n, build_frame):
#     n += 1
#     answer = []
#     wall = list([3] * n for _ in range(n))
#
#     for x, y, a, b in build_frame:
#         if b:  # 설치
#             if check(x, y, a, wall):
#                 if wall[y][x] == 0 or wall[y][x] == 1:
#                     wall[y][x] = 2
#                 else: wall[y][x] = a
#         else:  # 삭제
#             temp = wall[y][x] # 일단 지워보고
#             if temp == 2:
#                 if a == 1: wall[y][x] = 0
#                 else: wall[y][x] = 1
#             else:
#                 wall[y][x] = 3
#             for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]:
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < n and 0 <= nx < n:
#                     if wall[ny][nx] == 0 or wall[ny][nx] == 1:
#                         if not check(nx, ny, wall[ny][nx], wall):
#                             wall[y][x] = temp
#                             break
#                     elif wall[ny][nx] == 2:
#                         if not check(nx, ny, 0, wall) and not check(nx, ny, 1, wall):
#                             wall[y][x] = temp
#                             break
#
#     for y in range(n):
#         for x in range(n):
#             if wall[y][x] == 1 or wall[y][x] == 0:
#                 answer.append([x, y, wall[y][x]])
#             elif wall[y][x] == 2:
#                 answer.append([x, y, 0])
#                 answer.append([x, y, 1])
#     answer.sort()
#     return answer
#
#
# def check(x, y, a, wall):
#     if a:  # 보
#         if y == 0: return False
#         if wall[y - 1][x] == 0 or wall[y - 1][x + 1] == 0 \
#             or wall[y - 1][x] == 2 or wall[y - 1][x + 1] == 2:  # 한 쪽 끝 부분이 기둥 위에 있거나
#             return True
#         if (wall[y][x - 1] == 1 or wall[y][x - 1] == 2)\
#             and (wall[y][x + 1] == 1 or wall[y][x - 1] == 2):  # 양쪽 끝 부분이 다른 보와 동시에 연결
#             return True
#         return False
#     else:  # 기둥
#         if y == 0: return True  # 바닥 위에 있거나
#         if wall[y][x] == 1 or wall[y][x - 1] == 1 \
#             or wall[y][x] == 2 or wall[y][x - 1] == 2:  # 보의 한쪽 끝 부분 위에 있거나
#             return True
#         if wall[y - 1][x] == 0 or wall[y - 1][x] == 2:  # 다른 기둥 위에
#             return True
#         return False