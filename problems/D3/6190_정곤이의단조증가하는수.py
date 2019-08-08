T = int(input())


def isMono(number):
    for i in range(len(number)-1):
        if int(number[i]) > int(number[i+1]):
            return False
    return True


for tc in range(1, T+1):
    N = int(input())
    max_num = 0
    A = list(map(int, input().split()))
    noMono = True
    for i in range(N-1):
        for j in range(i+1, N):
            target = str(A[i] * A[j])
            if isMono(target):
                noMono = False
                max_num = max_num if max_num > int(target) else int(target)
    result = -1 if noMono else max_num

    print('#{} {}'.format(tc, result))
