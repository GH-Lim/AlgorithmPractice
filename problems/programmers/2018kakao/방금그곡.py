A = {'A#': '1', 'C#': '4', 'D#': '6', 'G#': 'B', 'A': '0', 'B': '2',
     'C': '3', 'D': '5', 'E': '7', 'F': '8', 'F#': '9', 'G': 'A'}
def solution(m, musicinfos):
    musics = {}
    e_m = encode_m(m)
    for musicinfo in musicinfos:
        s, e, title, a = musicinfo.split(',')
        ea = encode_m(a)
        sM, sm = map(int, s.split(':'))
        eM, em = map(int, e.split(':'))
        t = (eM - sM) * 60 + em - sm
        musics[title] = ea * (t // len(ea)) + ea[:t % len(ea)]
    for title, mm in musics.items():
        if e_m in mm:
            return title
    return '(None)'

def encode_m(m):
    for char, i in A.items():
        m = m.replace(char, i)
    return m

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))