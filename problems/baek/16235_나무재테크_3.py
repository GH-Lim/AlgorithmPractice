import sys
sys.stdin = open('input_16235.txt', 'r')

from collections import deque
N, M, K = map(int, input().split())
A = deque([[0 for i in range(N+2)]])
nutrient_info = deque(deque(5 for _ in range(N+2)) for _ in range(N+2))
for r in range(1, N + 1):
    a = deque(map(int, input().split()))
    a.append(0)
    a.appendleft(0)
    A.append(a)
A.append([0 for i in range(N+2)])
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         nutrient_info[i][j] = 5  # 나무 양분 초기값 5

tree_info = deque(deque([] for _ in range(N+2)) for _ in range(N+2))

for m in range(M):
    x, y, z = map(int, input().split())  # 나무 위치 x, y 나이 z
    tree_info[x][y].append(z)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for k in range(K):
    # 봄
    dead_tree = []
    big_tree = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(tree_info[r][c]):  # 한바퀴 돌면 len != 0 인 영역이 늘어남
                tree_info[r][c].sort()
                i = 0
                while i < len(tree_info[r][c]):
                    if tree_info[r][c][i] <= nutrient_info[r][c]:
                        nutrient_info[r][c] -= tree_info[r][c][i]
                        tree_info[r][c][i] += 1
                        if tree_info[r][c][i] == 5:
                            big_tree.append([r, c])
                        i += 1
                    else:
                        dead_tree.append([r, c, tree_info[r][c].pop(i)])
    # 여름
    if len(dead_tree):
        for tree in dead_tree:
            nutrient_info[tree[0]][tree[1]] += tree[2] // 2
    # 가을
    if len(big_tree):
        for tree in big_tree:
            for vector in range(8):
                tree_info[tree[0] + dx[vector]][tree[1] + dy[vector]].append(1)
    # 겨울
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            nutrient_info[r][c] += A[r][c]
count = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        count += len(tree_info[r][c])

print(count)
