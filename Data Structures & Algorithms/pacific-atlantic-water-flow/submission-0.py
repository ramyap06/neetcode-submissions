class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachable = []
        ROWS, COLS = len(heights), len(heights[0])

        p_que = collections.deque()
        a_que = collections.deque()
        p_visited = set()
        a_visited = set()

        for c in range(COLS):
            p_que.append((0, c))
            p_visited.add((0, c))
            a_que.append((ROWS - 1, c))
            a_visited.add((ROWS - 1, c))
        
        for r in range(ROWS):
            p_que.append((r, 0))
            p_visited.add((r, 0))
            a_que.append((r, COLS - 1))
            a_visited.add((r, COLS - 1))

        def bfs(q, visited):
            coords = set()

            while q:
                row, col = q.pop()
                coords.add((row, col))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r >= 0 and r < ROWS and
                        c >= 0 and c < COLS and
                        heights[row][col] <= heights[r][c] and
                        (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

            return coords
        
        p_coords = bfs(p_que, p_visited)
        a_coords = bfs(a_que, a_visited)

        for p in list(p_coords):
            if p in a_coords:
                reachable.append(list(p))
        
        return reachable