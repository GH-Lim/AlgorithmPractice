from collections import deque

for tc in range(1, int(input()) + 1):
    K = int(input())
    wheels = [deque(map(int, input().split())) for _ in range(4)]

    for k in range(K):
        num, r = map(int, input().split())
        num -= 1
        visited = [0] * 4
        select = [0] * 4
        q = deque([(num, r)])
        while q:
            nw, nr = q.popleft()
            visited[nw] = 1
            select[nw] = nr
            if nw > 0 and not visited[nw - 1] and wheels[nw - 1][2] != wheels[nw][6]:
                q.append((nw - 1, -nr))
            if nw < 3 and not visited[nw + 1] and wheels[nw][2] != wheels[nw + 1][6]:
                q.append((nw + 1, -nr))
        for i in range(4):
            if select[i]:
                wheels[i].rotate(select[i])
    ans = 0
    for i in range(4):
        ans += wheels[i][0] * (2 ** i)
    print('#%d %d' % (tc, ans))
