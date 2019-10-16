def cubing(f, w):
    if f == 'U':
        a = faces[F][0]
        b = faces[R][0]
        c = faces[B][0]
        d = faces[L][0]
        if w == '+':
            faces[F][0], faces[R][0], faces[B][0], faces[L][0] = b, c, d, a
        else:
            faces[F][0], faces[R][0], faces[B][0], faces[L][0] = d, a, b, c
    elif f == 'D':
        a = faces[F][2]
        b = faces[R][2]
        c = faces[B][2]
        d = faces[L][2]
        if w == '+':
            faces[F][2], faces[R][2], faces[B][2], faces[L][2] = d, a, b, c
        else:
            faces[F][2], faces[R][2], faces[B][2], faces[L][2] = b, c, d, a
    elif f == 'F':
        a = faces[U][2]
        b = [faces[R][0][0], faces[R][1][0], faces[R][2][0]]
        c = faces[D][0]
        d = [faces[L][0][2], faces[L][1][2], faces[L][2][2]]
        if w == '+':
            faces[U][2] = d[2::-1]
            faces[R][0][0], faces[R][1][0], faces[R][2][0] = a
            faces[D][0] = b[2::-1]
            faces[L][0][2], faces[L][1][2], faces[L][2][2] = c
        else:
            faces[U][2] = b
            faces[R][0][0], faces[R][1][0], faces[R][2][0] = c[2::-1]
            faces[D][0] = d
            faces[L][0][2], faces[L][1][2], faces[L][2][2] = a[2::-1]
    elif f == 'B':
        a = faces[U][0]
        b = [faces[R][0][2], faces[R][1][2], faces[R][2][2]]
        c = faces[D][2]
        d = [faces[L][0][0], faces[L][1][0], faces[L][2][0]]
        if w == '+':
            faces[U][0] = b
            faces[R][0][2], faces[R][1][2], faces[R][2][2] = c[2::-1]
            faces[D][2] = d
            faces[L][0][0], faces[L][1][0], faces[L][2][0] = a[2::-1]
        else:
            faces[U][0] = d[2::-1]
            faces[R][0][2], faces[R][1][2], faces[R][2][2] = a
            faces[D][2] = b[2::-1]
            faces[L][0][0], faces[L][1][0], faces[L][2][0] = c
    elif f == 'L':
        a = [faces[U][2][0], faces[U][1][0], faces[U][0][0]]
        b = [faces[F][2][0], faces[F][1][0], faces[F][0][0]]
        c = [faces[D][2][0], faces[D][1][0], faces[D][0][0]]
        d = [faces[B][2][2], faces[B][1][2], faces[B][0][2]]
        if w == '+':
            faces[U][0][0], faces[U][1][0], faces[U][2][0] = d
            faces[F][2][0], faces[F][1][0], faces[F][0][0] = a
            faces[D][2][0], faces[D][1][0], faces[D][0][0] = b
            faces[B][0][2], faces[B][1][2], faces[B][2][2] = c
        else:
            faces[U][2][0], faces[U][1][0], faces[U][0][0] = b
            faces[F][2][0], faces[F][1][0], faces[F][0][0] = c
            faces[D][0][0], faces[D][1][0], faces[D][2][0] = d
            faces[B][0][2], faces[B][1][2], faces[B][2][2] = a
    elif f == 'R':
        a = [faces[U][2][2], faces[U][1][2], faces[U][0][2]]
        b = [faces[F][2][2], faces[F][1][2], faces[F][0][2]]
        c = [faces[D][2][2], faces[D][1][2], faces[D][0][2]]
        d = [faces[B][2][0], faces[B][1][0], faces[B][0][0]]
        if w == '+':
            faces[U][2][2], faces[U][1][2], faces[U][0][2] = b
            faces[F][2][2], faces[F][1][2], faces[F][0][2] = c
            faces[D][0][2], faces[D][1][2], faces[D][2][2] = d
            faces[B][0][0], faces[B][1][0], faces[B][2][0] = a
        else:
            faces[U][0][2], faces[U][1][2], faces[U][2][2] = d
            faces[F][2][2], faces[F][1][2], faces[F][0][2] = a
            faces[D][2][2], faces[D][1][2], faces[D][0][2] = b
            faces[B][0][0], faces[B][1][0], faces[B][2][0] = c


U, D, F, B, L, R = 0, 1, 2, 3, 4, 5
for tc in range(1, int(input()) + 1):
    n = int(input())
    commands = input().split()
    faces = [
        [['w'] * 3 for _ in range(3)],  # U w
        [['y'] * 3 for _ in range(3)],  # D y
        [['r'] * 3 for _ in range(3)],  # F r
        [['o'] * 3 for _ in range(3)],  # B o
        [['g'] * 3 for _ in range(3)],  # L g
        [['b'] * 3 for _ in range(3)],  # R b
    ]
    for command in commands:
        face, wise = command  # 면, 방향
        cubing(face, wise)
    for i in range(3):
        for f in range(6):
            print(faces[f][i], end='  ')
        print()
