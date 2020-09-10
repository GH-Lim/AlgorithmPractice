def solution(n):
    answer = []
    for i in range(1, n + 1):
        answer.append([0] * i)
    di = [1, 0, -1]
    dj = [0, 1, -1]

    k = 1
    i, j = 0, 0
    d = 0
    while k <= n * (n + 1) * 0.5:
        ni, nj = i + di[d], j + dj[d]
        try:
            if answer[ni][nj]:
                d = (d + 1) % 3
        except:
            d = (d + 1) % 3
        answer[i][j] = k
        k += 1
        i += di[d]
        j += dj[d]
    # 확인용
    # for a in answer:
    #     print(a)
    return sum(answer, [])