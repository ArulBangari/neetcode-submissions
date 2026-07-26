class Solution:
    def trap(self, height: List[int]) -> int:
        totalTrappedWater = 0
        l, r = 0 , len(height) - 1
        maxLHeight, maxRHeight = 0, 0
        while l < r:
            maxLHeight = max(height[l], maxLHeight)
            maxRHeight = max(height[r], maxRHeight)
            if height[l] >= height[r]:
                totalTrappedWater += min(maxLHeight, maxRHeight) - height[r]
                r -= 1
            else:
                totalTrappedWater += min(maxLHeight, maxRHeight) - height[l]
                l += 1
        return totalTrappedWater