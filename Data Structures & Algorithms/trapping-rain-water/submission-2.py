class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = [0 for _ in range(len(height))]
        l, r = 0 , len(height) - 1
        maxLHeight, maxRHeight = 0, 0
        while l < r:
            maxLHeight = max(height[l], maxLHeight)
            maxRHeight = max(height[r], maxRHeight)
            if height[l] >= height[r]:
                trappedWater[r] = min(maxLHeight, maxRHeight) - height[r]
                r -= 1
            else:
                trappedWater[l] = min(maxLHeight, maxRHeight) - height[l]
                l += 1
        return sum(trappedWater)