nodes = [[10, i] for i in range(10)]

a = nodes[0]
stack = [a]
print(a)
nodes[0][0] = 3
print(a)
print(stack)
