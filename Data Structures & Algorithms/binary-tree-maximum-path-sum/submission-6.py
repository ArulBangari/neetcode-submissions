# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float("-infinity")
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            path = left + right + node.val
            self.maxPath = max(self.maxPath, path)
            return max(max(left, right) + node.val, 0)
        dfs(root)
        return self.maxPath