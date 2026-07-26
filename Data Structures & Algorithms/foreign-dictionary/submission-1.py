class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {char: [] for word in words for char in word}
        inDegree = defaultdict(int)
        s = set(adjList.keys())
        l = []

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""
            for c in range(minLen):
                if w1[c] != w2[c]:
                    s.discard(w2[c])
                    inDegree[w2[c]] += 1
                    adjList[w1[c]].append(w2[c])
                    break
        s = list(s)
        print(adjList)
        while s:
            n = s.pop()
            l.append(n)
            while adjList[n]:
                m = adjList[n].pop()
                print(adjList)
                inDegree[m] -= 1
                if inDegree[m] == 0:
                    s.append(m)
            del adjList[n]
        
        l = "".join(l)
        if adjList:
            return ""
        return l