from typing import List
from collections import defaultdict, deque

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Initialize in-degree array and adjacency list
        in_degree = [0] * n
        graph = defaultdict(list)
        
        # Build the graph and in-degree array
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Find all nodes with in-degree 0
        candidates = [i for i in range(n) if in_degree[i] == 0]
        
        # If there's exactly one node with in-degree 0, it's the champion
        if len(candidates) == 1:
            return candidates[0]
        
        # Otherwise, return -1
        return -1

        