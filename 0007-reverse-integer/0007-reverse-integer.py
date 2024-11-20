class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of x
        sign = 1 if x >= 0 else -1
        
        # Reverse the digits of the absolute value of x
        reversed_x = int(str(abs(x))[::-1])
        
        # Apply the sign to the reversed number
        result = sign * reversed_x
        
        # Check for 32-bit integer overflow
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result

        