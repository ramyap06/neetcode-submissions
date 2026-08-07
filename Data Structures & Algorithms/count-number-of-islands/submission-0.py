class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            grid[row][col] = "*"
            
            while q:
                r, c = q.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r >= 0 and new_r < ROWS and
                        new_c >= 0 and new_c < COLS and
                        grid[new_r][new_c] == "1"):
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = "*"
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands