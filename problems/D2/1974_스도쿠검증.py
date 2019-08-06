import sys
sys.stdin = open('input_1974.txt', 'r')

T = int(input())
all_num = list(range(1, 10))


def isCorrect(sudoku):
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(sudoku[i][j])
            col.append(sudoku[j][i])
        # print(row)
        # print(col)
        if sorted(row) != all_num or sorted(col) != all_num:
            return 0
    for k in range(3):
        for l in range(3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(sudoku[3*l+i][3*k+j])
            # print(square)
            if sorted(square) != all_num:
                return 0
    return 1


for tc in range(1, T+1):
    sudoku = []
    for r in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
    result = isCorrect(sudoku)
    print('#{} {}'.format(tc, result))
