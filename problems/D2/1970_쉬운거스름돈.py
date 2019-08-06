import sys

sys.stdin = open('input_1970.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = {}
    for money in moneys:
        count = 0
        if N >= money:
            count = N // money
            N -= (money * count)
        result[money] = count
    # print(result)
    print('#{}\n{}'.format(tc, ' '.join(map(str, result.values()))))
