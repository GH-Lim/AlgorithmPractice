# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    N = len(S)
    s = set()
    cnt = 1
    for i in range(N):
        if S[i] in s:
            s.clear()
            s.add(S[i])
            cnt += 1
        else:
            s.add(S[i])
    return(cnt)
