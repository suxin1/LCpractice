"""
无向图深拷贝
"""

from collections import deque


class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


# 递归(调用栈 LIFO) recursive
def clone_graph(root):
    if not root:
        return None
    mem = dict()

    def recursive(node):
        if node.val in mem:
            return mem[node.val]

        new_node = Node(val=node.val, neighbors=[])
        mem[node.val] = new_node

        if node.neighbors:
            new_node.neighbors = [recursive(n) for n in node.neighbors]

        return new_node

    return recursive(root)


# 使用广度优先搜索 (BFS)
def clone_graph_stack(node):
    if not node:
        return node

    mem = dict()
    mem[node] = Node(val=node.val, neighbors=[])
    queue = deque([node])

    while queue:
        cur = queue.popleft()
        for n in cur.neighbors:
            if n not in mem:
                mem[n] = Node(val=n.val, neighbors=[])
                queue.append(n)
            mem[cur].neighbors.append(mem[n])

    return mem[node]


graph = [[2,4],[1,3],[2,4],[1,3]]
def list_graph(list):
    mem = dict()

    for node in range(len(list)):
        mem[node+1] = Node(val=node+1, neighbors=[])

    for i in range(len(list)):
        for n in list[i]:
            mem[i+1].neighbors.append(mem[n])

    return mem[1]


graph_res = list_graph(graph)
graph_clone = clone_graph_stack(graph_res)
