from collections import defaultdict

def solve(l, k):
    if not L[l][k]:
        return {k}
    sub_set = set()
    for c in L[l][k]:
        if rel[l][c]:
            sub_set.add(c)
            sub_set = sub_set.union(rel[l][c])
        else:
            sub_set.add(c)
            sub_set = sub_set.union(solve(l, c))
    rel[l][k] = sub_set
    return sub_set


for tc in range(1, int(input()) + 1):
    N, M = int(input()), int(input())
    L = [defaultdict(list), defaultdict(list)]
    for _ in range(M):
        a, b = map(int, input().split())
        L[0][a].append(b)
        L[1][b].append(a)
    rel = [defaultdict(set), defaultdict(set)]
    for i in range(1, N + 1):
        if not L[0][i]:
            solve(1, i)
        if not L[1][i]:
            solve(0, i)
    cnt = 0
    for i in range(1, N + 1):
        if len(rel[0][i]) + len(rel[1][i]) == N - 1:
            cnt += 1
    print('#%d %d' % (tc, cnt))



# from collections import defaultdict
#
# def dfs(l, k, s):
#     for n in L[l][k]:
#         rel[l][n] = rel[l][n].union(s.union({k}))
#         dfs(l, n, s.union({k}))
#
# for tc in range(1, int(input()) + 1):
#     N, M = int(input()), int(input())
#     L = [defaultdict(list), defaultdict(list)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         L[0][a].append(b)
#         L[1][b].append(a)
#
#     rel = defaultdict(set), defaultdict(set)
#     for i in range(2):
#         for j in range(1, N + 1):
#             dfs(i, j, set())
#     cnt = 0
#     for i in range(N):
#         if len(rel[0][i]) + len(rel[1][i]) == N - 1:
#             cnt += 1
#     print('#%d %d' % (tc, cnt))
