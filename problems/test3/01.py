for tc in range(1, int(input()) + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    k, r, c = 0, 0, 0

    for i in range(N):
        row = [0] * N
        col = [0] * N
        for j in range(N):
            if i == j: k += matrix[i][j]

            row[matrix[i][j] - 1] += 1

            col[matrix[j][i] - 1] += 1

        for m in range(N):
            if row[m] > 1:
                r += 1
                break
        for n in range(N):
            if col[n] > 1:
                c += 1
                break

    print('Case #%d: %d %d %d' % (tc, k, r, c))
