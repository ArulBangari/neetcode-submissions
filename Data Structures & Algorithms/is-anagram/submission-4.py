class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted
        char_table = {}
        for char in s:
            char_table[char] = 1 + char_table.get(char, 0)
        for char in t:
            char_table[char] = char_table.get(char, 0) - 1
        for val in char_table.values():
            if val != 0:
                return False
        return True