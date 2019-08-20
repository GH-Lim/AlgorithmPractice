def dfs_recursive(v):
    print(v)
    visited[v] = True

    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            dfs_recursive(i)


a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0 for _ in range(8)] for _ in range(8)]
for i in range(len(a) // 2):
    G[a[2 * i]][a[2 * i + 1]] = 1
    G[a[2 * i + 1]][a[2 * i]] = 1

visited = [False] * 8
dfs_recursive(1)