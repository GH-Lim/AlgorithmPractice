from collections import deque


N = int(input())

green = deque([[0] * 4 for _ in range(6)])
blue = deque([[0] * 4 for _ in range(6)])


def go_down(y, dir):
    nx = 0
    while nx + 1 < 6 and not dir[nx + 1][y]:
        nx += 1
    return nx


def go(t, x, y):
    if t == 1:
        g_location = go_down(y, green)
        green[g_location][y] = 1
        b_location = go_down(x, blue)
        blue[b_location][x] = 1
    elif t == 2:
        g_location = min(go_down(y, green), go_down(y + 1, green))
        green[g_location][y], green[g_location][y + 1] = 1, 1
        b_location = go_down(x, blue)
        blue[b_location][x], blue[b_location - 1][x] = 1, 1
    elif t == 3:
        g_location = go_down(y, green)
        green[g_location][y], green[g_location - 1][y] = 1, 1
        b_location = min(go_down(x, blue), go_down(x + 1, blue))
        blue[b_location][x], blue[b_location][x + 1] = 1, 1


def find_full(dir):
    i = 2
    score = 0
    while i < len(dir):
        if sum(dir[i]) == 4:
            del dir[i]
            dir.appendleft([0] * 4)
            score += 1
        else:
            i += 1
    return score


def push_block(dir):
    while sum(dir[1]):
        dir.pop()
        dir.appendleft([0] * 4)


ans = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    go(t, x, y)
    ans += find_full(green) + find_full(blue)
    push_block(green), push_block(blue)
print(ans)
print(sum(sum(blue, [])) + sum(sum(green, [])))
