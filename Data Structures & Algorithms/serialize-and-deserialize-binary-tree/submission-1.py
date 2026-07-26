# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if not node:
                    arr.append(None)
                else:
                    arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        return "/".join(str(x) for x in arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        sq = collections.deque(data.split("/"))
        if sq[0] == 'None': return None
        q = collections.deque()
        head = TreeNode(int(sq.popleft()))
        q.append(head)
        while q and sq:
            node = q.popleft()
            if node:
                left, right = sq.popleft(), sq.popleft()
                if left != 'None':
                    node.left = TreeNode(int(left))
                    q.append(node.left)
                if right != 'None':
                    node.right = TreeNode(int(right))
                    q.append(node.right)
        return head
