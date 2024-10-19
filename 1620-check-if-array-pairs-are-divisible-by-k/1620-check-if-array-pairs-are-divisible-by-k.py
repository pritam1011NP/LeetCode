from collections import defaultdict

class Solution:
    def canArrange(self, arr, k):
        # Frequency dictionary to count remainders
        remainder_count = defaultdict(int)
        
        # Count the frequency of each remainder when divided by k
        for num in arr:
            remainder = num % k
            # Handle negative remainders by converting them to positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # Now, check if we can form valid pairs
        for r in remainder_count:
            if r == 0:
                # If the remainder is 0, we need an even number of such elements
                if remainder_count[r] % 2 != 0:
                    return False
            elif 2 * r == k:
                # Special case when remainder is exactly half of k (only when k is even)
                # We need an even number of such elements
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                # For general case, the count of remainder r should match the count of remainder k - r
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return True

# Example usage:
solution = Solution()
arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k1 = 5
print(solution.canArrange(arr1, k1))  # Output: True

arr2 = [1, 2, 3, 4, 5, 6]
k2 = 7
print(solution.canArrange(arr2, k2))  # Output: True

arr3 = [1, 2, 3, 4, 5, 6]
k3 = 10
print(solution.canArrange(arr3, k3))  # Output: False
