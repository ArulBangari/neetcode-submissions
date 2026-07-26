class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index_dict = defaultdict(int)
        frequency_array = [set() for _ in range(len(nums))]
        for num in nums:
            index_dict[num] += 1
        
        for num in index_dict:
            frequency_array[index_dict[num] - 1].add(num)
        
        return_array = []
        num_count = 0
        i = len(frequency_array) - 1

        while num_count < k:
            num_count += len(frequency_array[i])
            return_array = return_array +  list(frequency_array[i])
            i -= 1
        return return_array
