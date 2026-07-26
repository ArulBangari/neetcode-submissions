class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adjList[word[:i] + '*' + word[i + 1:]].append(word)
        

        q = collections.deque()
        q.append(beginWord)
        visited = set(beginWord)
        step = 0
        while q:
            step += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    wild = word[:i] + '*' + word[i + 1:]
                    for child in adjList[wild]:
                        if child not in visited:
                            q.append(child)
                            visited.add(child)
        return 0