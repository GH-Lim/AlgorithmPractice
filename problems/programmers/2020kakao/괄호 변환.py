def solution(p):
    answer = ''
    u, v, u_is_correct = split_balance(p)
    if u_is_correct:
        answer += u
        if v == '':
            return answer
        return answer + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
    return answer


def split_balance(string):
    stack = []
    open_cnt = 0
    close_cnt = 0
    u_is_correct = True
    split_idx = 0
    for idx in range(len(string)):
        if string[idx] == '(':
            if u_is_correct:
                stack.append('(')
            open_cnt += 1
        else:
            if stack and u_is_correct:
                stack.pop()
            else:
                u_is_correct = False
            close_cnt += 1
        if open_cnt == close_cnt:
            split_idx = idx
            break
    u = string[:split_idx + 1]
    v = string[split_idx + 1:]
    return u, v, u_is_correct