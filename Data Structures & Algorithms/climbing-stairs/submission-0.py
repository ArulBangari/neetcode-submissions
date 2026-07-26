class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 0
        while n:
            one, two = one + two, one
            n -= 1
        return one