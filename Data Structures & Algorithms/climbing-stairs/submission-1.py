class Solution:
    def climbStairs(self, n: int) -> int:
        x = [0] * (n + 1)
        x[n], x[n - 1] = 1, 1
        for i in range(n - 2, -1, -1):
            x[i] = x[i + 1] + x[i + 2]
        return x[0]