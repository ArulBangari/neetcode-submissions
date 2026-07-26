class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_arr = [set() for _ in range(9)]
        col_arr = [set() for _ in range(9)]
        square_arr = [set() for _ in range(9)]
        row = 0
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = board[row][col]
                    square_ind = row // 3 + (col // 3) * 3
                    if num in row_arr[row] or num in col_arr[col] or num in square_arr[square_ind]:
                        return False
                    row_arr[row].add(num)
                    col_arr[col].add(num)
                    square_arr[square_ind].add(num)
        return True
                        