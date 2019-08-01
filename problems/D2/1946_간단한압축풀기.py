T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sumstring = ''
    for n in range(N):
        Ci, Ki = input().split()
        sumstring += Ci * int(Ki)
    tenwords = 0
    print('#{}'.format(tc))
    for i in range(len(sumstring)//10+1):
        print(sumstring[tenwords:tenwords+10])
        tenwords += 10
    print()
