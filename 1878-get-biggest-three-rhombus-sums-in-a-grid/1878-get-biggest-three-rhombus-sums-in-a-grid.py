from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):

                # size 0 rhombus (single cell)
                res.add(grid[r][c])

                size = 1
                while True:
                    if r-size < 0 or r+size >= m or c-size < 0 or c+size >= n:
                        break

                    total = 0

                    # top -> right
                    i, j = r-size, c
                    for k in range(size):
                        total += grid[i+k][j+k]

                    # right -> bottom
                    i, j = r, c+size
                    for k in range(size):
                        total += grid[i+k][j-k]

                    # bottom -> left
                    i, j = r+size, c
                    for k in range(size):
                        total += grid[i-k][j-k]

                    # left -> top
                    i, j = r, c-size
                    for k in range(size):
                        total += grid[i-k][j+k]

                    res.add(total)
                    size += 1

        return sorted(res, reverse=True)[:3]