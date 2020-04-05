def solution(inputString):
    answer = 0
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    for s in inputString:
        if s == "(":
            stack1.append(1)
        elif s == "{":
            stack2.append(2)
        elif s == "[":
            stack3.append(3)
        elif s == "<":
            stack4.append(4)
        elif s == ")":
            if len(stack1):
                stack1.pop()
                answer += 1
            else:
                answer = -1
                break
        elif s == "}":
            if len(stack2):
                stack2.pop()
                answer += 1
            else:
                answer = -1
                break
        elif s == "]":
            if len(stack3):
                stack3.pop()
                answer += 1
            else:
                answer = -1
                break
        elif s == ">":
            if len(stack4):
                stack4.pop()
                answer += 1
            else:
                answer = -1
                break
    if stack1: answer = -1
    if stack2: answer = -1
    if stack3: answer = -1
    if stack4: answer = -1

    return answer
