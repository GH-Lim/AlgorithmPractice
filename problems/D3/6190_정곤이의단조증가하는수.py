T = int(input())

for tc in range(1, T+1):
    N = int(input())
    max_num = 0
    for n in range(N):
        nums = input().split()
        for num in nums:
            flag = True
            for i in range(len(num)):
                if int(num[i]) > int(num[i+1]):
                    flag = False
                    break
            if flag:
                max_num = max_num if max_num > num else num

