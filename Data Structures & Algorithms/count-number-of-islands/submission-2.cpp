class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;
        int ROWS = grid.size();
        int COLS = grid[0].size();
            
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    std::queue<pair<int, int>> q;
                    q.push({r, c});
                    grid[r][c] = '*';
                    
                    while (!q.empty()) {
                        auto [row, col] = q.front();
                        q.pop();
                        std::vector<std::pair<int, int>> directions = {
                            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
                        };
                        for (const auto& [dr, dc] : directions) {
                            int new_r = row + dr;
                            int new_c = col + dc;
                            
                            if (new_r >= 0 && new_r < ROWS &&
                                new_c >= 0 && new_c < COLS &&
                                grid[new_r][new_c] == '1') {
                                    q.push({new_r, new_c});
                                    grid[new_r][new_c] = '*';
                            }
                        }
                    }
                    islands++;
                }
            }
        }
        
        return islands;
    }
};
