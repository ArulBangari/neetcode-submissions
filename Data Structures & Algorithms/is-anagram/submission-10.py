class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphDict = defaultdict(int)
        for i in range(len(s)):
            alphDict[s[i]] += 1
            alphDict[t[i]] -= 1
        
        for (_, value) in alphDict.items():
            if value != 0:
                return False
        return True