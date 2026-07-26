class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        notZeroCount, alphDict = 0, defaultdict(int)
        for i in range(len(s)):
            if alphDict[s[i]] == 0:
                notZeroCount += 1
            alphDict[s[i]] += 1
            if alphDict[s[i]] == 0:
                notZeroCount -= 1
            
            if alphDict[t[i]] == 0:
                notZeroCount += 1
            alphDict[t[i]] -= 1
            if alphDict[t[i]] == 0:
                notZeroCount -= 1
        print(alphDict)
        return notZeroCount == 0