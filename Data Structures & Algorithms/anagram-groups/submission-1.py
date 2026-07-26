class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_char_counts = {}
        group_anagrams = []
        count = 0
        for word in strs:
            char_counts = [0]*26
            for char in word:
                char_counts[ord(char) - ord("a")] += 1
            char_counts = tuple(char_counts)
            if char_counts in word_char_counts:
                word_char_counts[char_counts].append(word)
            else:
                word_char_counts[char_counts] = [word]
        return list(word_char_counts.values())