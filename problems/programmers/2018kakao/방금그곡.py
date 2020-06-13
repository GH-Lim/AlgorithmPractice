A = {'A': '0', 'A#': '1', 'B': '2', 'C': '3', 'C#': '4', 'D': '5',
     'D#': '6', 'E': '7', 'F': '8', 'F#': '9', 'G': 'A', 'G#': 'B'}
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
    i = 0
    encoded = ''
    while i < len(m):
        if m[i: i + 2] in ['A#', 'C#', 'D#']:
            encoded += str(A[m[i:i+2]])
            i += 2
        else:
            encoded += str(A[m[i:i+1]])
            i += 1
    return encoded
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))