class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        
        for r in range(rows):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][cols - 1] == "O":
                q.append((r, cols - 1))
        
        for c in range(cols):
            if board[0][c] == "O":
                q.append((0, c))
            if board[rows - 1][c] == "O":
                q.append((rows - 1, c))

        while q:
            i, j = q.popleft()
            visited.add((i, j))
            for di, dj in directions:
                x, y = i + di, j + dj
                if (0 <= x < rows and 0 <= y < cols and
                    (x, y) not in visited and board[x][y] == "O"):
                    q.append((x, y))
                    
        for r in range(1 , rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"