from collections import deque
wheels = [deque(map(int, input())) for _ in range(4)]

for k in range(int(input())):
    num, r = map(int, input().split())
    num -= 1
    L = [[] for _ in range(4)]
    for i in range(3):
        if wheels[i][2] != wheels[i + 1][6]:
            L[i].append(i + 1)
            L[i + 1].append(i)
    select = [0] * 4
    q = deque([num])
    while q:
        r = -r
        for _ in range(len(q)):
            n = q.popleft()
            select[n] = -r
            for m in L[n]:
                if not select[m]:
                    q.append(m)

    for i in range(4):
        if select[i]:
            wheels[i].rotate(select[i])

ans = 0
for i in range(4):
    if wheels[i][0]:
        ans += 2 ** i

print(ans)
