N = int(input())
f = list(input())

ans = -987654321


def calc(l, k):
    global ans
    if len(l) == 1:
        ans = max(ans, int(l[0]))
        return
    sub_l = l[:]
    sub_l[0:3] = [int(sub_l[0]) + int(sub_l[2])] if sub_l[1] == '+' else [int(sub_l[0]) * int(sub_l[2])] if sub_l[1] == '*' else [int(sub_l[0]) - int(sub_l[2])]
    calc(sub_l, True)
    if k and len(l) > 4:
        sub_l = l[:]
        sub_l[2:5] = [int(sub_l[2]) + int(sub_l[4])] if sub_l[3] == '+' else [int(sub_l[2]) * int(sub_l[4])] if sub_l[3] == '*' else [int(sub_l[2]) - int(sub_l[4])]
        calc(sub_l, False)


calc(f, True)
print(ans)
