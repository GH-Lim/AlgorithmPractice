from heapq import heappop, heappush

def calc_day(month, day):
    res = 0
    for i in range(month):
        if i in {1, 3, 5, 7, 8, 10, 12}:
            res += 31
        elif i in {4, 6, 9, 11}:
            res += 30
        else:
            res += 28
    return res + day

def solution(n, customers):
    times = []
    rest = []
    work = []
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        heappush(rest, (0, i))

    for customer in customers:
        date, time, minute = customer.split()
        MM, DD = map(int, date.split('/'))
        hh, mm, ss = map(int, time.split(':'))
        d = calc_day(MM, DD)

        arrival = d * 24 * 3600 + hh * 3600 + mm * 60 + ss
        if times and times[-1][0] > arrival:
            arrival += 365 * 24 * 3600
        times.append((arrival, int(minute) * 60))

    for arr_time in times:
        t, m = arr_time
        while work:
            fin_time, num = heappop(work)
            if t >= fin_time:
                heappush(rest, (fin_time, num))
            else:
                heappush(work, (fin_time, num))
                break
        if rest:
            _, num = heappop(rest)
            cnt[num] += 1
            heappush(work, (t + m, num))
        else:
            fin_time, num = heappop(work)
            cnt[num] += 1
            heappush(work, (fin_time + m, num))
    return max(cnt)