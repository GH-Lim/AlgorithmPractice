import random

def solution(k, score):
    answer = set()
    n = len(score)
    a = [0] * n
    cnt = {}
    for i in range(1, n):
        a[i] = score[i - 1] - score[i]
        if a[i] not in cnt:
            cnt[a[i]] = 0
        cnt[a[i]] += 1
    for i in range(1, n):
        if cnt[a[i]] >= k:
            answer.add(i)
            answer.add(i - 1)
    return n - len(answer)

s = random.sample(range(2000000001), 500000)
s.sort(reverse=True)
print(solution(2, s))