from _collections import deque

l = deque(list(input()))
r = deque()

M = int(input())

cursor = len(l)

for _ in range(M):
    c = input()
    if c[0] == 'L':
        if l:
            r.appendleft(l.pop())
    elif c[0] == 'D':
        if r:
            l.append(r.popleft())
    elif c[0] == 'B':
        if l:
            l.pop()
    else:
        l.append(c[2])

print(''.join(l) + ''.join(r))
