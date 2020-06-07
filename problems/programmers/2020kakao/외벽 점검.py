from collections import deque
from itertools import permutations

def perms(k, n, weak, dist, pick):
    global answer
    if not pick:
        for i in range(len(weak)):
            start_idx = i
            for p in pick:
                check_dist = weak[start_idx] + p
                for _ in range(len(weak)):
                    if check_dist < weak[start_idx]:
                        pass

    if k == n:
        print(pick)
        return 0
    for i in range(len(dist)):
        if dist[i] not in pick:
            perms(k + 1, n, weak, dist, pick+[dist[i]])

def solution(n, weak, dist):
    global answer
    answer = len(dist) + 1
    weak = deque(weak)
    dist.sort(reverse=True)

    perms(0, len(dist), weak, dist, [])
    return answer

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))