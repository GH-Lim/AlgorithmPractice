import sys
sys.stdin = open('input.txt', 'r')


def left_rotate()


L = int(input())

u, v, w, x, y = map(int, input().split())

plate = [list(map(int, input().split())) for _ in range(L)]

visited = [[0]*L for _ in range(L)]
