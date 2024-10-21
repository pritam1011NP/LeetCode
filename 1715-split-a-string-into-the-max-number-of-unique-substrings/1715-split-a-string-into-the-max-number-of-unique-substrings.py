class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return 0

            max_splits = 0
            for i in range(start, len(s)):
                substr = s[start:i + 1]
                if substr not in seen:
                    seen.add(substr)
                    max_splits = max(max_splits, 1 + backtrack(i + 1, seen))
                    seen.remove(substr)

            return max_splits

        return backtrack(0, set())

# Example usage
solution = Solution()
print(solution.maxUniqueSplit("ababccc"))  # Output: 5
print(solution.maxUniqueSplit("aba"))      # Output: 2
print(solution.maxUniqueSplit("aa"))       # Output: 1
       