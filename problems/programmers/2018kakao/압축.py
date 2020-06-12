def solution(msg):
    answer = []
    index = 1
    dictionary = {}
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dictionary[char] = index
        index += 1
    i = 0
    while i < len(msg):
        j = 1
        while j < len(msg):
            if msg[i:i + j] in dictionary:
                j += 1
            else:

                index += 1
                break
        answer.append(dictionary[msg[i:i + j - 1]])
        dictionary[msg[i:i + j]] = index
        i += j - 1

    return answer

print(solution('KAKAO'))