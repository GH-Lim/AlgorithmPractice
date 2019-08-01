import sys

sys.stdin = open('input_1954.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    t_arr = [[0 for n in range(N)] for m in range(N)]
    i = 0
    j = 0
    up_i = 0
    down_i = N-1
    right_j = N-1
    left_j = 0
    #print(t_arr)
    for k in range(1, N*N+1):
        t_arr[i][j] = k
        if i == up_i and j < right_j:
            j += 1
            if j == right_j:
                up_i += 1
        elif j == right_j and i < down_i:
            i += 1
            if i == down_i:
                right_j -= 1
        elif i == down_i and j > left_j:
            j -= 1
            if j == left_j:
                down_i -= 1
        elif j == left_j and i > up_i:
            i -= 1
            if i == up_i:
                left_j += 1
    print('#{}'.format(tc))
    for arr in t_arr:
        print(' '.join(map(str, arr)))



