import sys
from pprint import pprint
sys.stdin = open('5648.txt', 'r')

# dx = [0, 0, -0.5, 0.5]
# dy = [0.5, -0.5, 0, 0]
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     atoms = [list(map(int, input().split())) for _ in range(N)]
#     energy = 0
#     while len(atoms) > 1:
#         k = 0
#         while k < len(atoms):
#             atoms[k][0] += dx[atoms[k][2]]
#             atoms[k][1] += dy[atoms[k][2]]
#             if abs(atoms[k][0]) > 1000 or abs(atoms[k][1]) > 1000:
#                 atoms.pop(k)
#             else:
#                 k += 1
#         i = 0
#         while i < len(atoms) - 1:
#             crash = False
#             j = i + 1
#             while j < len(atoms):
#                 if (atoms[i][0], atoms[i][1]) == (atoms[j][0], atoms[j][1]):
#                     energy += atoms[j][3]
#                     atoms.pop(j)
#                     crash = True
#                 else:
#                     j += 1
#             if crash:
#                 energy += atoms[i][3]
#                 atoms.pop(i)
#             else:
#                 i += 1
#     print('#{} {}'.format(tc, energy))


# # 틀린답
# T = int(input())
# # for tc in range(1, T + 1):
# #     N = int(input())
# #     atoms = [list(map(int, input().split())) for _ in range(N)]
# #     x_p = []
# #     y_p = []
# #     for atom in atoms:
# #         atom[0] *= 2
# #         if atom[0] not in x_p:
# #             x_p.append(atom[0])
# #         atom[1] *= 2
# #         if atom[1] not in y_p:
# #             y_p.append(atom[1])
# #     energy = 0
# #     for x in x_p:
# #         for y in y_p:
# #             approach = []
# #             for atom in atoms:
# #                 if x == atom[0]:
# #                     if y < atom[1] and atom[2] == 1:
# #                         approach.append([atom[1] - y, atom])
# #                     elif y > atom[1] and atom[2] == 0:
# #                         approach.append([y - atom[1], atom])
# #                 elif y == atom[1]:
# #                     if x < atom[0] and atom[2] == 2:
# #                         approach.append([atom[0] - x, atom])
# #                     elif y > atom[0] and atom[2] == 3:
# #                         approach.append([x - atom[0], atom])
# #             if len(approach) > 1:
# #                 visited = [0] * len(approach)
# #                 for i in range(len(approach) - 1):
# #                     if not visited[i]:
# #                         collision = False
# #                         for j in range(i, len(approach)):
# #                             if approach[i][0] == approach[j][0]:
# #                                 energy += approach[j][1][3]
# #                                 approach[j][1][3] = 0
# #                                 visited[j] = 1
# #                                 collision = True
# #                         if collision:
# #                             energy += approach[i][1][3]
# #                             approach[i][1][3] = 0
# #     print('#{} {}'.format(tc, energy))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    energy = 0
    candidates = [[0, 0, 0]]
    for i in range(N - 1):
        for j in range(i, N):
            dx = atoms[i][0] - atoms[j][0]
            dy = atoms[i][1] - atoms[j][1]
            v1 = atoms[i][2]
            v2 = atoms[j][2]
            if dy == 0:
                if v1 == 2 and v2 == 3 and dx > 0:
                    candidates.append([dx / 2, i, j])
                elif v1 == 3 and v2 == 2 and dx < 0:
                    candidates.append([-dx / 2, i, j])
            elif dx == 0:
                if v1 == 0 and v2 == 1 and dy < 0:
                    candidates.append([-dy / 2, i, j])
                elif v1 == 1 and v2 == 0 and dy > 0:
                    candidates.append([dy / 2, i, j])
            elif dx == dy:
                if dx < 0 and v1 == 3 and v2 == 1:
                    candidates.append([-dx, i, j])
                elif dx < 0 and v1 == 0 and v2 == 2:
                    candidates.append([-dx, i, j])
                elif dx > 0 and v1 == 1 and v2 == 3:
                    candidates.append([dx, i, j])
                elif dx > 0 and v1 == 2 and v2 == 0:
                    candidates.append([dx, i, j])
            elif dx == -dy:
                if dx < 0 and v1 == 3 and v2 == 0:
                    candidates.append([-dx, i, j])
                elif dx < 0 and v1 == 1 and v2 == 2:
                    candidates.append([-dx, i, j])
                elif dx > 0 and v1 == 0 and v2 == 3:
                    candidates.append([dx, i, j])
                elif dx > 0 and v1 == 2 and v2 == 1:
                    candidates.append([dx, i, j])
    visited = [0] * N
    candidates.sort()
    collision = []
    for i in range(len(candidates) - 1):
        if candidates[i][0] != candidates[i+1][0]:
            while collision:
                temp = collision.pop()
                if not visited[temp]:
                    visited[temp] = 1
                    energy += atoms[temp][3]

            if not visited[candidates[i + 1][1]] and not visited[candidates[i + 1][2]]:
                collision.append(candidates[i + 1][1])
                collision.append(candidates[i + 1][2])
        else:
            if not visited[candidates[i + 1][1]] and not visited[candidates[i + 1][2]]:
                collision.append(candidates[i + 1][1])
                collision.append(candidates[i + 1][2])
    while collision:
        temp = collision.pop()
        if not visited[temp]:
            visited[temp] = 1
            energy += atoms[temp][3]
    print('#{} {}'.format(tc, energy))
