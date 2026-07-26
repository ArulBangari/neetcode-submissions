class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k:
            num = -heapq.heappop(nums) if nums else -1
            k -= 1
        return num