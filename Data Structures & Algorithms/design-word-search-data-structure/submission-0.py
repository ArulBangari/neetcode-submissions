class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        def backtrack(cur, i):
            if i == len(word):
                return cur.endOfWord
            if word[i] == '.':
                check = False
                for child in cur.children:
                    check = check or backtrack(cur.children[child], i + 1)
                return check
            else:
                if word[i] not in cur.children:
                    return False
                else:
                    return backtrack(cur.children[word[i]], i + 1)
        return backtrack(cur, 0)