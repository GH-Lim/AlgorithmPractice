N = int(input())
clap = '369'
numbers = []

for i in range(1, N + 1):
    if ('3' or '6' or '9') in str(i):
        count = 0
        for digit in str(i):
            if digit in clap:
                count += 1
        numbers.append('-' * count)
    else:
        numbers.append(i)


print(numbers)
