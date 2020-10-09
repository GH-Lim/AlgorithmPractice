from collections import deque


def bfs(s, e, Li):
    ans = 0
    q = deque([s])
    while q:
        a = q.popleft()
        if a == e:
            ans += 1
            continue
        for b in Li[a]:
            q.append(b)
    return ans


def solution(depar, hub, dest, roads):

    L = {}
    rev_L = {}
    for a, b in roads:
        if a not in L:
            L[a] = []
        if a not in rev_L:
            rev_L[a] = []
        L[a].append(b)
        if b not in rev_L:
            rev_L[b] = []
        if b not in L:
            L[b] = []
        rev_L[b].append(a)

    # idx = 0
    # cities = {}
    # for a, b in roads:
    #     if a not in cities:
    #         cities[a] = idx
    #         idx += 1
    #     if b not in cities:
    #         cities[b] = idx
    #         idx += 1
    # L = [[] for _ in range(len(cities))]
    # rev_L = [[] for _ in range(len(cities))]
    #
    # for a, b in roads:
    #     L[cities[a]].append(cities[b])
    #     rev_L[cities[b]].append(cities[a])
    #
    # depar = cities[depar]
    # hub = cities[hub]
    # dest = cities[dest]

    dep_to_hub = bfs(hub, depar, rev_L)
    if dep_to_hub == 0:
        return 0
    hub_to_des = bfs(hub, dest, L)

    return dep_to_hub * hub_to_des

print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"], ["SEOUL", "ULSAN"], ["DAEJEON", "DAEGU"], ["GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"], ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"], ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"]]))
print(solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL", "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "ULSAN"], ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]))