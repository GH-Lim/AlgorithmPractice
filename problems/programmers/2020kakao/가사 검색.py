# # 효율성 테스트 1, 2, 3 실패
# def solution(words, queries):
#     answer = []
#     for q in queries:
#         r_or_l = 0
#         if q[0] == '?':
#             sub_q = q.lstrip('?')
#         else:
#             sub_q = q.rstrip('?')
#             r_or_l = 1
#         cnt = 0
#         for w in words:
#             if len(w) != len(q):
#                 continue
#             if r_or_l:
#                 if w[:len(sub_q)] == sub_q:
#                     cnt += 1
#             else:
#                 if w[-len(sub_q):] == sub_q:
#                     cnt += 1
#         answer.append(cnt)
#
#     return answer

