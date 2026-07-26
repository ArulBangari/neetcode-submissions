class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = defaultdict(int)
        t_char = defaultdict(int)
        for char in s:
            s_char[char] += 1
        for char in t:
            t_char[char] += 1
        
        return s_char==t_char