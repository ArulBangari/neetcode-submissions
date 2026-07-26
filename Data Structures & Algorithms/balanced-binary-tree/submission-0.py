# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check = True
        def dfs(curr):
            if not curr:
                return 0
            
            lHeight = dfs(curr.left)
            rHeight = dfs(curr.right)
            if abs(lHeight - rHeight) > 1:
                self.check = False
            return max(lHeight + 1, rHeight + 1)
        dfs(root)
        return self.check