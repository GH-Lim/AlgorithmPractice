import sys
from collections import deque

sys.stdin = open('input_미로.txt', 'r')


# sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = deque(deque(i for i in map(int, input().split())) for _ in range(N))
    stack = [(1000, 1000)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    f = 0
    flag = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 3:
                stack.append((x, y))
                flag = 1
                break
        if flag:
            break
    x, y = stack[1]
    # print(stack)
    while stack != []:
        i = 0
        while i < 4:
            y2 = y + dy[i]
            x2 = x + dx[i]
            if 0 > y2 or y2 >= len(arr) or 0 > x2 or x2 >= len(arr[0]):
                pass
            elif arr[y + dy[i]][x + dx[i]] == 2:
                print(1)
                f = 1
                break
            elif arr[y + dy[i]][x + dx[i]] == 0:
                arr[y + dy[i]][x + dx[i]] = 1
                stack.append((x + dx[i], y + dy[i]))
                x += dx[i]
                y += dy[i]
                i = -1
            i += 1
        x, y = stack.pop()
        # print(y, x)
        if f:
            break
    if f == 0:
        print(0)
