def solution(N, stages):
    current_stage = {}
    failed = {}
    for s in range(1, N + 2):
        current_stage[s] = 0
        failed[s] = 0
    for s in stages:
        for i in range(1, s + 1):
            current_stage[i] += 1
        failed[s] += 1

    failed_rate = {}
    for s in range(1, N + 1):
        if current_stage[s]:
            failed_rate[s] = failed[s] / current_stage[s]
        else:
            failed_rate[s] = 0

    answer = list(k for k, v in sorted(failed_rate.items(), key=lambda x: x[1], reverse=True))
    return answer