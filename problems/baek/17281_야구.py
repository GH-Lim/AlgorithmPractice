from collections import deque

N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]


visited = [0] * 9
visited[0] = 1
ans = 0


def perm(k, li):
    if k == 9:
        hit(li)
        return
    if k == 3:
        perm(k + 1, li + [0])
    else:
        for i in range(9):
            if not visited[i]:
                visited[i] = 1
                perm(k + 1, li + [i])
                visited[i] = 0


def hit(li):
    global ans
    k = 0
    score = 0
    for i in range(N):
        bases = deque([0] * 8)
        out_cnt = 0
        while out_cnt != 3:
            if hits[i][li[k]]:
                bases[0] = 1
                bases.rotate(hits[i][li[k]])
                for j in range(4):
                    if bases[4 + j]:
                        score += 1
                        bases[4 + j] = 0
            else:
                out_cnt += 1
            k = k + 1 if k != 8 else 0
    ans = max(ans, score)


perm(0, [])
print(ans)
