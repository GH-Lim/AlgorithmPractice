from collections import deque

N = int(input())

arr = [list(input()) for _ in range(N)]
wood = []
end = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            wood.append([i, j])
        elif arr[i][j] == 'E':
            end.append([i, j])

woods = deque([wood])
cnt = 0
while woods:
    cnt += 1
    for i in