def convert(n, k):
    ans = 1
    while n > 0:
        ans *= n % k
        if ans == 0:
            return 0
        n //= k
    return ans

def solution(N):
    answer = [0, 0]
    for i in range(2, 10):
        num = convert(N, i)
        if answer[1] <= num:
            answer = [i, num]
    return answer

print(solution(1000000))