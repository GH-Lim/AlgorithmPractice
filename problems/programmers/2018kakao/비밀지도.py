def solution(n, arr1, arr2):
    answer = []

    map1 = [bin(code)[2:].zfill(n) for code in arr1]
    map2 = [bin(code)[2:].zfill(n) for code in arr2]
    for i in range(n):
        line = ''
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                line += ' '
            else:
                line += '#'
        answer.append(line)

    return answer
