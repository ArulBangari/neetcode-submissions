class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternToWord = defaultdict(list)
        wordToPattern = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                patternToWord[pattern].append(word)
                wordToPattern[word].append(pattern)

        q = collections.deque()
        q.append(beginWord)
        visited = set([beginWord])
        step = 0
        while q:
            step += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return step
                print(word)
                print(wordToPattern[word])
                for pattern in wordToPattern[word]:
                    print(pattern)
                    for child in patternToWord[pattern]:
                        if child not in visited:
                            q.append(child)
                            visited.add(child)
        return 0