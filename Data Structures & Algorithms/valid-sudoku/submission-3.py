class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_array = [set() for _ in range(9)]
        column_array = [set() for _ in range(9)]
        sub_box_array = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                n = board[i][j]
                if n == ".":
                    print(n)
                    continue
                n = int(n)
                if n in row_array[i] or n in column_array[j] or n in sub_box_array[3*(i//3) + j//3]:
                    return False
                row_array[i].add(n)
                column_array[j].add(n)
                sub_box_array[3*(i//3) + j//3].add(n)
        return True