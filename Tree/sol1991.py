import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#전위 순회 //루트-왼-오
def pre_order(node):
    print(node.data, end='')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

#중위 순회 // 왼-루트-오
def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != None:
        in_order(tree[node.right])

#후위 순회 // 왼-오-루트
def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end='')

N = int(sys.stdin.readline().rstrip())
tree = {}

for i in range(N):
    data, left, right = sys.stdin.readline().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])