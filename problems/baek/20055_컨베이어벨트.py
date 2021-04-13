from collections import deque

N, K = map(int, input().split())
step = 0
count = 0
robots = deque([0] * N)
belt = deque(list(map(int, input().split())))

while count < K:
    step += 1
    belt.rotate(1)
    robots.pop()
    robots.appendleft(0)
    robots[N - 1] = 0
    for i in range(N - 1):
        if robots[N - i - 1] == 0 and robots[N - i - 2] == 1 and belt[N - i - 1] > 0:
            robots[N - i - 1], robots[N - i - 2] = robots[N - i - 2], robots[N - i - 1]
            belt[N - i - 1] -= 1
            if belt[N - i - 1] == 0:
                count += 1
    if belt[0] > 0:
        belt[0] -= 1
        if belt[0] == 0:
            count += 1
        robots[0] = 1
print(step)
