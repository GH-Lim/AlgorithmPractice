def solution(maze):
    answer = 0
    N = len(maze)

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    y, x, d = 0, 0, 0
    if maze[0][1] == 0:
        d = 1
    cnt = 0
    while True:

        if y == N - 1 and x == N - 1:
            return cnt
        y += dy[d]
        x += dx[d]

        for i in [1, 0, 3, 2]:
            ny, nx = y + dy[(d + i) % 4], x + dx[(d + i) % 4]
            if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] == 0:
                d = (d + i) % 4
                break
        cnt += 1
    return answer

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))