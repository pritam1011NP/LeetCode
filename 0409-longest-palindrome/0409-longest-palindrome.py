class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
        
        # Add one if there was any odd frequency to place in the center
        if odd_found:
            length += 1
        
        return length
       