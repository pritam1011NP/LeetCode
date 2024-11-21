class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid with 0: unoccupied, 1: guard, 2: wall, -1: guarded
        grid = [[0] * n for _ in range(m)]
        
        # Place guards and walls on the grid
        for r, c in guards:
            grid[r][c] = 1  # Guard
        for r, c in walls:
            grid[r][c] = 2  # Wall
        
        # Function to mark cells in one direction
        def mark_direction(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] == 2 or grid[r][c] == 1:  # Stop at wall or another guard
                    break
                if grid[r][c] == 0:  # Mark as guarded
                    grid[r][c] = -1
                r += dr
                c += dc
        
        # Mark all cells guarded by each guard
        for r, c in guards:
            mark_direction(r - 1, c, -1, 0)  # Up
            mark_direction(r + 1, c, 1, 0)   # Down
            mark_direction(r, c - 1, 0, -1)  # Left
            mark_direction(r, c + 1, 0, 1)   # Right
        
        # Count unguarded unoccupied cells
        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:  # Unoccupied and unguarded
                    unguarded_count += 1
        
        return unguarded_count
