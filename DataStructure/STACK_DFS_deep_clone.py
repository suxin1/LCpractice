from typing import List
from collections import deque

class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


# recursive
def clone_graph(root):
    if not root:
        return None
    mem = dict()

    def recursive(node):
        if node.val in mem:
            return mem[node.val]

        new_node = Node(val=node.val, neighbors=[])
        mem[node.val] = new_node

        neighbors = []
        for n in node.neighbors:
            neighbors.append(recursive(n))
        new_node.neighbors = neighbors

        return new_node

    return recursive(root)

# stack
def clone_graph_stack(node):
    mem = dict()
    new_node = Node(val=node.val, neighbors=[])
    queue = deque([node])

    while queue:
        cur = queue.pop()


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
graph_clone = clone_graph(graph_res)