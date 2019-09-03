# def solve(n, k):
#     global days
#     global money
#     global result
#     if n == 0 or days > N:
#         return
#     for i in range(k, N+1):
#         if not visited[i]:
#             if i + TP[i][0] > N + 1:
#                 return
#             for j in range(TP[i][0]):
#                 visited[i+j] = 1
#             days += TP[i][0]
#             if days < N:
#                 money += TP[i][1]
#                 if money > result:
#                     result = money
#                 solve(n-1, k + 1)
#                 money -= TP[i][1]
#             days -= TP[i][0]
#             for j in range(TP[i][0]):
#                 visited[i + j] = 0
def dfs(day, money):
    global result
    if day == N + 1:
        result = result if result > money else money
        return
    if day + TP[day][0] <= N + 1:
        dfs(day + TP[day][0], money + TP[day][1])
    dfs(day + 1, money)


N = int(input())
TP = [[] for _ in range(N+1)]
for i in range(1, N+1):
    TP[i] = list(map(int, input().split()))
result = 0
dfs(1, 0)
print(result)