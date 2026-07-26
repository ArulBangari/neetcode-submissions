"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {None: None}
        def populate(node):
            if not node:
                return
            oldToNew[node] = Node(node.val)
            for n in node.neighbors:
                if n not in oldToNew:
                    populate(n)
        populate(node)

        visited = set()
        def connect(node):
            if not node:
                return
            visited.add(node)
            for n in node.neighbors:
                oldToNew[node].neighbors.append(oldToNew[n])
                if n not in visited:
                    connect(n)
        connect(node)
        return oldToNew[node]