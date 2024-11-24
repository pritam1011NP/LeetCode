from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Initialize variables
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        
        # Traverse the matrix
        for row in matrix:
            for value in row:
                total_sum += abs(value)  # Add the absolute value to the total sum
                min_abs_value = min(min_abs_value, abs(value))  # Track the smallest absolute value
                if value < 0:
                    negative_count += 1  # Count negative numbers
        
        # If there is an odd number of negatives, subtract double the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value
        
        return total_sum

        