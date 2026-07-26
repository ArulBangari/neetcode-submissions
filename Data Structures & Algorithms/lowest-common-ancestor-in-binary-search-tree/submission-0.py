# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, p, q):
        if root is None:
            return [None, False]
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if left[0] is not None:
            return [left[0], True]
        if right[0] is not None:
            return [right[0], True]
        
        if root.val == p.val or root.val == q.val:
            if left[1] or right[1]:
                return [root, False]
            return [None, True]
        if left[1] == right[1] == True:
            return [root, False]
        return [None, left[1] or right[1]]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root, p, q)[0]