# board = [1,  # 시작점
#          2, 3, 4, 5, 6,
#          7, 8, 9, 10, 11,
#          12, 13, 14, 15, 16,
#          17, 18, 19, 20, 21,
#          21,
#          23, 24, 30,
#          26, 30,
#          28, 29, 30,
#          31, 32, 20,
#          22, 25, 27]
board = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9],
    [22, 23, 24, 30, 31],
    [7, 8, 9, 10, 11],
    [8, 9, 10, 11, 12],
    [9, 10, 11, 12, 13],
    [10, 11, 12, 13, 14],
    [25, 16, 30, 31, 32],
    [12, 13, 14, 15, 16],
    [13, 14, 15, 16, 17],
    [14, 15, 16, 17, 18],
    [15, 16, 17, 18, 19],
    [27, 28, 29, 30, 31],
    [17, 18, 19, 20, 21],
    [18, 19, 20, 21, 21],
    [19, 20, 21, 21, 21],
    [20, 21, 21, 21, 21],
    [21, 21, 21, 21, 21],
    [],
    [23, 24, 30, 31, 32],
    [24, 30, 31, 32, 20],
    [30, 31, 32, 20, 21],
    [26, 30, 31, 32, 20],
    [30, 31, 32, 20, 21],
    [28, 29, 30, 31, 32],
    [29, 30, 31, 32, 20],
    [30, 31, 32, 20, 21],
    [31, 32, 20, 21, 21],
    [32, 20, 21, 21, 21],
    [20, 21, 21, 21, 21]
]
scores = [0,
          2, 4, 6, 8, 10,
          12, 14, 16, 18, 20,
          22, 24, 26, 28, 30,
          32, 34, 36, 38, 40,
          0,
          13, 16, 19,
          22, 24,
          28, 27, 26,
          25, 30, 35]
dices = list(map(int, input().split()))
ans = 0


def play(k, a, b, c, d, score):
    global ans
    if k == 10:
        ans = max(ans, score)
        return
    if a != 21:
        # ta = go(a, dices[k])
        ta = board[a][dices[k] - 1]
        if ta == 21 or ta not in [b, c, d]:
            play(k + 1, ta, b, c, d, score + scores[ta])
    if b != 21:
        # tb = go(b, dices[k])
        tb = board[b][dices[k] - 1]
        if tb == 21 or tb not in [a, c, d]:
            play(k + 1, a, tb, c, d, score + scores[tb])
    if c != 21:
        # tc = go(c, dices[k])
        tc = board[c][dices[k] - 1]
        if tc == 21 or tc not in [a, b, d]:
            play(k + 1, a, b, tc, d, score + scores[tc])
    if d != 21:
        # td = go(d, dices[k])
        td = board[d][dices[k] - 1]
        if td == 21 or td not in [a, b, c]:
            play(k + 1, a, b, c, td, score + scores[td])


# def go(unit, num):
#     unit = 33 if unit == 5 else 34 if unit == 10 else 35 if unit == 15 else unit
#     for _ in range(num):
#         if unit == 21: return unit
#         unit = board[unit]
#     return unit


play(0, 0, 0, 0, 0, 0)
print(ans)
