# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(node, maxVal):
            maxVal = max(maxVal, node.val)
            if maxVal == node.val:
                self.good += 1

            if node.left:
                dfs(node.left, maxVal)
            if node.right:
                dfs(node.right, maxVal)
        dfs(root, float("-infinity"))
        return self.good