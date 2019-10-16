N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0  # 0으로 초기화
for i in range(N):
    same = 1  # 같은 높이인 바닥 수 카운트
    j = 1
    while j < N:  # 바로 앞 칸과 비교를 해야하므로 index 1부터 시작
        if arr[i][j - 1] == arr[i][j]:  # 높이가 같으면 same + 1
            same += 1
        elif arr[i][j - 1] - arr[i][j] == -1:  # 높이가 1 높으면
            if same < L:
                break  # L 보다 짧다면 break
            else:
                same = 1  # 초기화

        elif arr[i][j - 1] - arr[i][j] == 1:  # 높이가 1 낮다면

            for k in range(1, L):  # 다음 L 만큼이 높이가 같아야 함

                if j + k > N - 1:  # 범위를 벗어나거나
                    break
                elif arr[i][j] != arr[i][j + k]:  # 높이가 달라진다면 브레이크
                    break

            else:  # L 만큼 범위 돌면서 break 를 만나지 않았다면
                j += L  # 다음 L 만큼 높이가 같았으므로 L 만큼 이동
                same = 0  # 초기화 / 내려왔을 땐 0으로 해줌
                continue  # 다음 while 로 이동

            break  # L 만큼 범위 돌면서 break 를 만나서 빠져나왔다면 한번 더 break

        else:  # 높이 차가 2 이상이라면 break
            break
        j += 1
    else:  # j 가 N 까지 무사히 도착했다면 ans + 1
        ans += 1


for j in range(N):  # 세로로 시작
    same = 1
    i = 1
    while i < N:
        if arr[i - 1][j] == arr[i][j]:
            same += 1
        elif arr[i - 1][j] - arr[i][j] == -1:
            if same < L:
                break
            else:
                same = 1
        elif arr[i - 1][j] - arr[i][j] == 1:
            for k in range(1, L):
                if i + k > N - 1:
                    break
                elif arr[i][j] != arr[i + k][j]:
                    break
            else:
                i += L
                same = 0
                continue
            break
        else:
            break
        i += 1
    else:
        ans += 1

print(ans)
