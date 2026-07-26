# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            q1, q2 = collections.deque(), collections.deque()
            q1.append(root1)
            q2.append(root2)
            while q1 and q2:
                node1 = q1.popleft()
                node2 = q2.popleft()
                if node1 is None and node2 is None:
                    continue
                if node1 is None or node2 is None or node1.val != node2.val:
                    return False
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            return q1 == q2
        
        def recursion(root1):
            if root1 is None: return False
            nonlocal subRoot
            if sameTree(root1, subRoot):
                return True
            return recursion(root1.left) or recursion(root1.right)
        return recursion(root)
