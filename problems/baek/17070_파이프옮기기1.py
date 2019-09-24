import sys
sys.stdin = open('17070.txt', 'r')

# def push(y, x, state):
#     global count
#     if y == N - 1 and x == N - 1:
#         count += 1
#         return
#     for mode in range(len(dx[state])):
#         next_y, next_x = y + dy[state][mode], x + dx[state][mode]
#         if next_y < N and next_x < N and not room[next_x][next_y]:
#             if state == 0:
#                 if mode == 0:
#                     push(next_y, next_x, 0)
#                 elif mode == 1 and not room[y + 1][x]:
#                     push(next_y, next_x, 2)
#             elif state == 1:
#                 if mode == 1:
#                     push(next_y, next_x, 1)
#                 elif mode == 0 and not room[y][x + 1]:
#                     push(next_y, next_x, 2)
#             else:
#                 if mode == 0 or mode == 1:
#                     push(next_y, next_x, mode)
#                 elif mode == 2 and not room[y + 1][x] and not room[y][x + 1]:
#                     push(next_y, next_x, 2)


# def push(y, x, state):
#     global count
#     queue = [(y, x, state)]
#
#     while queue:
#         y, x, state = queue.pop(0)
#         if (y, x) == (N - 1, N - 1):
#             count += 1
#         for mode in range(len(dx[state])):
#             next_y, next_x = y + dy[state][mode], x + dx[state][mode]
#             if next_y < N and next_x < N and not room[next_x][next_y]:
#                 if state == 0:
#                     if mode == 0:
#                         queue.append((next_y, next_x, 0))
#                     elif mode == 1 and not room[y + 1][x]:
#                         queue.append((next_y, next_x, 2))
#                 elif state == 1:
#                     if mode == 1:
#                         queue.append((next_y, next_x, 1))
#                     elif mode == 0 and not room[y][x + 1]:
#                         queue.append((next_y, next_x, 2))
#                 else:
#                     if mode == 0 or mode == 1:
#                         queue.append((next_y, next_x, mode))
#                     elif mode == 2 and not room[y + 1][x] and not room[y][x + 1]:
#                         queue.append((next_y, next_x, 2))

def push(y, x, state):
    global count
    if y == N - 1 and x == N - 1:
        count += 1
        return
    if state == 0:
        if x + 1 < N and not room[y][x + 1]:
            push(y, x + 1, 0)
        if x + 1 < N and y + 1 < N and not room[y + 1][x + 1] and not room[y + 1][x] and not room[y][x + 1]:
            push(y + 1, x + 1, 2)
    elif state == 1:
        if y + 1 < N and not room[y + 1][x]:
            push(y + 1, x, 1)
        if x + 1 < N and y + 1 < N and not room[y + 1][x + 1] and not room[y + 1][x] and not room[y][x + 1]:
            push(y + 1, x + 1, 2)
    else:
        if x + 1 < N and not room[y][x + 1]:
            push(y, x + 1, 0)
        if y + 1 < N and not room[y + 1][x]:
            push(y + 1, x, 1)
        if x + 1 < N and y + 1 < N and not room[y + 1][x + 1] and not room[y + 1][x] and not room[y][x + 1]:
            push(y + 1, x + 1, 2)


N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
# dx = [[1, 1], [1, 0], [1, 0, 1]]
# dy = [[0, 1], [1, 1], [0, 1, 1]]
count = 0
if not room[N - 1][N - 1]:
    push(0, 1, 0)
print(count)
