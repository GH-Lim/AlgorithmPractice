def comb(k, i, g):
    global ans
    if g:
        h = [_ for _ in range(1, N + 1) if _ not in g]
        A = B = 0
        if bfs(g) and bfs(h):
            for a in g:
                A += p[a - 1]
            for b in h:
                B += p[b - 1]
            ans = min(ans, abs(A - B))
    if k == N // 2:
        return
    for j in range(i + 1, N + 1):
        gg = g[:] + [j]
        comb(k + 1, j, gg)


def bfs(k):
    visited = [0] * (N + 1)
    q = [k[0]]
    visited[k[0]] = 1
    while q:
        nn = q.pop(0)
        for l in L[nn]:
            if not visited[l] and l in k:
                q.append(l)
                visited[l] = 1
    if sum(visited) == len(k):
        return True
    else:
        return False


N = int(input())
p = list(map(int, input().split()))
len_L = [0] * (N + 1)
L = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    l = list(map(int, input().split()))
    len_L[i] = l[0]
    L[i].extend(l[1:])
ans = sum(p) + 1
comb(0, 0, [])
if ans > sum(p):
    ans = -1
print(ans)