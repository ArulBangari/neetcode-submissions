class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        sequence_beginning = []
        for num in nums:
            if num - 1 not in hash_set:
                sequence_beginning.append(num)
        
        max_sequence_length = 0
        for num in sequence_beginning:
            temp_sequence_length = 0
            while num in hash_set:
                temp_sequence_length += 1
                num = num + 1
            if max_sequence_length < temp_sequence_length:
                max_sequence_length = temp_sequence_length
        
        return max_sequence_length