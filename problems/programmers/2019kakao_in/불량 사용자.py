from itertools import permutations
def check(u_id, b_id):
    for i in range(len(u_id)):
        if b_id[i] == '*':
            continue
        if u_id[i] != b_id[i]:
            return False
    return True


def solution(user_id, banned_id):
    answer = set()
    if len(user_id) == len(banned_id):
        return 1
    for combs in permutations(user_id, len(banned_id)):
        for u, b in zip(combs, banned_id):
            if len(u) == len(b) and check(u, b):
                continue
            break
        else:
            answer.add(tuple(sorted(combs)))
    return len(answer)