from collections import deque
N = int(input())

L = [[] for _ in range(N)]
one_way = []
three_way = set()
visited = set()
for _ in range(N):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    L[a].append(b)
    L[b].append(a)
ans = [0] * N
for i in range(N):
    if len(L[i]) == 2 : continue
    if len(L[i]) == 1:
        one_way.append(i)
    elif len(L[i]) > 2:
        three_way.add(i)


q = deque(one_way)
temp = set()
while q:
    for _ in range(len(q)):
        a = q.popleft()
        ans[a] += 1
        for b in L[a]:
            if b not in temp and b not in three_way:
                q.append(b)
                temp.add(b)

for node in three_way:
    cnt = 0
    q = deque([node])
    temp = set()
    while q:
        a = q.popleft()
        for b in L[a]:
            if b > 0 and b not in temp:
                q.append(b)
                ans[b] += cnt
                temp.add(b)
        cnt += 1

print(ans)
