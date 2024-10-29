class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize a pointer for t
        j = 0
        
        # Loop through each character in s
        for char in s:
            # If the character in s matches the current character in t,
            # move the pointer of t to the next character
            if j < len(t) and char == t[j]:
                j += 1
        
        # The number of characters to append is the remaining length of t
        return len(t) - j
        