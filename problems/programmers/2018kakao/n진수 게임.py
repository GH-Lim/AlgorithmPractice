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


# def solution(n, t, m, p):
#     m_chars = '0123456789ABCDEF'
#
#     def _rep(numb, to):
#         j, k = divmod(numb, to)
#         i = m_chars[k]
#         return ('' if j == 0 else _rep(j, to)) + i
#
#     numbers = ''
#     for i in range(0, t * m):
#         numbers += _rep(i, n)
#         if len(numbers) >= t * m:
#             break
#
#     result = ''
#     for i in range(p - 1, t * m, m):
#         result += numbers[i]
#
#     return result