# def solution(lines):
#     answer = 0
#     traffic_time = {}
#     for idx, line in enumerate(lines):
#         s, S, T = line.split(' ')
#         h, m, s = S.split(':')
#         end = int(h) * 3600 + int(m) * 60 + float(s)
#         end = int(end * 1000)
#         T = int(float(T.rstrip('s')) * 1000)
#         start = end - T + 1
#
#         start -= 999.9  # 1초보다 작은시간으로 늘려준다.
#         if start not in traffic_time:
#             traffic_time[start] = idx
#         else:
#             while start in traffic_time:
#                 start -= 0.001
#             traffic_time[start] = idx
#         if end not in traffic_time:
#             traffic_time[end] = idx
#         else:
#             while end in traffic_time:
#                 end -= 0.001
#             traffic_time[end] = idx
#
#     on_off = [0] * len(lines)
#     for time, idx in sorted(traffic_time.items()):
#         on_off[idx] = not on_off[idx]
#         answer = max(answer, sum(on_off))
#
#     return answer
def solution(lines):
    answer = 0
    start, end = [], []
    for line in lines:
        d, t, s = line.split()
        h, m, sec = map(float, t.split(":"))
        ms = h * 3600 + m * 60 + sec
        s = float(s[:-1])
        end.append(ms + 1)  # 끝지점일때도 1초 범위안에 들어있는 거니까 +1을 해주어서 길이를 늘려준다.
        start.append(ms - s + 0.001)

    start.sort()
    cnt = 0
    a, b = 0, 0
    l = len(lines)
    while a < l and b < l:
        if start[a] < end[b]:
            cnt += 1
            a += 1
            answer = max(answer, cnt)
        else:
            b += 1
            cnt -= 1
    return answer


print(solution([
    '2016-09-15 20:59:57.421 0.351s',
    '2016-09-15 20:59:58.233 1.181s',
    '2016-09-15 20:59:58.299 0.8s',
    '2016-09-15 20:59:58.688 1.041s',
    '2016-09-15 20:59:59.591 1.412s',
    '2016-09-15 21:00:00.464 1.466s',
    '2016-09-15 21:00:00.741 1.581s',
    '2016-09-15 21:00:00.748 2.31s',
    '2016-09-15 21:00:00.966 0.381s',
    '2016-09-15 21:00:02.066 2.62s'
]))
