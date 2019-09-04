T = int(input())

for t in range(1, T+1):
    N = int(input())
    danjo_list = []
    n_list = sorted(list(map(int, input().split())))
    isdanjo = ''
    result = False
    max_num = 0
    if len(n_list) == 1:
        print('#{} -1'.format(t))
    else:
        for i in range(len(n_list)-2, -1, -1):
            for j in range(len(n_list)-1, i, -1):
                # print(i,j)
                isdanjo = str(n_list[i] * n_list[j])
                for d in range(len(isdanjo) - 1):
                    if int(isdanjo[d]) <= int(isdanjo[d+1]):
                        result = True
                    else:
                        result = False
                        max_num = -1
                        break
                if result == True:
                    answer = int(isdanjo)
                    if max_num < answer:
                        max_num = answer
        print('#{} {}'.format(t, max_num))