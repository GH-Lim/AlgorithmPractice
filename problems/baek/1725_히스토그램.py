n = int(input())
stack = []
ans = 0

for i in range(n + 1):
    height = -1
    if i < n:
        height = int(input())
    left = i
    while stack and stack[-1][1] > height:
        ans = max(ans, (i - stack[-1][0]) * stack[-1][1])
        left = stack.pop()[0]
    stack.append((left, height))
print(ans)