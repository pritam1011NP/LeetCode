class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        max_sum = 0
        current_sum = 0
        window_start = 0
        unique_elements = set()
        
        for window_end in range(len(nums)):
            # Add the current number to the sliding window
            while nums[window_end] in unique_elements or len(unique_elements) >= k:
                # Remove elements from the window until it's valid
                unique_elements.remove(nums[window_start])
                current_sum -= nums[window_start]
                window_start += 1
            
            # Add the new number to the window
            unique_elements.add(nums[window_end])
            current_sum += nums[window_end]
            
            # Check if we have a valid window of size k
            if len(unique_elements) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum

        