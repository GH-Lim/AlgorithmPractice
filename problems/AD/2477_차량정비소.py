from heapq import heappop, heappush
for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))  # N 개
    b = list(map(int, input().split()))  # M 개
    t = list(map(int, input().split()))  # K 개

    aq = []
    bq = []
