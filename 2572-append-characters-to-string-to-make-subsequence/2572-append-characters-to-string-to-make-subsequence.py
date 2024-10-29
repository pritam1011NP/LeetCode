class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize two pointers, one for s and one for t
        i, j = 0, 0
        
        # Traverse through s and t to find the common subsequence
        while i < len(s) and j < len(t):
            # If characters match, move both pointers
            if s[i] == t[j]:
                j += 1
            # Move the pointer in s regardless
            i += 1
        
        # If we have not reached the end of t, then we need to append the remaining characters in t
        return len(t) - j
