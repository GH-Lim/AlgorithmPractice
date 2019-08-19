def dfs_recursive(G, v):
    visited[v-1] = True


a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
arr = [[0 for _ in range(7)] for _ in range(7)]
for i in range(len(a) // 2):
    arr[a[2 * i]-1][a[2 * i + 1]-1] = 1
    arr[a[2 * i + 1]-1][a[2 * i]-1] = 1

visited = [False] * 7