class Solution:
    def myAtoi(self, s: str) -> int:
        # Define limits for 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Strip leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Step 2: Handle optional sign
        sign = 1
        start = 0
        
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        
        # Step 3: Convert characters to number
        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
            
            # Step 4: Handle overflow by early exit
            if result > INT_MAX:
                break
        
        # Step 5: Apply sign and clamp the result within 32-bit bounds
        result *= sign
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
sol = Solution()
print(sol.myAtoi("42"))         # Output: 42
print(sol.myAtoi("   -042"))    # Output: -42
print(sol.myAtoi("1337c0d3"))   # Output: 1337
print(sol.myAtoi("0-1"))        # Output: 0
print(sol.myAtoi("words and 987"))  # Output: 0
  