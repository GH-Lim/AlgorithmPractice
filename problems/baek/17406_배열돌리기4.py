import sys
sys.stdin = open('input_17406.txt', 'r')

N, M, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for k in range(K):
    r, c, s = map(int, input().split())
    for shell in range(s):
        left_top_x, left_top_y = r - s + shell, c - s + shell
        next_x, next_y = left_top_x, left_top_y
        flag = 0
        for i in range((2*s+1)**2 - (2*s-1)**2):
            mode = flag // (2 * (s-shell))
            next_x += dx[mode]
            next_y += dy[mode]
            arr[left_top_x][left_top_y], arr[next_x][next_y] = arr[next_x][next_y], arr[left_top_x][left_top_y]
            flag += 1
min_row = sum(arr[0])
for row in arr:
    if sum(row) < min_row:
        min_row = sum(row)

print(min_row)