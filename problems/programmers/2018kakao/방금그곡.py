def solution(m, musicinfos):
    musics = {}
    for musicinfo in musicinfos:
        s, e, title, a = musicinfo.split(',')
        sM, sm = map(int, s.split(':'))
        eM, em = map(int, e.split(':'))
        t = (eM - sM) * 60 + em - sm
        musics[title] = a * (t // len(a)) + a[:t % len(a)]
    for title, mm in musics.items():
        if m in mm:
            return title
    return '(None)'

print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))