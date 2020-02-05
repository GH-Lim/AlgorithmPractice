N, M = int(input()), int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

p = {}
rank = {}
def make_set(v):
    p[v] = v
    rank[v] = 0

def find_set(v):
    if p[v] != v:
        p[v] = find_set(p[v])
    return p[v]

def union(v, u):
    root1 = find_set(v)
    root2 = find_set(u)
    if rank[root1] > rank[root2]:
        p[root2] = root1
    else:
        p[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


for n in range(1, N + 1):
    make_set(n)

for i in range(1, N + 1):
    for j in range(1,  N + 1):
        if arr[i - 1][j - 1]:
            if find_set(i) != find_set(j):
                union(i, j)

root = p[plan[0]]
answer = 'YES'
for i in range(1, M):
    if p[plan[i]] != root:
        answer = 'NO'
        break
print(answer)
