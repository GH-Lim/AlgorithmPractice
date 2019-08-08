import sys
sys.stdin = open('input_7675.txt', 'r')

print('Aa'.isalpha())
T = int(input())


def isName(word):
    if len(word) == 1:
        return word.isupper()
    else:
        if word.isalpha():
            if word[0].islower():
                return False
            else:
                if word[1:].islower():
                    return True
                else:
                    return False
        else:
            return False


pp = ['.', '?', '!']
for tc in range(1, T + 1):
    N = int(input())
    name_count = [0] * N
    sentences = input()
    for i in range(3):
        # n = sentence.count(pp[i])
        for _ in range(sentences.count(pp[i])):
            sentences = sentences.replace(pp[i], ':')
    sentences = sentences.split(':')
    for i in range(N):
        words = sentences[i].strip(':').strip().split()
        for word in words:
            if isName(word):
                name_count[i] += 1
    print('#{} {}'.format(tc, ' '.join(map(str, name_count))))
