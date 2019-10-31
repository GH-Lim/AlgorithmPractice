# def perm(n, p, papers):
#     global ans, plate
#     cnt = 0
#     for i in range(10 - p + 1):
#         for j in range(10 - p + 1):
#             if cnt == 5: break
#             if plate[i][j]:
#                 if attach(i, j, p):
#                     cnt += 1
#                     papers += 1
#     if zeros():
#         ans = min(papers, ans)
#         return
#     if n == 5:
#         return
#
#     for i in range(1, 6):
#         if not visited[i]:
#             visited[i] = 1
#             sub_arr = [row[:] for row in plate]
#             perm(n + 1, i, papers)
#             plate = [row[:] for row in sub_arr]
#             visited[i] = 0
def perm(i, j, a1, a2, a3, a4, a5):
    global ans
    if not count:
        ans = min(ans, a1 + a2 + a3 + a4 + a5)
        return
    while i < 10:
        while j < 10:
            if plate[i][j] and a1 + a2 + a3 + a4 + a5 + 1 < ans:
                if a5 != 5 and attach(i, j, 5):
                    perm(i, j+5, a1, a2, a3, a4, a5 + 1)
                    detach(i, j, 5)
                if a4 != 5 and attach(i, j, 4):
                    perm(i, j+4, a1, a2, a3, a4 + 1, a5)
                    detach(i, j, 4)
                if a3 != 5 and attach(i, j, 3):
                    perm(i, j+3, a1, a2, a3 + 1, a4, a5)
                    detach(i, j, 3)
                if a2 != 5 and attach(i, j, 2):
                    perm(i, j+2, a1, a2 + 1, a3, a4, a5)
                    detach(i, j, 2)
                if a1 != 5 and attach(i, j, 1):
                    perm(i, j+1, a1 + 1, a2, a3, a4, a5)
                    detach(i, j, 1)
        j = 0
        i += 1


def attach(y, x, p):
    global count
    if y + p > 10 or x + p > 10:
        return False
    for i in range(y, y + p):
        for j in range(x, x + p):
            if not plate[i][j]:
                return False
    for i in range(y, y + p):
        plate[i][x: x + p] = [0] * p
    count -= p * p
    return True


def detach(y, x, p):
    global count
    for i in range(y, y + p):
        plate[i][x: x + p] = [1] * p
    count += p * p


plate = [list(map(int, input().split())) for _ in range(10)]
count = sum(sum(plate, []))
ans = 26
visited = [0] * 6
perm(0, 0, 0, 0, 0, 0, 0)
# perm(0, 11, 0)
# for p in range(5, 0, -1):
#     cnt = 0
#     for i in range(10 - p + 1):
#         for j in range(10 - p + 1):
#             if plate[i][j]:
#                 if cnt == 5:
#                     if p == 1:
#                         papers = -1
#                     break
#                 if attach(i, j, p):
#                     cnt += 1
#                     papers += 1
#             else:
#                 if p == 1 and cnt == 5:
#                     break
#                 continue
#         else:
#             if p == 1 and cnt == 5:
#                 break
#             continue
#     else:
#         if p == 1 and cnt == 5:
#             break
# if ans == 26:
#     ans = -1
print(ans)