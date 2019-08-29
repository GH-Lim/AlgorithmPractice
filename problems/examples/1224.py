def turn(idx):
    if s_list[idx] == 1:
        s_list[idx] = 0
    elif s_list[idx] == 0:
        s_list[idx] = 1


# s_list = [1, 0, 1]

# turn(1)
# print(s_list)
switch = int(input())
s_list = list(map(int, input().split()))
s_list.insert(0, 9)  # 가장 앞에 의미없는 값인 9를 삽입하여 idx맞춰주기
s_list.append(9)
people = int(input())

for p in range(people):
    gender, card_num = map(int, input().split())

    if gender == 1:
        i = 1
        while card_num * i < switch + 1:
            turn(card_num*i)
            i += 1
        print(s_list)

    if gender == 2:
        turn(card_num)

        i = 1
        while s_list[card_num - i] == s_list[card_num + i]:
            # print(card_num -i, card_num + i)
            turn(card_num - i)
            turn(card_num + i)
            i += 1
            if card_num - i >= 1 and card_num + i < switch + 1:
                continue
            else:
                break
s_list.pop(0)
s_list.pop()
for s in range(len(s_list)):
    print(s_list[s], end=' ')
    if (s + 1) % 20 == 0:
        print('')