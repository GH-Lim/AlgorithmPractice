N, M, K = list(map(int, input().split()))

notebook = [[0] * N for _ in range(M)]
stickers = []

for _ in range(K):
    R, C = list(map(int, input().split()))
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)

def spin(stick):
    for i in range(len(stick)):
        for j in range(len(stick[0])):
            pass
