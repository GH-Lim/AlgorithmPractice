def select(k, s1, s2):
    if k == len(people):
        solve(s1, s2)
        return
    select(k + 1, s1 + [k], s2)

    select(k + 1, s1, s2 + [k])


def solve(s1, s2):
    global ans
    cnt = 0
    to_stair1 = sorted([to_stair[s][0] for s in s1])
    to_stair2 = sorted([to_stair[s][1] for s in s2])

    stair1 = []
    stair2 = []
    stair1_q = []
    stair2_q = []
    while cnt < ans:
        while to_stair1 and to_stair1[0] == cnt:
            to_stair1.pop(0)
            stair1_q.append(0)
        while to_stair2 and to_stair2[0] == cnt:
            to_stair2.pop(0)
            stair2_q.append(0)
        for i in range(len(stair1)):
            stair1[i] += 1
        while stair1 and stair1[0] == stairs[0]:
            stair1.pop(0)
        for i in range(len(stair2)):
            stair2[i] += 1
        while stair2 and stair2[0] == stairs[1]:
            stair2.pop(0)

        while stair1_q and len(stair1) < 3:
            stair1.append(stair1_q.pop())
        while stair2_q and len(stair2) < 3:
            stair2.append(stair2_q.pop())

        cnt += 1

        if not stair1 and not stair2 and not to_stair2 and not to_stair1:
            ans = cnt


for tc in range(1, int(input()) + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    stair_l = []
    stairs = []
    people = []
    ans = 1000
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append((i, j))
            if room[i][j] > 1:
                stair_l.append((i, j))
                stairs.append(room[i][j])
    to_stair = []
    for person in people:
        d = []
        for stair in stair_l:
            d.append(abs(person[0] - stair[0]) + abs(person[1] - stair[1]))
        to_stair.append(d)
    select(0, [], [])
    print('#%d %d' % (tc, ans))
