# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        level = 0
        while q:
            qLen = len(q)
            check = False
            for i in range(qLen):
                node = q.popleft()
                if node:
                    check = True
                    q.append(node.left)
                    q.append(node.right)
            if check:
                level += 1
        return level