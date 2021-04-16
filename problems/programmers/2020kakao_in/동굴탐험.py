"""
사이클이 존재하는 지 찾기
recursion 이용 => dfs를 진행하면서 현재 해당 노드의 dfs 진행중인데 다시 진행한다면 사이클 존재
위상정렬 이용 => 남은 노드 중 진입차수가 0인 지점이 없다면 사이클 존재
"""
from collections import deque


# recursion 이용 버전
from sys import setrecursionlimit
setrecursionlimit(int(2e9))


def find_cycle(node, _list, visited):
    pass


def solution(n, path, order):
    answer = True
    L = [[] for _ in range(n)]
    sub_L = [[] for _ in range(n)]
    visited = [0] * n
    # 무방향 인접 리스트
    for a, b in path:
        L[a].append(b)
        L[b].append(a)
    q = deque([0])
    visited[0] = 1
    while q:
        cur_node = q.popleft()
        for next_node in L[cur_node]:
            if not visited[next_node]:
                sub_L[cur_node] = next_node
                visited[next_node] = 1
    for a, b in order:
        sub_L[b] = a

    return answer


solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])
