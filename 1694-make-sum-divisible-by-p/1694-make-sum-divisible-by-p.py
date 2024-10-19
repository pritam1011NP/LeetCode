class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        
        # If the total sum is already divisible by p, no need to remove anything
        if remainder == 0:
            return 0
        
        # Dictionary to store the prefix sums and their indices
        prefix_sums = {0: -1}
        current_sum = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            current_sum += num
            current_sum %= p
            
            # Find the required prefix sum to make the subarray sum divisible by p
            target = (current_sum - remainder) % p
            
            if target in prefix_sums:
                min_length = min(min_length, i - prefix_sums[target])
            
            # Store the current prefix sum and its index
            prefix_sums[current_sum] = i
        
        return min_length if min_length < len(nums) else -1
    