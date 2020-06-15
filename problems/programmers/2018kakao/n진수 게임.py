def solution(n, t, m, p):
    answer = ''
    number = 0
    i = 0
    while True:
        num = trans_n(n, number)
        for digit in num:
            if i == p - 1:
                answer += digit
                if len(answer) == t:
                    return answer
            i = (i + 1) % m
        number += 1

def trans_n(n, num):
    N = "0123456789ABCDEF"
    encoded = ''
    while num // n:
        encoded += N[num % n]
        num //= n
    encoded += N[num % n]
    return encoded[::-1]