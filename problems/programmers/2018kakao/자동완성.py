class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.children = {}
        self.data = data
        self.trailing_word = 0


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            cur_node.trailing_word += 1
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        cur_node.data = string

    def search(self, string):
        cur_node = self.head
        for i in range(len(string)):
            if string[i] in cur_node.children:
                cur_node = cur_node.children[string[i]]
                if not cur_node.data and cur_node.trailing_word == 1:
                    return i + 1
        if cur_node.data:
            return len(string)


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)
    return answer
