import sys
sys.stdin = open('2105.txt', 'r')
def find_cafe(y, x, d):
    global max_dessert
    global cnt
    global start_point
    cnt += 1
    stack.append(cafes[y][x])
    visited[y][x] = 1
    if d == 4:
        return
    if (y + dy[3], x + dx[3]) == start_point:
        max_dessert = max_dessert if max_dessert > cnt else cnt
        return
    if 0 <= y + dy[d] < N and 0 <= x + dx[d] < N:
        if not visited[y + dy[d]][x + dx[d]] and cafes[y + dy[d]][x + dx[d]] not in stack:
            find_cafe(y + dy[d], x + dx[d], d)
            stack.pop()
            cnt -= 1
            visited[y + dy[d]][x + dx[d]] = 0
    if (y, x) != start_point and 0 <= y + dy[d + 1] < N and 0 <= x + dx[d + 1] < N:
        if not visited[y + dy[d + 1]][x + dx[d + 1]] and cafes[y + dy[d + 1]][x + dx[d + 1]] not in stack:
            find_cafe(y + dy[d + 1], x + dx[d + 1], d + 1)
            stack.pop()
            cnt -= 1
            visited[y + dy[d + 1]][x + dx[d + 1]] = 0

dy = [1, 1, -1, -1, 0]
dx = [1, -1, -1, 1, 0]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    max_dessert = 0
    for i in range(N - 2):
        for j in range(1, N - 1):
            visited = [[0] * N for _ in range(N)]
            cnt = 0
            stack = []
            start_point = (i, j)
            find_cafe(i, j, 0)
    max_dessert = -1 if max_dessert == 1 or max_dessert == 0 else max_dessert
    print('#{} {}'.format(tc, max_dessert))
