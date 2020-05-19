N, M, K = list(map(int, input().split()))

notebook = [[0] * M for _ in range(N)]
stickers = []

for _ in range(K):
    R, C = list(map(int, input().split()))
    sticker = [list(map(int, input().split())) for _ in range(R)]
    temp_sticker = [R, C, []]
    for i in range(R):
        for j in range(C):
            if sticker[i][j]:
                temp_sticker[2].append((i, j))
    stickers.append(temp_sticker)



def spin(sticker):
    R, C, sticker = sticker
    temp_sticker = []
    for i, j in sticker:
        temp_sticker.append((C - j - 1, i))
    return C, R, temp_sticker


for sticker in stickers:
    for _ in range(4):
        r, c, ss = sticker
        # if N - r + 1 <= 0 or M - c + 1 <= 0:
        #     sticker = spin(sticker)
        #     continue
        for di in range(N - r + 1):
            for dj in range(M - c + 1):
                for s in ss:
                    i, j = s
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and notebook[ni][nj]:
                        break
                else:
                    for s in ss:
                        i, j = s
                        ni, nj = i + di, j + dj
                        notebook[ni][nj] = 1
                    break
            else:
                continue
            break
        else:
            if _ != 3:
                sticker = spin(sticker)
            continue
        break
print(sum(sum(notebook, [])))
