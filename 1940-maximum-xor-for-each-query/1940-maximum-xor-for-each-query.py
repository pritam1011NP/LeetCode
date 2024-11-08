class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Step 1: Calculate the total XOR of all elements in nums
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # Step 2: Maximum k value is (2^maximumBit) - 1
        max_k = (1 << maximumBit) - 1
        
        # Step 3: Iterate in reverse to find the answer for each query
        result = []
        for num in reversed(nums):
            # Maximum XOR is achieved with total_xor ^ max_k
            result.append(total_xor ^ max_k)
            
            # Update the total_xor by removing the last element (simulating popping the element)
            total_xor ^= num
        
        return result


        