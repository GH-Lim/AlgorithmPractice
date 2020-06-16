def solution(m, musicinfos):
    musics = {}
    m = m.replace('A#', '0').replace('C#', '1').replace('D#', '2').replace('E#', '3').replace('F#', '4').replace('G#', '5')
    for musicinfo in musicinfos:
        s, e, title, a = musicinfo.split(',')
        a = a.replace('A#', '0').replace('C#', '1').replace('D#', '2').replace('E#', '3').replace('F#', '4').replace('G#', '5')
        sM, sm = map(int, s.split(':'))
        eM, em = map(int, e.split(':'))
        t = (eM - sM) * 60 + em - sm
        musics[title] = a * (t // len(a)) + a[:t % len(a)]
    for title, mm in sorted(musics.items(), key=lambda x: -len(x[1])):
        if m in mm:
            return title
    return '(None)'

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))