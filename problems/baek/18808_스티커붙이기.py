N, M, K = list(map(int, input().split()))

notebook = [[0] * N for _ in range(M)]
stickers = []

for _ in range(K):
    R, C = list(map(int, input().split()))
    sticker = [list(map(int, input().split())) for _ in range(R)]
    temp_sticker = {}
    for i in range(R):
        for j in range(C):
            if sticker[i][j]:
                temp_sticker[(i, j)] = 1
    stickers.append(temp_sticker)


def spin(sticker):
    temp_sticker = {}
    for i, j in sticker:
        temp_sticker[(j, i - 1 - j)]
