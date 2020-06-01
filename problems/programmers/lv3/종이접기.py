def solution(n):
    answer = []
    for _ in range(n):
        answer = answer + [0] + [int(not(i)) for i in answer[::-1]]
    return answer
