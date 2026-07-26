class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = defaultdict(list)

        for string in strs:
            frequency_array = [0 for _ in range(26)]

            for char in string:
                frequency_array[ord(char) - ord("a")] += 1

            string_dict[tuple(frequency_array)].append(string)
        
        return list(string_dict.values())