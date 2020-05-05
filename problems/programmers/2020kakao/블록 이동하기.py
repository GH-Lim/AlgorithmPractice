def solution(board):
    answer = 0
    return answer


def move(y1, x1, y2, x2, visited):
    for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ny1, nx1, ny2, nx2 = y1 + dy, x1 + dx, y2 + dy, x2 + dx
        if (ny1, nx1, ny2, nx2) not in visited:
            if
