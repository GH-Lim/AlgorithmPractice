user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]


def solution(user_id, banned_id):
    cases = []
    case = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        candidate = banned_id[i]
        for user in user_id:
            if len(candidate) != len(user): pass
            else:
                for j in range(len(candidate)):
                    if candidate[j] == '*': pass
                    else:
                        if candidate[j] != user[j]:
                            break
                else:
                    case[i].append(user)
    def dfs(k, u):
        if k == len(case):
            if u in cases: pass
            elif len(u) != len(banned_id): pass
            else: cases.append(u)
            return
        for i in range(len(case[k])):
            if case[k][i] in u: continue
            sub_u = u.copy()
            sub_u.add(case[k][i])
            dfs(k + 1, sub_u)
    dfs(0, set())
    answer = len(cases)
    return answer


print(solution(user_id, banned_id))
