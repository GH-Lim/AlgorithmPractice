T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    start = []
    end = []
    people = []
    group = [[] for i in range(N)]
    cnt = 1

    for m in range(M):
        p_list = list(map(int, input().split()))
        people.append(p_list)
    # print(people) = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]

    for p in people:
        start.append(p[0])
        end.append(p[1])
    # start = [1, 2, 5, 3, 4]
    # end = [2, 5, 1, 4, 6]

    # 처음 관계되는 start, end를 group 1에 넣어둠
    group[0].append(start[0])
    group[0].append(end[0])
    start.pop(0)
    end.pop(0)
    # group = [[1, 2], [], [], [], [], []]

    # # i = 0은 이미 했다
    # for i in range(1, M):
    #     flag = 0
    #     for g in range(cnt): # 현재까지 채워져 있는 그룹
    #         if start[i] in group[g] or end[i] in group[g]:
    #             group[g].append(start[i])
    #             group[g].append(end[i])
    #             flag = 1
    #     if flag == 0:
    #         group[cnt].append(start[i])
    #         group[cnt].append(end[i])
    #         cnt += 1
    while start:
        flag = 0
        print('시작 전,', start, end, group)
        for i in range(cnt):  # group[i]
            for s in range(len(start)):
                print('ddd', len(start))
                if start[s] in group[i]:
                    group[i].append(end[s])
                    start.pop(s)
                    end.pop(s)
                    flag = 1
                print('if문 시행', start, end, group)
        print('for문돌고', start, end, group)

        if flag == 0:
            group[cnt].append(start(0))
            group[cnt].append(end(0))
            start.pop(0)
            end.pop(0)
            cnt += 1
        print('if문 끝나고', start, end, group)

    print(group)

    print(cnt)




