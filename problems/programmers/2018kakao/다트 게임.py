def solution(dartResult):
    i = 0
    score = [0, 0, 0]
    dart = 0
    while i < len(dartResult):
        if dartResult[i] == '*':
            if dart == 1:
                score[0] *= 2
            else:
                score[dart - 2] *= 2
                score[dart - 1] *= 2
            i += 1

        elif dartResult[i] == '#':
            score[dart - 1] *= -1
            i += 1

        else:
            dart += 1
            if dartResult[i: i + 2] == '10':
                curr = 10
                i += 1
            else:
                curr = int(dartResult[i])
            if dartResult[i + 1] == 'S':
                score[dart - 1] = curr
            elif dartResult[i + 1] == 'D':
                score[dart - 1] = curr ** 2
            elif dartResult[i + 1] == 'T':
                score[dart - 1] = curr ** 3
            i += 2
    answer = sum(score)
    return answer


dartResult = [
    # '1S2D*3T',
    '1D2S#10S',
    '1D2S0T',
    '1S*2T*3S',
    '1D#2S*3S',
    '1T2D3D#',
    '1D2S3T*'
    ]
for d in dartResult:
    print(solution(d))