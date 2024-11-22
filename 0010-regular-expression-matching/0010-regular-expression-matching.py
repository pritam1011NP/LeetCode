class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a 2D dp array where dp[i][j] represents whether s[:i] matches p[:j].
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches empty pattern.

        # Handle patterns with '*' that can match zero characters.
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the dp table.
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # '.' matches any character or character matches itself.
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' matches zero occurrences or one/more occurrences of the preceding character.
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))

        return dp[len(s)][len(p)]

        