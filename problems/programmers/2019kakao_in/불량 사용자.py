def check(u_id, b_id):
    for i in range(len(u_id)):
        if b_id[i] == '*':
            continue
        if u_id[i] != b_id[i]:
            return False
    return True


def solution(user_id, banned_id):
    if len(user_id) == len(banned_id):
        return 1
    answer = {}
    for b in banned_id:
        for u in user_id:
            if check(u, b):

    return answer