class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        inDeg = {}
        for word in words:
            for char in word:
                graph[char]
                inDeg[char] = 0
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            small = min(len(word1), len(word2))
            for j in range(small):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        inDeg[word2[j]] += 1
                    break
                if j == small - 1 and len(word1) > len(word2):
                    return ""
        print(graph)
    
        q = collections.deque()
        for i in inDeg:
            if inDeg[i] == 0:
                q.append(i)
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for dst in graph[char]:
                inDeg[dst] -= 1
                if inDeg[dst] == 0:
                    q.append(dst)
        return "".join(res) if len(res) == len(graph) else ""