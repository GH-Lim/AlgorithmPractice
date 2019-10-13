N, M, X = map(int, input().split())

inf = 1e9
G = [[] for _ in range(N)]
rev_G = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, input().split())
    G[s - 1].append([d, e - 1])
    rev_G[e - 1].append([d, s - 1])

dij_list = [[inf, inf] for i in range(N)]


def dijkstra(arr, rev):
    dij_list[X - 1][rev] = 0
    q = [(0, X - 1)]
    while q:
        val, node = q.pop()
        if val > dij_list[node][rev]:
            continue
        for v, i in arr[node]:
            if dij_list[i][rev] > val + v:
                dij_list[i][rev] = val + v
                q.append([val + v, i])
        q.sort(reverse=True)


dijkstra(G, False)
dijkstra(rev_G, True)

result = [sum(dij_list[i]) for i in range(N)]
print(max(result))
