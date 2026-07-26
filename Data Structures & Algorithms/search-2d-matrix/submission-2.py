class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = self.findArray(matrix, target, 0, len(matrix) - 1)
        if not arr:
            return False
        return self.findNumber(arr, target, 0, len(arr) - 1)
    
    def findArray(self, matrix, target, l, r):
        m = l + (r - l) // 2
        if l == m:
            if matrix[m][0] > target:
                return False
        if r == m:
            if matrix[m][len(matrix[m]) - 1] < target:
                return False

        if matrix[m][0] > target:
            return self.findArray(matrix, target, l, m - 1)
        if matrix[m][len(matrix[m]) - 1] < target:
            return self.findArray(matrix, target, m + 1, r)
        return matrix[m]
    
    def findNumber(self, arr, target, l, r):
        m = l + (r - l) // 2
        if l > r:
            return False

        if arr[m] > target:
            return self.findNumber(arr, target, l, m - 1)
        elif arr[m] < target:
            return self.findNumber(arr, target, m + 1, r)
        else:
            return True