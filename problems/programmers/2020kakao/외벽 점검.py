from collections import deque
from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) + 1
    weak = deque(weak)
    dist_perms = list(permutations(dist))
    for _ in range(len(weak)):
        for d_perm in dist_perms:
            start_i = 0
            for i in range(len(d_perm)):
                for j in range(start_i + 1, len(weak)):
                    if weak[start_i] + d_perm[i] >= weak[-1]:
                        answer = min(answer, i + 1)
                        break
                    if weak[start_i] + d_perm[i] < weak[j]:
                        start_i = j
                        break
        weak.rotate(-1)
        weak[-1] += n
    return answer if answer != len(dist) + 1 else -1

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))