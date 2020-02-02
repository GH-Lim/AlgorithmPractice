def solution(A):
    N = len(A)
    res = 0
    def comb(n, str_set, ans):
        global res
        if n == N:
            res = max(res, ans)
            return
        temp = str_set + A[n]
        if len(str_set) + len(A[n]) == len(set(temp)):
            comb(n + 1, temp, max(ans, len(temp)))
        comb(n + 1, str_set, ans)
    comb(0, '', 0)
    return res
A = ['co', 'dil', 'ity']
print(solution(A))
