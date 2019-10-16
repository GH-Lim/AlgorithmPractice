from collections import deque

q = deque([1, 2, 3, 4, 5, 6])

q.rotate(1)

print(q)

q.rotate(-1)

print(q)

q.rotate(-1)

print(q)
