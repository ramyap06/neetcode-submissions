class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        if len(word) > ROWS * COLS:
            return False
        
        word_dict = {}
        for w in word:
            if w not in word_dict:
                word_dict[w] = 0
            word_dict[w] += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if len(word_dict) == 0:
                    break
                if board[r][c] in word_dict:
                    word_dict[board[r][c]] -= 1
                    if word_dict[board[r][c]] == 0:
                        del word_dict[board[r][c]]
        if len(word_dict) > 0:
            return False

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                board[row][col] != word[idx]):
                return False
            
            board[row][col] = '#'
            
            result = (dfs(row + 1, col, idx + 1) or
                      dfs(row - 1, col, idx + 1) or
                      dfs(row, col + 1, idx + 1) or
                      dfs(row, col - 1, idx + 1))
            
            board[row][col] = word[idx]

            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False