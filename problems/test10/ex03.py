from collections import deque

def solution(enter, leave):
    answer = []
    room = []
    enter = deque(enter)
    leave = deque(leave)
    visit = set()

    e = enter.popleft()
    visit.add(e)
    room.append(e)

    l = leave.popleft()
    while enter or leave:
        if e != l:
            e = enter.popleft()
            visit.add(e)
            room.append(e)
        while l in visit:
            room.append(l)
            if leave:
                l = leave.popleft()
            else:
                l = -1
    print(room)
    return answer

enter = [1, 4, 2, 3]
leave = [2, 1, 4, 3]

print(solution(enter, leave))