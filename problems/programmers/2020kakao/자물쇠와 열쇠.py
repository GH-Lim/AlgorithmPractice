def solution(key, lock):
    N = len(key)
    hole = N * N - sum(sum(lock, []))
    for r in range(4):
        if r:
            key = rotate(key, N)
        for i in range(N):
            for j in range(N):


    return False


def rotate(key, N):
    rotated_key = [[0] * N for _ in range(N)]
    for i in range(len(key)):
        for j in range(len(key)):
            rotated_key[i][j] = key[j][N - 1 - i]
    return rotated_key


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key, lock)
