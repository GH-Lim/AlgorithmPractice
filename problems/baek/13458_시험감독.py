N = int(input())
room = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = [1] * N
for i in range(N):
    room[i] -= B
    if room[i] > 0:
        room[i] += C - 1
        cnt[i] += room[i] // C

print(sum(cnt))
