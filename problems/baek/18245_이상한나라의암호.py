cnt = 2
while True:
    pw = input()
    if pw == 'Was it a cat I saw?':
        break
    for i in range(0, len(pw), cnt):
        print(pw[i], end='')
    cnt += 1
    print()
