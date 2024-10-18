class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        count = 0
        n = len(nums)
        
        # Iterate through all possible subsets using bitmask
        for mask in range(1, 1 << n):  # 1 << n gives us 2^n (all subsets except empty)
            current_or = 0
            for i in range(n):
                if mask & (1 << i):  # Check if the i-th bit is set in the mask
                    current_or |= nums[i]
            
            # Check if current subset OR is equal to the max OR
            if current_or > max_or:
                max_or = current_or
                count = 1  # Reset count since we found a new max
            elif current_or == max_or:
                count += 1  # Increment count for subsets with max OR
        
        return count

# Example usage:
sol = Solution()
print(sol.countMaxOrSubsets([3, 1]))  # Output: 2
print(sol.countMaxOrSubsets([2, 2, 2]))  # Output: 7
print(sol.countMaxOrSubsets([3, 2, 1, 5]))  # Output: 6
      