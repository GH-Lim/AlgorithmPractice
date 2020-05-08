def solution(n, t, m, timetable):
    answer = ''
    ans_time = 0
    times = []
    for time in timetable:
        hh, mm = time.split(':')
        times.append(int(hh) * 60 + int(mm))
    times.sort()

    depart = 9 * 60

    crew_idx = 0
    for _ in range(n):
        cnt = 0
        while cnt < m:
            if crew_idx == len(times):
                break
            if times[crew_idx] <= depart:
                crew_idx += 1
                cnt += 1
            else:
                break
        depart += t
    if cnt == m:
        ans_time = times[crew_idx - 1] - 1
    else:
        ans_time = depart - t
    answer = str(ans_time // 60).zfill(2) + ":" + str(ans_time % 60).zfill(2)
    return answer


print(solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']))
print(solution(2, 10, 2, ['09:10', '09:09', '08:00']))
print(solution(2, 1, 2, ['09:00', '09:00', '09:00', '09:00']))
print(solution(1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']))
print(solution(1, 1, 1, ['23:59']))
print(solution(10, 60, 45, ['23:59', '23:59', '23:59', '23:59',
                            '23:59', '23:59', '23:59', '23:59',
                            '23:59', '23:59', '23:59', '23:59',
                            '23:59', '23:59', '23:59', '23:59']))