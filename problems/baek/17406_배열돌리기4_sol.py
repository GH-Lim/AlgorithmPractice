import sys
sys.stdin = open('input_17406.txt', 'r')


def rotate(r, c, s):
    for i in range(1, s + 1):
        temp = data[r - i][c - i]
        for j in range(r - i, r + i):
            data[j][c - i] = data[j + 1][c - i]
        for j in range(c - i, c + i):
            data[r + i][j] = data[r + i][j + 1]
        for j in range(r + i, r - i, -1):
            data[j][c + i] = data[j - 1][c + i]
        for j in range(c + i, c - i, -1):
            data[r - i][j] = data[r - i][j - 1]
        data[r - i][c - i + 1] = temp


def reverse_rotate(r, c, s):
    for i in range(1, s + 1):
        temp = data[r - i][c - i]
        for j in range(c - i, c + i):
            data[r - i][j] = data[r - i][j + 1]
        for j in range(r - i, r + i):
            data[j][c + i] = data[j + 1][c + i]
        for j in range(c + i, c - i, -1):
            data[r + i][j] = data[r + i][j - 1]
        for j in range(r + i, r - i, -1):
            data[j][c - i] = data[j - 1][c - i]
        data[r - i + 1][c - i] = temp


def check():
    global ans
    for i in data:
        temp = sum(i)
        if ans > temp:
            ans = temp


def sol(cnt):
    if cnt == K:
        check()
        return
    for i in range(K):
        if visit[i]:
            rotate(rcs[i][0], rcs[i][1], rcs[i][2])
            visit[i] = False
            sol(cnt + 1)
            visit[i] = True
            reverse_rotate(rcs[i][0], rcs[i][1], rcs[i][2])


N, M, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]
visit = [True] * K
for _ in range(K):
    rcs[_][0] -= 1
    rcs[_][1] -= 1
ans = 2 << 30
sol(0)
print(ans)