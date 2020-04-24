def solution(key, lock):
    M = len(key)
    N = len(lock)
    key_p = []
    lock_hole = {}
    for i in range(N):
        for j in range(N):
            if i < M and j < M and key[i][j]:
                key_p.append((i, j))
            if not lock[i][j]:
                lock_hole[(i, j)] = 1

    for r in range(4):
        if r:
            lock_hole = rotate(lock_hole, N)
        for i in range(-M + 1, N):
            for j in range(-M + 1, N):
                cnt = 0
                for key_i, key_j in key_p:
                    moved_i, moved_j = key_i + i, key_j + j
                    if 0 <= moved_i < N and 0 <= moved_j < N:
                        if (moved_i, moved_j) in lock_hole:
                            cnt += 1
                        else:
                            break
                else:
                    if cnt == len(lock_hole):
                        return True
    return False


def rotate(lock_arr, n):
    rotated_lock = {}
    for i, j in lock_arr.keys():
        rotated_lock[(j, n - 1 - i)] = 1
    return rotated_lock


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))

# def solution(key, lock):
#     N = len(key)
#     lock_hole = N * N - sum(sum(lock, []))
#     key_p = []
#     for i in range(N):
#         for j in range(N):
#             if key[i][j]:
#                 key_p.append((i, j))
#     for r in range(4):
#         if r:
#             lock = rotate(lock, N)
#         for i in range(-N + 1, N):
#             for j in range(-N + 1, N):
#                 cnt = 0
#                 for key_i, key_j in key_p:
#                     moved_i, moved_j = key_i + i, key_j + j
#                     if 0 <= moved_i < N and 0 <= moved_j < N:
#                         if lock[moved_i][moved_j] == 0:
#                             cnt += 1
#                         else:
#                             break
#                 else:
#                     if cnt == lock_hole:
#                         return True
#     return False
#
#
# def rotate(arr, N):
#     rotated_arr = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             rotated_arr[i][j] = arr[j][N - 1 - i]
#     return rotated_arr
