class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_char_counts = defaultdict(list)
        group_anagrams = []
        count = 0
        for word in strs:
            char_counts = [0]*26
            for char in word:
                char_counts[ord(char) - ord("a")] += 1
            word_char_counts[tuple(char_counts)].append(word)
        return list(word_char_counts.values())