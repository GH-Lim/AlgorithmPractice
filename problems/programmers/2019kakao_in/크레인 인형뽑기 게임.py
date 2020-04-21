from collections import deque


def solution(board, moves):
    answer = 0

    sub_board = []

    for arr in zip(*board):
        sub_arr = deque()
        for e in arr:
            if e:
                sub_arr.append(e)
        sub_board.append(sub_arr)

    basket = []
    for move in moves:
        if sub_board[move - 1]:
            doll = sub_board[move - 1].popleft()
            if basket and basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)
        else:
            continue
    return answer
