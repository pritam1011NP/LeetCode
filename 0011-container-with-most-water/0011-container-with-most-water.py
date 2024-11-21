class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers and the maximum area variable
        left, right = 0, len(height) - 1
        max_area = 0

        # Loop until the two pointers meet
        while left < right:
            # Calculate the area with the current two pointers
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            # Update the maximum area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        