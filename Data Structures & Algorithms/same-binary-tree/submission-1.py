# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = collections.deque(), collections.deque()
        q1.append(p)
        q2.append(q)
        while q1 or q2:
            if (not q1) ^ (not q2):
                return False
            node1, node2 = q1.popleft(), q2.popleft()
            if (not node1) ^ (not node2):
                return False
            if node1 == node2:
                continue
            if node1.val != node2.val:
                return False
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
        return True