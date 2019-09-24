import sys
sys.stdin = open('input_16235.txt', 'r')

N, M, K = map(int, input().split())
A = [[0] * (N + 2)]
nutrient_info = [[0] * (N + 2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        nutrient_info[i][j] = 5  # 나무 양분 초기값 5

tree_info = [[[] for _ in range(N+2)] for _ in range(N+2)]
for r in range(1, N + 1):
    A.append([0] + list(map(int, input().split())) + [0])
A.append([0] * (N + 2))
for m in range(M):
    x, y, z = map(int, input().split())  # 나무 위치 x, y 나이 z
    tree_info[x][y].append(z)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for k in range(K):
    # 봄
    dead_tree = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(tree_info[r][c]):  # 한바퀴 돌면 len != 0 인 영역이 늘어남
                tree_info[r][c].sort()
                i = 0
                while i < len(tree_info[r][c]):
                    if tree_info[r][c][i] <= nutrient_info[r][c]:
                        nutrient_info[r][c] -= tree_info[r][c][i]
                        tree_info[r][c][i] += 1
                        i += 1
                    else:
                        dead_tree.append([r, c, tree_info[r][c].pop(i)])
    # 여름
    if len(dead_tree):
        for tree in dead_tree:
            nutrient_info[tree[0]][tree[1]] += tree[2] // 2
    # 가을
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(tree_info[r][c]):
                for tree in tree_info[r][c]:
                    if tree % 5 == 0:
                        for vector in range(8):
                            tree_info[r + dx[vector]][c + dy[vector]].append(1)
            # 겨울
            nutrient_info[r][c] += A[r][c]
count = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        count += len(tree_info[r][c])

print(count)