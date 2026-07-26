class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = {
            "rows": [set() for _ in range(9)],
            "cols": [set() for _ in range(9)],
            "sub": [set() for _ in range(9)]
        }

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                
                sub = 3 * (row // 3) + col // 3
                if cell in sets["rows"][row] or cell in sets["cols"][col] or cell in sets["sub"][sub]:
                    return False
                
                sets["rows"][row].add(cell)
                sets["cols"][col].add(cell)
                sets["sub"][sub].add(cell)
        return True