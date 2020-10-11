ans = -1

N, M, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

sharks = {}
smells = {}
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            sharks[(i, j)] = [arr[i][j], k]
vec = {}
for idx, v in enumerate(list(map(int, input().split()))):
    vec[idx + 1] = v
priority = {}
for i in range(M):
    priority[i + 1] = {}
    for j in range(1, 5):
        priority[i + 1][j] = list(map(int, input().split()))
for a in range(1001):
    if len(sharks) == 1:
        ans = a
        break

    delete = []
    for yx in smells:
        smells[yx][1] -= 1
        if smells[yx][1] == 0:
            delete.append(yx)
    for yx in delete:
        smells.pop(yx)
    new_sharks = {}
    for y, x in sharks:
        shark = sharks[(y, x)][0]
        v = vec[shark]
        temp = (-1, -1, -1)
        for d in priority[shark][v]:
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < N) or not (0 <= nx < N):
                continue
            elif (ny, nx) in smells and smells[(ny, nx)][0] == shark and temp == (-1, -1, -1):
                temp = (ny, nx, d)
                continue
            elif (ny, nx) in smells:
                continue
            else:
                if (ny, nx) in new_sharks:
                    if shark < new_sharks[(ny, nx)][0]:
                        new_sharks[(ny, nx)][0] = shark
                        vec[shark] = d
                    break
                else:
                    new_sharks[(ny, nx)] = [shark, k]
                    vec[shark] = d
                    break
        else:
            if temp == (-1, -1, -1):
                new_sharks[(y, x)] = sharks[(y, x)]
            else:
                ny, nx, d = temp
                new_sharks[(ny, nx)] = [shark, k]
                vec[shark] = d
    smells.update(sharks)
    sharks = new_sharks
print(ans)
