class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        
        for char in s:
            # Check if the last two characters are the same as the current character
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            result.append(char)
        
        # Join list into final string
        return ''.join(result)
       