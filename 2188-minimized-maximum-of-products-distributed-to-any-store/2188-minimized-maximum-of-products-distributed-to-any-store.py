class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(maxProductsPerStore):
            storesNeeded = 0
            for qty in quantities:
                # Calculate the number of stores needed for this product type
                storesNeeded += (qty + maxProductsPerStore - 1) // maxProductsPerStore
                if storesNeeded > n:
                    return False
            return True
        
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try to find a smaller maximum
            else:
                left = mid + 1
        
        return left

        