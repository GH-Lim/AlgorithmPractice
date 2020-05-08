import sys
sys.setrecursionlimit(10000)


class Node(object):
    def __init__(self, data):
        self.key = data[0] + 1
        self.x = data[1][0]
        self.y = data[1][1]
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.pre_order_list = []
        self.post_order_list = []

    def insert(self, node):
        if self.root is None:
            self.root = node
            return
        cur_node = self.root
        insert_node = node
        while True:
            if cur_node.left and insert_node.x < cur_node.x:
                cur_node = cur_node.left
            elif cur_node.right and insert_node.x > cur_node.x:
                cur_node = cur_node.right
            else:
                if insert_node.x < cur_node.x:
                    cur_node.left = insert_node
                elif insert_node.x > cur_node.x:
                    cur_node.right = insert_node
                break

    def preorder(self, node):
        self.pre_order_list.append(node.key)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        self.post_order_list.append(node.key)


def solution(nodeinfo):
    answer = []
    nodes = sorted(enumerate(nodeinfo), key=lambda x: (-x[1][1], x[1][0]))
    bst = BinarySearchTree()
    for node in nodes:
        bst.insert(Node(node))
    bst.preorder(bst.root)
    bst.postorder(bst.root)
    answer.append(bst.pre_order_list)
    answer.append(bst.post_order_list)
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))