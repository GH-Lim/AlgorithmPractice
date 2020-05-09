class Node(object):
    def __init__(self, data):
        self.key = data[0]
        self.val = data[1]
        self.gems = {self.val: 1}
        self.length = 1
        self.find_min = False


def solution(gems):
    min_gems = len(set(gems))
    nodes = []
    answer_len = 1000000
    answer_idx = 0
    for data in enumerate(gems):
        nodes.append(Node(data))
    for idx, node in enumerate(nodes):
        if node.length >= answer_len:
            continue
        for i in range(idx):
            if not nodes[i].find_min:
                nodes[i].gems[node.val] = 1
                nodes[i].length += 1
                if len(nodes[i].gems) == min_gems:
                    if answer_len > nodes[i].length:
                        answer_len = nodes[i].length
                        answer_idx = i

                    nodes[i].find_min = True

    return [answer_idx + 1, answer_idx + answer_len]


print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
