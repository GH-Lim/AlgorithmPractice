def solution(files):
    answer = []
    for file in files:
        temp = ['', '', '']
        i = 0
        for char in file:
            if i == 0 and char.isnumeric():
                i += 1
            elif i == 1 and not char.isnumeric():
                i += 1
            temp[i] += char
        answer.append(temp)
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(f) for f in answer]
