class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        bag = dict()
        zeroCount = 0
        l, r = 0, 0
        for c in s1:
            bag[c] = bag.get(c, 0) + 1
        
        uniqChars = len(bag.keys())
        while r < len(s2):
            if r - l + 1 > len(s1):
                if s2[l] in bag:
                    if bag[s2[l]] == 0:
                        zeroCount -= 1
                    bag[s2[l]] += 1
                l += 1
            
            if s2[r] in bag:
                bag[s2[r]] -= 1
                if bag[s2[r]] == 0:
                    zeroCount += 1
            if zeroCount == uniqChars:
                return True
            r += 1
        return False