class Solution:
    def intToRoman(self, num: int) -> str:
        # Define Roman numeral symbols and their values
        values = [
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 
            1
        ]
        symbols = [
            "M", "CM", "D", "CD", 
            "C", "XC", "L", "XL", 
            "X", "IX", "V", "IV", 
            "I"
        ]
        
        roman = ""  # Resultant Roman numeral
        
        # Iterate through values and symbols
        for i in range(len(values)):
            # Append the corresponding Roman numeral symbols
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]
        
        return roman

        