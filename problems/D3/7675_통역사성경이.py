import sys
sys.stdin = open('input_7675.txt', 'r')

print('A'.isupper())
T = int(input())


def isName(word):
    if len(word) == 1:
        return word.isupper()
    else:
        if word[0].islower():
            return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper() or word[i].isdigit():
                    return False
        return True


pp = ['.', '?', '!']
for tc in range(1, T + 1):
    N = int(input())
    name_count = [0] * N
    sentences = input()
    for i in range(3):
        # n = sentence.count(pp[i])
        for _ in range(sentences.count(pp[i])):
            sentences = sentences.replace(pp[i], ':')
    sentences = sentences.strip(':').split(':')
    for i in range(N):
        words = sentences[i].strip().split()
        for word in words:
            if isName(word):
                name_count[i] += 1
    print('#{} {}'.format(tc, ' '.join(map(str, name_count))))
