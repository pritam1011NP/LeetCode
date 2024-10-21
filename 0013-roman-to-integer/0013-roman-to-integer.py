class Solution:
    def romanToInt(self, s: str) -> int:
        # Define the values for each Roman numeral
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the result variable
        total = 0
        
        # Loop through the string
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            # Otherwise, add it to the total
            else:
                total += roman[s[i]]
        
        return total
sol = Solution()
print(sol.romanToInt("III"))       # Output: 3
print(sol.romanToInt("LVIII"))     # Output: 58
print(sol.romanToInt("MCMXCIV"))   # Output: 1994
   