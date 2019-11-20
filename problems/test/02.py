s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"


def solution(s):
    stack = []
    sub_s = set()
    sub_num = ''
    sub_ans = {0: set()}
    for char in s:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if sub_num:
                sub_s.add(int(sub_num))
                sub_num = ''
            stack.pop()
            sub_ans[len(sub_s)] = sub_s.copy()
            sub_s.clear()
        elif char == ',':
            if sub_num:
                sub_s.add(int(sub_num))
                sub_num = ''
        else:
            sub_num += char
    answer = []

    for i in range(1, len(sub_ans)):
        for element in sub_ans[i]:
            if element in sub_ans[i - 1]:
                continue
            else:
                answer.append(element)
                break
    return answer

solution(s)