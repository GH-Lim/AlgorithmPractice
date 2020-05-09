def solution(n, path, order):
    answer = True
    G = [[0] * n for _ in range(n)]

    check_room = {}
    for o in order:
        a, b = o
        check_room[a] = b

    for p in path:
        a, b = p
        G[a][b] = 1
        G[b][a] = 1
    visited = [0] * n



    return answer

def explore(check_room, p):


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))