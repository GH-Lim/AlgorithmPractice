import sys
sys.stdin = open('input_1961.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0]*N
    for r in range(N):
        row = input().split()
        arr[r] = row
    print('#{}'.format(tc))
    for i in range(N):
        row90 = []
        row180 = []
        row270 = []
        for j in range(N):
            row90.append(arr[N-1-j][i])
            row180.append(arr[N-1-i][N-1-j])
            row270.append(arr[j][N-1-i])
        print('{} {} {}'.format(''.join(row90), ''.join(row180), ''.join(row270)))
