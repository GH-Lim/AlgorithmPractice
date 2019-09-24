def go(n, time):
    if n == X:
        Node_to_X[start_node] = min(Node_to_X[start_node], time)
        return
    for i in range(1, N + 1):
        if G[n][i] and not visited_go[i] and time + G[n][i] < Node_to_X[start_node]:
            visited_go[i] = 1
            go(i, time + G[n][i])
            visited_go[i] = 0

# def back(n, time):
#     if time >= X_to_Node[return_node]:
#         return
#     if n == return_node:
#         X_to_Node[return_node] = min(X_to_Node[return_node], time)
#         return
#     for i in range(1, N + 1):
#         if G[n][i] and not visited_go[i]:
#             visited_go[i] = 1
#             back(i, time + G[n][i])
#             visited_go[i] = 0
def back(n, time):
    X_to_Node[n] = min(X_to_Node[n], time)
    for i in range(1, N + 1):
        if G[n][i] and not visited_back[i]:
            visited_back[i] = 1
            back(i, time + G[n][i])
            visited_back[i] = 0

N, M, X = map(int, input().split())

G = [[0]*(N + 1) for _ in range(N + 1)]
for i in range(M):
    s, e, T = map(int, input().split())
    G[s][e] = T

Node_to_X = [100 * M] * (N + 1)
X_to_Node = [100 * M] * (N + 1)

visited_go = [0] * (N + 1)
visited_back = [0] * (N + 1)

for i in range(1, N + 1):
    if i != X:
        start_node = i
        visited_go[i] = 1
        go(i, 0)
        visited_go[i] = 0
    else:
        back(i, 0)
# for i in range(1, N + 1):
#     if i != X:
#         return_node = i
#         visited_back[i] = 1
#         back(2, 0)
#         visited_back[i] = 1

result = []
for i in range(1, N + 1):
    if i != X:
        result.append(Node_to_X[i] + X_to_Node[i])

print(max(result))
# for i in range(1, N + 1):
#     if i != X:
#         queue = [[i, 0]]
#         while queue:
#             next_node, time = queue.pop(0)
#             if next_node == X:
#                 Node_to_X[next_node] = min(Node_to_X[next_node], time)
#             for j in range(1, N + 1):
#                 if G[next_node][j]:
#                     queue.append([j, time + G[next_node][j]])
#
#
#     else:
