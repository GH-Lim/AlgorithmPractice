def dfs(y, x, cnt, one):
    global ans
    if cnt >= ans:
        return
    if not one:
        ans = cnt
        return
    if y == 10:
        return
    if plate[y][x] and not visited[y][x]:
        for k in range(5, 0, -1):
            if paper[k - 1]:
                if check(y, x, k):
                    paper[k - 1] -= 1
                    attach(y, x, k)
                    if x + 1 < 10:
                        dfs(y, x + 1, cnt + 1, one - (k * k))
                    else:
                        dfs(y + 1, 0, cnt + 1, one - (k * k))
                    detach(y, x, k)
                    paper[k - 1] += 1
    else:
        if x + 1 < 10:
            dfs(y, x + 1, cnt, one)
        else:
            dfs(y + 1, 0, cnt, one)

    pass

def check(y, x, k):
    if y + k > 10 or x + k > 10:
        return False
    for i in range(y, y + k):
        for j in range(x, x + k):
            if not plate[i][j] or visited[i][j]:
                return False
    return True


def attach(y, x, k):
    for i in range(y, y + k):
        for j in range(x, x + k):
            visited[i][j] = 1


def detach(y, x, k):
    for i in range(y, y + k):
        for j in range(x, x + k):
            visited[i][j] = 0


plate = [list(map(int, input().split())) for _ in range(10)]
one_cnt = sum(sum(plate, []))
count = sum(sum(plate, []))
ans = 26
visited = [[0] * 10 for _ in range(10)]
paper = [5] * 5

if not one_cnt:
    ans = 0

else:
    dfs(0, 0, 0, one_cnt)
if ans == 26:
    ans = -1
print(ans)
