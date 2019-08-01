T = int(input())

for tc in range(1, T+1):
    N = int(input())
    factors = [2, 3, 5, 7, 11]
    powers = [0] * 5
    while N != 1:
        for factor in enumerate(factors):
            if N % factor[1] == 0:
                powers[factor[0]] += 1
                N /= factor[1]
    result = ' '.join(map(str, powers))
    print('#{0} {1}'.format(tc, result))
