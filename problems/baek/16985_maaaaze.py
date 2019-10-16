from collections import deque

def rotate(plate, plates):
    plate90 = []
    plate180 = []
    plate270 = []
    for i in range(5):
        row90 = []
        row180 = []
        row270 = []
        for j in range(5):
            row90.append(plate[5 - 1 - j][i])
            row180.append(plate[5 - 1 - i][5 - 1 - j])
            row270.append(plate[j][5 - 1 - i])
        plate90.append(row90)
        plate180.append(row180)
        plate270.append(row270)
    plates.append(plate90)
    plates.append(plate180)
    plates.append(plate270)


def bfs(y, x, z):
    queue = deque()
    queue.append((y, x, z))
    while queue:
        for _ in range(len(queue)):
            y, x, z = queue.popleft()
            visited[y][x][z] = 1
            for v in range(6):
                next_y, next_x, next_z = y + dy[v], x + dx[v], z + dz[v]
                if 0 <= next_y < 5 and 0 <= next_x < 5 and 0 <= next_z < 5:
                    if



plate1 = [list(map(int, input().split())) for _ in range(5)]
p1 = [plate1]
rotate(plate1, p1)
plate2 = [list(map(int, input().split())) for _ in range(5)]
p2 = [plate2]
rotate(plate2, p2)
plate3 = [list(map(int, input().split())) for _ in range(5)]
p3 = [plate3]
rotate(plate3, p3)
plate4 = [list(map(int, input().split())) for _ in range(5)]
p4 = [plate4]
rotate(plate4, p4)
plate5 = [list(map(int, input().split())) for _ in range(5)]
p5 = [plate5]
rotate(plate5, p5)

visited = list(list([0]*5 for _ in range(5)) for _ in range(5))

cube = [[] for _ in range(5)]

dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for a in range(4):
    cube[0] = p1[a]
    for b in range(4):
        cube[1] = p2[b]
        for c in range(4):
            cube[2] = p3[c]
            for d in range(4):
                cube[3] = p4[c]
                for e in range(4):
                    cube[4] = p5[c]

                    bfs(0, 0, 0)
