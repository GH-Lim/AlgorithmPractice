from itertools import permutations
N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]


hitter = {3: 0}
visited = [0] * 9
ans = 0


def perm(k):
    if k == 9:
        hit(hitter)
        return
    if k == 3:
        perm(k + 1)
    else:
        for i in range(1, 9):
            if not visited[i]:
                visited[i] = 1
                hitter[k] = i
                perm(k + 1)
                visited[i] = 0


def hit(li):
    global ans
    k = 0
    score = 0
    for hit_order in hits:
        one, two, three = 0, 0, 0
        out_cnt = 0
        while out_cnt != 3:
            if hit_order[li[k]] == 1:
                score += three
                one, two, three = 1, one, two
            elif hit_order[li[k]] == 2:
                score += three + two
                one, two, three = 0, 1, one
            elif hit_order[li[k]] == 3:
                score += three + two + one
                one, two, three = 0, 0, 1
            elif hit_order[li[k]] == 4:
                score += three + two + one + 1
                one, two, three = 0, 0, 0
            else:
                out_cnt += 1
            k = (k + 1) % 9
    ans = max(ans, score)


perm(0)
perms = permutations(range(1, 9), 8)

for perm in perms:
    p = list(perm[:3]) + [0] + list(perm[3:])
    k = 0
    score = 0
    for hit_order in hits:
        one, two, three = 0, 0, 0
        out_cnt = 0
        while out_cnt != 3:
            if hit_order[p[k]] == 1:
                score += three
                one, two, three = 1, one, two
            elif hit_order[p[k]] == 2:
                score += three + two
                one, two, three = 0, 1, one
            elif hit_order[p[k]] == 3:
                score += three + two + one
                one, two, three = 0, 0, 1
            elif hit_order[p[k]] == 4:
                score += three + two + one + 1
                one, two, three = 0, 0, 0
            else:
                out_cnt += 1
            k = (k + 1) % 9
    ans = max(ans, score)
    # print(time.time() - st)
print(ans)
