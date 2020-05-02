def solution(s):
    s = [list(map(int, s.split(','))) for s in s.strip('{{').strip('}}').split('},{')]
    s.sort(key=lambda x: len(x))
    answer = s[0]
    for i in range(1, len(s)):
        answer.extend([n for n in s[i] if n not in s[i - 1]])
    return answer