import sys
sys.stdin = open('5644.txt', 'r')

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, +1, 0]
T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    move1 = list(map(int, input().split())) + [0]
    move2 = list(map(int, input().split())) + [0]
    arr = [[0] * 10 for _ in range(10)]
    for bc in range(A):
        x, y, c, p = map(int, input().split())
        x -= 1
        y -= 1
        for i in range(-c, 1):
            for j in range(-i - c, i + c + 1):
                if 0 <= x + j < 10 and 0 <= y + i < 10:
                    if arr[y + i][x + j] == 0:
                        arr[y + i][x + j] = [[p, bc]]
                    else:
                        arr[y + i][x + j].append([p, bc])
        for i in range(1, c + 1):
            for j in range(i - c, -i + c + 1):
                if 0 <= x + j < 10 and 0 <= y + i < 10:
                    if arr[y + i][x + j] == 0:
                        arr[y + i][x + j] = [[p, bc]]
                    else:
                        arr[y + i][x + j].append([p, bc])
    y1, x1 = 0, 0
    y2, x2 = 9, 9
    charge = 0
    for t in range(M + 1):
        if arr[y1][x1] != 0:
            user1 = arr[y1][x1]
            user1.sort(reverse=True)
        else: user1 = []
        if arr[y2][x2] != 0:
            user2 = arr[y2][x2]
            user2.sort(reverse=True)
        else: user2 = []

        if not user1 and not user2:
            pass
        elif not user1 and user2:
            charge += user2[0][0]
        elif user1 and not user2:
            charge += user1[0][0]
        else:
            same_bc = False
            for u1 in user1:
                if u1 in user2:
                    same_bc = True
                    break
            if same_bc:
                if len(user1) == 1 and len(user2) == 1:
                    charge += user1[0][0]
                elif len(user1) == 1:
                    temp = user1[0][0]
                    if user2[0][0] == temp:
                        charge += temp
                        charge += user2[1][0]
                    else:
                        charge += temp
                        charge += user2[0][0]
                elif len(user2) == 1:
                    temp = user2[0][0]
                    if user1[0][0] == temp:
                        charge += temp
                        charge += user1[1][0]
                    else:
                        charge += temp
                        charge += user1[0][0]
                else:
                    temp = user1[0][0]
                    if user2[0][0] == temp:
                        charge += temp
                        charge += user2[1][0] if user2[1][0] > user1[1][0] else user1[1][0]
                    else:
                        charge += user1[0][0]
                        charge += user2[0][0]
            else:
                charge += user1[0][0]
                charge += user2[0][0]
        y1 += dy[move1[t]]
        x1 += dx[move1[t]]
        y2 += dy[move2[t]]
        x2 += dx[move2[t]]
    print('#{} {}'.format(tc, charge))
