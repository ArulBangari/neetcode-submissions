class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = [0] * len(height)
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        while l <= r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] < height[r]:
                trapped[l] = min(maxLeft, maxRight) - height[l]
                l += 1
            else:
                trapped[r] = min(maxLeft, maxRight) - height[r]
                r -= 1
        return sum(trapped)