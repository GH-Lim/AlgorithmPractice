from collections import deque
N, A, B = map(int, input().split())

ori = deque([A])
yukri = deque([B])
y = 0
while ori and yukri:
    y += 1
    temp = set()
    for _ in range(len(ori)):
        a = ori.popleft()
        nap, nam = a + 2 ** (y - 1), a - 2 ** (y - 1)
        if nap <= N and nap not in temp:
            temp.add(nap)
            ori.append(nap)
        if nam > 0 and nam not in temp:
            temp.add(nam)
            ori.append(nam)
    temp2 = set()
    for _ in range(len(yukri)):
        a = yukri.popleft()
        nap, nam = a + 2 ** (y - 1), a - 2 ** (y - 1)
        if nap in temp or nam in temp:
            break
        if nap <= N and nap not in temp2:
            temp2.add(nap)
            yukri.append(nap)
        if nam > 0 and nam not in temp2:
            temp2.add(nam)
            yukri.append(nam)
    else: continue
    break
else: y = -1
print(y)
