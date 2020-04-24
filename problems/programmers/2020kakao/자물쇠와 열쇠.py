def solution(key, lock):
    M = len(key)
    N = len(lock)
    lock_hole = N * N - sum(sum(lock, []))
    key_p = []
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                key_p.append((i, j))
    for r in range(4):
        if r:
            lock = rotate(lock, N)
        for i in range(-M + 1, N):
            for j in range(-M + 1, N):
                cnt = 0
                for key_i, key_j in key_p:
                    moved_i, moved_j = key_i + i, key_j + j
                    if 0 <= moved_i < N and 0 <= moved_j < N:
                        if lock[moved_i][moved_j] == 0:
                            cnt += 1
                        else:
                            break
                else:
                    if cnt == lock_hole:
                        return True
    return False


def rotate(arr, size):
    rotated_arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated_arr[i][j] = arr[j][size - 1 - i]
    return rotated_arr