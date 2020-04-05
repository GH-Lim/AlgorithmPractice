def solution(answer_sheet, sheets):
    ans_len = len(answer_sheet)
    length = len(sheets)
    answer = 0
    for i in range(length):

        for j in range(length):
            if i == j: continue
            cheats = 0
            max_len = 0
            temp_len = 0
            for a in range(ans_len):
                if sheets[i][a] != answer_sheet[a] and sheets[i][a] == sheets[j][a]:
                    temp_len += 1
                    cheats += 1
                else:  # sheets[i][a] == answer_sheet[a]:
                    max_len = max(max_len, temp_len)
                    temp_len = 0
            max_len = max(max_len, temp_len)
            answer = max(answer, cheats + max_len ** 2)

    return answer


a = "24551"
b = ["24553", "24553", "24553", "24553"]

print(solution(a, b))