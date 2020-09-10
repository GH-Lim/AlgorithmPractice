# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

N = int(input())

HR_max = 220 - N
train = [0, 0, 0, 0, 0, 0]
for line in sys.stdin:
    if line.strip():
        HR = int(line.strip()) / HR_max
        if HR >= 0.9:
            train[0] += 1
        elif HR >= 0.8:
            train[1] += 1
        elif HR >= 0.75:
            train[2] += 1
        elif HR >= 0.68:
            train[3] += 1
        elif HR >= 0.6:
            train[4] += 1
        else:
            train[5] += 1
    else: break
print(' '.join(map(str, train)))
