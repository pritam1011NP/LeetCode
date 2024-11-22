class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import Counter

        # Convert each row into a normalized pattern
        # Normalize a row by considering it and its flipped equivalent
        patterns = []
        for row in matrix:
            # Normalize by making the first element 0
            base_pattern = tuple(val ^ row[0] for val in row)
            patterns.append(base_pattern)
        
        # Count the frequency of each pattern
        pattern_counts = Counter(patterns)
        
        # The most frequent pattern determines the maximum equal rows
        return max(pattern_counts.values())
        