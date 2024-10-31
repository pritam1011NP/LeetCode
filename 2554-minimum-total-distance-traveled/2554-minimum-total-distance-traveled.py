class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories by their positions
        robot.sort()
        factory.sort()
        
        # Number of robots and factories
        n = len(robot)
        m = len(factory)
        
        # Initialize the dp array to store minimum distance to repair i robots using j factories
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: zero distance if no robots to repair

        # Dynamic programming to calculate the minimum distance
        for j in range(1, m + 1):
            position, limit = factory[j - 1]
            dp[0][j] = 0  # If there are no robots, distance is zero for any number of factories

            # Try to repair up to `limit` robots with the current factory
            for i in range(1, n + 1):
                total_dist = 0
                # Repair `k` robots at the current factory
                for k in range(1, min(i, limit) + 1):
                    total_dist += abs(robot[i - k] - position)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_dist)
                dp[i][j] = min(dp[i][j], dp[i][j - 1])

        # The answer is the minimum distance to repair all robots using all factories
        return dp[n][m]

        