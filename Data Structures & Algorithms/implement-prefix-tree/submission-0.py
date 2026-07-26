class TreeNode:
    def __init__(self, val=None):
        self.children = {}
        self.val = val

class PrefixTree:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.val = word
        x = []

    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.val == word

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True