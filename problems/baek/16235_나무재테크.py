import sys
sys.stdin = open('input_16235.txt', 'r')

N, M, K = map(int, input().split())
A = [[0 for i in range(N+2)] for j in range(N+2)]
nutrient_info = [[0 for i in range(N+2)] for j in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        nutrient_info[i][j] = 5  # 나무 양분 초기값 5

tree_info = [[[] for i in range(N+2)] for j in range(N+2)]
for r in range(1, N + 1):
    A[r] = [0] + list(map(int, input().split())) + [0]

for m in range(M):
    x, y, z = map(int, input().split())  # 나무 위치 x, y 나이 z
    tree_info[x][y].append(z)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for k in range(K):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            # 봄
            if len(tree_info[r][c]):
                tree_info[r][c].sort()
                i = 0
                while i < len(tree_info[r][c]):
                    if tree_info[r][c][i] <= nutrient_info[r][c]:
                        nutrient_info[r][c] -= tree_info[r][c][i]
                        tree_info[r][c][i] += 1
                        i += 1
                    else:
                        # 여름
                        nutrient_info[r][c] += int(tree_info[r][c][i] / 2)
                        # tree_info[r][c] = tree_info[r][c][:i]
                        tree_info[r][c].pop(i)
            # 가을
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