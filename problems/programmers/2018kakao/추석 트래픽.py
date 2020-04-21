def solution(lines):
    answer = 0
    traffic_time = {}
    for idx, line in enumerate(lines):
        s, S, T = line.split(' ')
        h, m, s = S.split(':')
        end = int(h) * 3600 + int(m) * 60 + float(s)
        end = int(end * 1000)
        T = int(float(T.rstrip('s')) * 1000)
        start = end - T + 1

        start -= 999.9  # 1초보다 작은시간으로 늘려준다.
        if start not in traffic_time:
            traffic_time[start] = idx
        else:
            while start in traffic_time:
                start -= 0.001
            traffic_time[start] = idx
        if end not in traffic_time:
            traffic_time[end] = idx
        else:
            while end in traffic_time:
                end -= 0.001
            traffic_time[end] = idx

    on_off = [0] * len(lines)
    for time, idx in sorted(traffic_time.items()):
        on_off[idx] = not on_off[idx]
        answer = max(answer, sum(on_off))

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
