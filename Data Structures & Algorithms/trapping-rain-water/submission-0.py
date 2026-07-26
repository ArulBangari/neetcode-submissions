class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_maximum = [0 for _ in range(len(height))]
        suffix_maximum = [0 for _ in range(len(height))]
        water = [0 for _ in range(len(height))]

        for index in range(1, len(height)):
            prefix_maximum[index] = max(prefix_maximum[index - 1], height[index - 1])

        for index in range(len(height) - 2, -1, -1):
            suffix_maximum[index] = max(suffix_maximum[index + 1], height[index + 1])
        
        for index in range(0, len(height)):
            water[index] = max(min(suffix_maximum[index], prefix_maximum[index]) - height[index] , 0)

        return sum(water)