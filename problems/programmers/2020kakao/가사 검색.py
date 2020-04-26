class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.trailing_len = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur_node = self.head
        word_len = len(word)
        try:
            cur_node.trailing_len[word_len] += 1
        except:
            cur_node.trailing_len[word_len] = 1
        for char in word:
            try:
                cur_node.children[char]
            except:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
            word_len -= 1

            try:
                cur_node.trailing_len[word_len] += 1
            except:
                cur_node.trailing_len[word_len] = 1

    def find(self, querie):
        cur_node = self.head
        querie_len = len(querie)
        querie_strip = querie.strip("?")
        wildcard = querie_len - len(querie_strip)
        if querie_len not in cur_node.trailing_len:
            return 0
        if wildcard == 0:
            return cur_node.trailing_len[querie_len]
        for char in querie_strip:
            try:
                cur_node = cur_node.children[char]
            except:
                return 0
        return cur_node.trailing_len[wildcard]


def solution(words, queries):
    answer = []
    trie = Trie()
    rev_trie = Trie()

    for word in words:
        trie.insert(word)
        rev_trie.insert(word[::-1])

    for querie in queries:
        if querie[0] == '?':
            answer.append(rev_trie.find(querie[::-1]))
        else:
            answer.append(trie.find(querie))
    return answer

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

w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q = ["fro??", "????o", "fr???", "fro???", "pro?", "??????"]

print(solution(w, q))