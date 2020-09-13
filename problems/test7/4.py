def solution(info, query):
    answer = []
    n = set(range(len(info)))
    lang = {
        'cpp': set(),
        'java': set(),
        'python': set(),
        '-': n
    }
    part = {
        'backend': set(),
        'frontend': set(),
        '-': n
    }
    car = {
        'junior': set(),
        'senior': set(),
        '-': n
    }
    food = {
        'chicken': set(),
        'pizza': set(),
        '-': n
    }
    score = []

    for idx, inf in enumerate(info):
        l, p, c, f, s = inf.split()
        lang[l].add(idx)
        part[p].add(idx)
        car[c].add(idx)
        food[f].add(idx)
        score.append(int(s))
    for q in query:
        l, p, c, f = q.split(' and ')
        f, s = f.split()
        s = int(s)
        cnt = 0
        candidate = lang[l] & part[p] & car[c] & food[f]
        for candi in candidate:
            if score[candi] >= s:
                cnt += 1
        answer.append(cnt)
    return answer