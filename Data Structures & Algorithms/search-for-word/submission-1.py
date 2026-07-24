class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if (row < 0 or col < 0 or
                row >= len(board) or col >= len(board[0]) or
                board[row][col] != word[idx] or
                (row, col) in path):
                return False
            
            path.add((row, col))
            
            result = (dfs(row + 1, col, idx + 1) or
                      dfs(row - 1, col, idx + 1) or
                      dfs(row, col + 1, idx + 1) or
                      dfs(row, col - 1, idx + 1))
            
            path.remove((row, col))

            return result
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != word[0]:
                    continue
                if dfs(r, c, 0):
                    return True
        return False