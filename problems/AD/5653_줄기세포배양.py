dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    plate = [list(map(int, input().split())) for _ in range(N)]
    cells = {}
    for i in range(N):
        for j in range(M):
            if plate[i][j]:
                cells[(i, j)] = [0, plate[i][j], 0]  # state, X, cnt
    dead_cnt = 0
    for i in range(K):
        # 활성화 번식 카운트
        sub_cells = {}
        for cell, info in cells.items():
            y, x = cell
            if info[0] == 1:
                info[2] += 1
                if info[1] == info[2]:
                    info[0] += 1
                    dead_cnt += 1
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if (ny, nx) not in cells and (ny, nx) not in sub_cells:
                        sub_cells[(ny, nx)] = [0, info[1], 0]
                    elif (ny, nx) not in cells and (ny, nx) in sub_cells:
                        if sub_cells[(ny, nx)][1] < info[1]:
                            sub_cells[(ny, nx)][1] = info[1]
            # 비활 카운트
            if info[0] == 0:
                info[2] += 1
                if info[1] == info[2]:
                    info[2] = 0
                    info[0] += 1
        cells.update(sub_cells)
    print('#%d %d' % (tc, len(cells) - dead_cnt))
