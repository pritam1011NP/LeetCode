from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(S):
            dsu = DSU(n)
            upgrades = 0
            used = 0

            optional = []

            for u,v,s,must in edges:
                if must == 1:
                    if s < S:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used += 1
                else:
                    optional.append((u,v,s))

            optional.sort(key=lambda x: x[2], reverse=True)

            for u,v,s in optional:
                if dsu.find(u) != dsu.find(v):

                    if s >= S:
                        dsu.union(u,v)
                        used += 1

                    elif 2*s >= S and upgrades < k:
                        dsu.union(u,v)
                        upgrades += 1
                        used += 1

                if used == n-1:
                    break

            return used == n-1


        left, right = 0, 2*10**5
        ans = -1

        while left <= right:
            mid = (left + right)//2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans