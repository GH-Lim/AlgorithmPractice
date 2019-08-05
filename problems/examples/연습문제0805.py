arr = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
'''
0 1 1 1 0
1 2 1 2 1
1 1 0 1 1
1 2 1 2 1
0 1 1 1 0
'''
def my_abs(num):
    return num if num >= 0 else - num

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr_result = [[0 for n in range(5)] for m in range(5)]
'''
벽인지 아닌지 구분해라
'''
# def isWall(textX, testY) == False:


print(arr_result)
