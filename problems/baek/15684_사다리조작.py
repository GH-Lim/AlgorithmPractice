N, M, H = map(int, input().split())

arr = [[0] * N for _ in range(H)]  # 사다리
ans = -1

for _ in range(M):
    n, h = map(int, input().split())
    arr[n - 1][h - 1] = 1  # 연결


def dfs(cnt, y, x):  # 사다리 추가
    if ans != -1:  # ans 가 갱신이 되었다면
        return
    j = x
    for i in range(y, H):
        while j < N - 1:
            if arr[i][j]:  # 사다리 있으면
                j += 2
            else:  # 없으면
                arr[i][j] = 1
                check(cnt + 1)
                if cnt + 1 != 3:  # 사다리는 3개가 최고
                    dfs(cnt + 1, i, j + 2)
                arr[i][j] = 0
                j += 1
        j = 0


def check(cnt):  # 조건에 맞는지
    global ans
    for i in range(N):
        y, x = 0, i
        while y < H:
            if arr[y][x]:  # 1이면
                x += 1  # 오른쪽으로 이동 후 한 칸 내려감
                y += 1
            else:  # 0이면
                if x - 1 >= 0 and arr[y][x - 1]:  # 왼쪽이 1이면
                    x -= 1  # 왼쪽 이동 후 내려감
                    y += 1
                else:
                    y += 1
        if x != i:
            break
    else:
        ans = cnt


check(0)
if ans == -1:
    dfs(0, 0, 0)
print(ans)
