from collections import deque
from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) + 1
    weak = deque(weak)
    dist_perms = permutations(dist)
    for _ in range(len(dist)):
        for d_perm in dist_perms:
            i = 0
            for d in d_perm:
                while


        weak.rotate(-1)
        weak[-1] += n
    return answer

solution(4, [1, 2], [1, 2])