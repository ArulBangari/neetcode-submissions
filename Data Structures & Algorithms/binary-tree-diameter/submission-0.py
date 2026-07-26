# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursion(self, root):
        if not root:
            return (0, 0)
        
        rightH, rightD = self.recursion(root.right)
        leftH, leftD = self.recursion(root.left)
        maxD = max(leftD, rightD, leftH + rightH)
        return (max(leftH + 1, rightH + 1), maxD)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)[1]        