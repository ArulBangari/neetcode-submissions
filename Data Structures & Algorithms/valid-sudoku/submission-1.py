class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        box_set = [set() for x in range(9)]
        col_set = [set() for x in range(9)]
        row_index = 0
        while row_index < 9:
            col_index = 0
            row_set = set()
            while col_index < 9:
                num = board[row_index][col_index]
                if num != ".":
                    num = int(num)

                    if num in row_set:
                        return False
                    else:
                        row_set.add(num)
                    
                    if num in col_set[col_index]:
                        return False
                    else:
                        col_set[col_index].add(num)
                    
                    box_index = math.floor(row_index / 3) * 3 + math.floor(col_index / 3)
                    if num in box_set[box_index]:
                        return False
                    else:
                        box_set[box_index].add(num)
                col_index += 1
            row_index += 1
        return True