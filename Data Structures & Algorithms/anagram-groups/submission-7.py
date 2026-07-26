class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)
        for word in strs:
            letCount = [0] * 26
            for c in word:
                letCount[ord(c) - ord('a')] += 1
            anaDict[tuple(letCount)].append(word)
        return list(anaDict.values())