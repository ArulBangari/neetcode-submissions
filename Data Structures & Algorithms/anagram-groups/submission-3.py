class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for string in strs:
            arr = [0 for _ in range(26)]
            for char in string:
                arr[ord(char) - ord('a')] += 1
            anagram_dict.setdefault(tuple(arr), []).append(string)
        return anagram_dict.values()