def ampersand(n):  # & 연산
    cnt = 0
    temp = 1
    while temp <= n:
        cnt += 1
        temp += cnt
    temp -= cnt
    cnt += 1
    x = 1
    y = cnt - x
    while temp != n:
        temp += 1
        x += 1
        y -= 1
    return x, y


def plus(a, b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y


def sharp(a, b):
    cnt = a + b
    jmp = a - 1
    num = 1
    for i in range(1, cnt - 1):
        num += i
    return num + jmp


def star(a, b):
    return sharp(*plus(ampersand(a), ampersand(b)))


T = int(input())
for tc in range(1, T + 1):
    print('#{} {}'.format(tc, star(*map(int, input().split()))))
