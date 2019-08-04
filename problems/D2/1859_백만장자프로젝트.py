import sys
sys.stdin = open('input_1859.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    '''
    first_index = 0
    store = 0
    gain = 0
    max_index = prices.index(max(prices))
    for i in range(N):
        if i == max_index:
            gain += prices[max_index] * store
            if max_index != N-1:
                sub_prices = prices[max_index+1:]
                max_index += sub_prices.index(max(sub_prices)) + 1
                store = 0
        else:
            gain -= prices[i]
            store += 1
    '''  # Runtime Error

    sell_price = prices[-1]
    gain = 0
    for i in range(N-1, -(N-1), -1):
    # for i in reversed(range(N)):
        if prices[i] <= sell_price:
            gain += (sell_price-prices[i])
        else:
            sell_price = prices[i]

    print('{} {}'.format(tc, gain))
