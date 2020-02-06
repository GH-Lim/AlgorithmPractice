def find_island(y, x):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        i_map[y][x] = numbering
        for mode in range(4):
            next_y, next_x = y + dy[mode], x + dx[mode]
            if 0 <= next_y < N and 0 <= next_x < M:
                if i_map[next_y][next_x] == 1:
                    stack.append((next_y, next_x))


def bridge(y, x, n):
    for mode in range(4):
        next_y, next_x = y + dy[mode], x + dx[mode]
        cnt = 0
        while 0 <= next_y < N and 0 <= next_x < M:
            if i_map[next_y][next_x] == n:
                break
            if i_map[next_y][next_x]:
                if cnt > 1:
                    G[n - 2][i_map[next_y][next_x] - 2] = min(cnt, G[n - 2][i_map[next_y][next_x] - 2])
                break
            cnt += 1
            next_y += dy[mode]
            next_x += dx[mode]


# def dfs(i, length, cnt):
#     global ans
#     if cnt == numbering - 3:
#         ans = min(ans, length)
#         return
#     for j in range(numbering - 2):
#         if not visited[j] and G[i][j] != 10:
#             visited[j] = 1
#             dfs(j, length + G[i][j], cnt + 1)
#             visited[j] = 0


N, M = map(int, input().split())
i_map = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
numbering = 2
for i in range(N):
    for j in range(M):
        if i_map[i][j] == 1:
            find_island(i, j)
            numbering += 1
G = [[10]*(numbering - 2) for _ in range(numbering - 2)]

for i in range(N):
    for j in range(M):
        if i_map[i][j]:
            bridge(i, j, i_map[i][j])
visited = [0] * (numbering - 2)
ans = 50
nodes = [[10, i] for i in range(numbering - 2)]
# for i in range(numbering - 2):
#     visited[i] = 1
#     dfs(i, 0, 0)
#     visited[i] = 0
# for n in range(numbering - 3):
#     for i in range(n, numbering - 2):
#         if visited[n] == 10 and G[n][i] != 10:
#             visited[n] = 0
#         visited[i] = min(visited[i], G[n][i])
nodes[0][0] = 0
q = [nodes[0]]
while q:
    val, node = q.pop(0)
    visited[node] = 1
    for i in range(1, numbering - 2):
        if G[node][i] != 10:
            if not visited[i]:
                if nodes[i][0] > G[node][i]:
                    nodes[i][0] = G[node][i]
                q.append(nodes[i])
    q.sort() # heapq or priority queue 사용과 같은 효과. 시간이 조금 더 걸릴 듯
ans = 0
for i in range(1, numbering - 2):
    if nodes[i][0] == 10:
        ans = -1
        break
    ans += nodes[i][0]
print(ans)
