from _collections import deque

N, M, f = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(N)]

taxi_y, taxi_x = map(int, input().split())
taxi_y -= 1
taxi_x -= 1

depart = {}
dest = {}

ans = f

for i in range(1, M + 1):
    depart_y, depart_x, dest_y, dest_x = map(int, input().split())
    depart_y, depart_x, dest_y, dest_x = depart_y - 1, depart_x - 1, dest_y - 1, dest_x - 1
    depart[(depart_y, depart_x)] = i
    dest[i] = (dest_y, dest_x)


dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(start):
    global ans

    q = deque([start])
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    while q:
        # if ans <= cnt:
        #     ans = -1
        #     return False
        for _ in range(len(q)):
            y, x = q.popleft()
            if (y, x) in depart:
                if ans <= 0:
                    ans = -1
                    return False
                return (y, x), depart.pop((y, x))
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                # if (ny, nx) in depart:
                #     ans -= cnt + 1
                #     return (ny, nx), depart.pop((ny, nx))
                if not (0 <= ny < N) or not (0 <= nx < N):
                    continue
                if area[ny][nx] == 1 or visited[ny][nx] == 1:
                    continue
                visited[ny][nx] = 1
                q.append((ny, nx))
        q = deque(sorted(q))
        ans -= 1
    ans = -1
    return False


def to_dest(start, end):
    global ans

    q = deque([start])
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    cnt = 0
    while q:
        # if ans < cnt:
        #     ans = -1
        #     return False
        for _ in range(len(q)):
            if ans < cnt:
                ans = -1
                return False
            y, x = q.popleft()
            if (y, x) == end:
                ans += cnt
                return y, x
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                # if (ny, nx) == end:
                #     ans += cnt + 1
                #     return ny, nx
                if not (0 <= ny < N) or not (0 <= nx < N):
                    continue
                if area[ny][nx] == 1 or visited[ny][nx] == 1:
                    continue
                visited[ny][nx] = 1
                q.append((ny, nx))
        cnt += 1
    ans = -1
    return False

next_s = taxi_y, taxi_x

while next_s:
    next_e = bfs(next_s)
    if not next_e:
        break
    s, e = next_e
    next_s = to_dest(s, dest[e])
    if len(depart) == 0:
        break

print(-1 if len(depart) else ans)