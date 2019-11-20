k = 10**12
room_number = [1,3,4,1,3,1]

def solution(k, room_number):
    rooms = set()
    min_room = {}
    answer = []
    def find_min_room(num):
        if num not in min_room:
            answer.append(num)
            return num + 1
        return find_min_room(min_room[num])
    for i in room_number:
        if i not in min_room:
            min_room[i] = find_min_room(i)
        else:
            min_room[min_room[i]] = find_min_room(min_room[i])
            min_room[i] = min_room[min_room[i]]
    print(min_room)
    # for i in room_number:
    #     if i >= min_room:
    #         for j in range(i, k + 1):
    #             if j not in rooms:
    #                 answer.append(j)
    #                 rooms.add(j)
    #                 if min_room == j:
    #                     min_room += 1
    #                 break
    #     else:
    #         for j in range(min_room, k + 1):
    #             if j not in rooms:
    #                 answer.append(j)
    #                 rooms.add(j)
    #                 if min_room == j:
    #                     min_room += 1
    #                 break
    return answer

print(solution(k, room_number))