from collections import defaultdict

def solution(info, query):
    answer = []
    resume = defaultdict(list)
    for spec in info:
        lang, job, car, food, score = spec.split()
        score = int(score)
        for l in [lang, '-']:
            for j in [job, '-']:
                for c in [car, '-']:
                    for f in [food, '-']:
                        resume[(l, j, c, f)].append(score)
                        resume[(l, j, c, f)].sort(reverse=True)
    for q in query:
        lang, job, car, foodscore = q.split(' and ')
        food, score = foodscore.split()
        score = int(score)
        key = (lang, job, car, food)
        left = 0
        right = len(resume[key]) - 1
        mid = 0
        while left < right:
            mid = (left + right) // 2
            if resume[key][mid] <= score:
                left = mid + 1
            else:
                right = mid - 1
        while mid < len(resume[key]) and resume[key][mid] >= score:
            mid += 1
        answer.append(mid)
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))