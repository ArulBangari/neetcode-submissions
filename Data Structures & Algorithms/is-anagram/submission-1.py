class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_table = {}
        for char in s:
            if char not in char_table:
                char_table[char] = 1
            else:
                char_table[char] += 1
        for char in t:
            if char in char_table:
                char_table[char] -= 1
            else:
                return False
        for val in char_table.values():
            if val != 0:
                return False
        return True