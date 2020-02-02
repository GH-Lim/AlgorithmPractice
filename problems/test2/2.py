# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    temp = S.split()
    temp = ''.join(temp)
    temp = temp.split('-')
    temp = ''.join(temp)

    ans = ''
    len_temp = len(temp)
    if len_temp % 3 == 0:
        k = len_temp // 3
        for i in range(k):
            ans += temp[3 * i: 3 * i + 3]
            if i != k - 1:
                ans += '-'
    elif len_temp % 3 == 2:
        k = len_temp // 3
        for i in range(k):
            ans += temp[3 * i: 3 * i + 3]
            ans += '-'
        ans += temp[-2:]
    else:
        k = len_temp // 3 - 1
        for i in range(k):
            ans += temp[3 * i: 3 * i + 3]
            ans += '-'
        ans += temp[-4:-2]
        ans += '-'
        ans += temp[-2:]
    return ans