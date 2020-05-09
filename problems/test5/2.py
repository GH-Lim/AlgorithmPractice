from itertools import permutations
def solution(expression):
    answer = 0
    nums = []

    temp = ''
    op_idx = 0
    for char in expression:
        if char in '*+-':
            nums.append(int(temp))
            nums.append(char)
            temp = ''
        else:
            temp += char
    nums.append(int(temp))
    for perm in permutations([0, 1, 2]):
        sub = nums[:]
        for op in perm:
            i = 0
            while i < len(sub):
                if sub[i] == '*' and op == 0:
                    sub[i - 1:i + 2] = [sub[i - 1] * sub[i + 1]]
                elif sub[i] == '+' and op == 1:
                    sub[i - 1:i + 2] = [sub[i - 1] + sub[i + 1]]
                elif sub[i] == '-' and op == 2:
                    sub[i - 1:i + 2] = [sub[i - 1] - sub[i + 1]]
                else:
                    i += 1
        answer = max(answer, abs(sub[0]))
    return answer

print(solution("100-200*300-500+20"))