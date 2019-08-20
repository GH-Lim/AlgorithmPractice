def dfs(v):
    global top
    result = []
    top += 1
    stack[top] = v
    while top >= 0:
        v = stack[top]
        stack[top] = 0
        top -= 1
        if not visited[v-1]:
            visited[v-1] = True
            for i in range(7, 0, -1):
                if arr[v][i] and not visited[i]:
                    top += 1
                    stack[top] = i
            result.append(v)
    print(result)


a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# node = [1, 2, 3, 4, 5, 6, 7]
arr = [[0 for _ in range(8)] for _ in range(8)]
for i in range(len(a) // 2):
    arr[a[2 * i]][a[2 * i + 1]] = 1
    arr[a[2 * i + 1]][a[2 * i]] = 1
stack = [0] * 7
top = -1
visited = [False] * 8
# visited[0] = True

dfs(1)
