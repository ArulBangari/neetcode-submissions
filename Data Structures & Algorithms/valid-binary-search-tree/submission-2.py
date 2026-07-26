# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, float("infinity"), float("-infinity"))
            left = dfs(node.left)
            right = dfs(node.right)
            print(left, right, node.val)
            if not left[0] or not right[0]:
                return (False, 0, 0)
            return (left[2] < node.val and right[1] > node.val, min(left[1], node.val), max(right[2], node.val))
        return dfs(root)[0]