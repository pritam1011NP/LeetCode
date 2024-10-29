class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(row, col):
            # If the result is already computed, return it
            if memo[row][col] != -1:
                return memo[row][col]
            
            max_moves = 0
            for dr in [-1, 0, 1]:  # possible row directions
                newRow, newCol = row + dr, col + 1
                if 0 <= newRow < m and newCol < n and grid[newRow][newCol] > grid[row][col]:
                    max_moves = max(max_moves, 1 + dfs(newRow, newCol))
            
            memo[row][col] = max_moves
            return max_moves
        
        # Try to start from any cell in the first column
        max_moves = 0
        for row in range(m):
            max_moves = max(max_moves, dfs(row, 0))
        
        return max_moves
