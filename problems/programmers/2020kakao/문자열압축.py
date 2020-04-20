def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        temp = 0
        for j in range(len(s) // i - 1):
            if s[i*j:i*(j+1)] == s[i*(j+1):i*(j+2)]:
                cnt += 1
            else:
                if cnt == 1:
                    temp += i
                else:
                    temp += i + len(str(cnt))
                    cnt = 1
        if cnt == 1:
            temp += i + len(s) % i
        else:
            temp += i + len(str(cnt)) + len(s) % i
        answer = min(answer, temp)
    return answer
