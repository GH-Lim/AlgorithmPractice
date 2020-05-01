# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    s_split = S.split()
    stack = []
    for s in s_split:
        if s == 'POP':
            if stack:
                stack.pop()
            else:
                return -1
        elif s == 'DUP':
            if stack:
                stack.append(stack[-1])
            else:
                return -1
        elif s == '+':
            if len(stack) >= 2:
                top = stack.pop()
                stack[-1] += top
            else:
                return -1
        elif s == '-':
            if len(stack) >= 2:
                top = stack.pop()
                stack[-1] = top - stack[-1]
            else:
                return -1
        else:
            stack.append(int(s))

        if stack[-1] > 2 ** 20 - 1 or stack[-1] < 0:
            return -1
    if not stack:
        return -1
    return stack[-1]
