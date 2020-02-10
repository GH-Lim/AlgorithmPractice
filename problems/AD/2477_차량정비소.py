import heapq
T = 10
N, M, K, A, B = map(int, input().split())
a = map(int, input().split())  # N 개
b = map(int, input().split())  # M 개
t = map(int, input().split())  # K 개

heapq.heapify(t)