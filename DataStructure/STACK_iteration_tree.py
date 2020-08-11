from typing import List


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# 前序递归（中，左，右）
def preorder_iteration(root):
    result = list()
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            result.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)

    return result

# 中序递归（左，中，右）
def midorder_iteration(root):
    result = list()
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result


def tree_factory(tree: List):
    """
    a tree is like [[1, 2, 3], [2, 4, 5]
    :param tree:
    :return:
    """
    memo = dict()

    for node in tree:
        memo[node[0]] = Node(node[0])

    for node in tree:
        try:
            memo[node[0]].left = memo[node[1]]
        except:
            pass
        try:
            memo[node[0]].right = memo[node[2]]
        except:
            pass

    return memo[tree[0][0]]


list_tree = [[1, 2, 3], [2, 4, 5], [3, 6, 7], [4], [5], [6], [7]]
root = tree_factory(list_tree)

print(midorder_iteration(root))
