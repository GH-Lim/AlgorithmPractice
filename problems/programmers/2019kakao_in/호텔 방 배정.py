import sys
sys.setrecursionlimit(200000)


class Reservation(object):
    def __init__(self):
        self.rooms = {}

    def check_room(self, num):
        if num not in self.rooms:
            self.rooms[num] = num
        if self.rooms[num] != num:
            self.rooms[num] = self.check_room(self.rooms[num])
        return self.rooms[num]

    def reserved(self, r, n):
        r, n = self.check_room(r), self.check_room(n)
        self.rooms[r] = n


def solution(k, room_number):
    answer = []
    r = Reservation()
    for num in room_number:
        room = r.check_room(num)
        answer.append(room)
        r.reserved(room, room + 1)
    return answer


# 재귀 없이 푸는 법
# def solution(k, room_number):
#     room_dic = {}
#     ret = []
#     for i in room_number:
#         n = i
#         visit = [n]
#         while n in room_dic:
#             n = room_dic[n]
#             visit.append(n)
#         ret.append(n)
#         for j in visit:
#             room_dic[j] = n+1
#     return ret