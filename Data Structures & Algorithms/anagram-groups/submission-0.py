class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = {}
        group_anagrams = []
        count = 0
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in sorted_anagrams:
                sorted_anagrams[sorted_word] = count
                group_anagrams.append([word])
                count += 1
            else:
                group_anagrams[sorted_anagrams[sorted_word]].append(word)
        return group_anagrams