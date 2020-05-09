def solution(numbers, hand):
    answer = ''
    key_pad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1),
        '*': (3, 0),
        '#': (3, 2),
    }
    ly, lx = key_pad['*']
    ry, rx = key_pad['#']

    for num in numbers:
        if num in [1, 4, 7]:
            ly, lx = key_pad[num]
            answer += 'L'
        elif num in [3, 6, 9]:
            ry, rx = key_pad[num]
            answer += 'R'
        else:
            ny, nx = key_pad[num]
            if abs(ny - ly) + abs(nx - lx) > abs(ny - ry) + abs(nx - rx):
                ry, rx = key_pad[num]
                answer += 'R'
            elif abs(ny - ly) + abs(nx - lx) < abs(ny - ry) + abs(nx - rx):
                ly, lx = key_pad[num]
                answer += 'L'
            else:
                if hand == 'right':
                    ry, rx = key_pad[num]
                    answer += 'R'
                else:
                    ly, lx = key_pad[num]
                    answer += 'L'

    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
