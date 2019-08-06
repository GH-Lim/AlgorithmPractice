N = int(input())
clap = '369'
numbers = []

for i in range(1, N + 1):
    count = 0
    for digit in str(i):
        if digit in clap:
            count += 1
    if count:
        numbers.append('-' * count)
    else:
        numbers.append(str(i))

print(' '.join(numbers))
