class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize with the count of characters in the first word
        common_count = Counter(words[0])
        
        # Intersect counts with each subsequent word to find common characters
        for word in words[1:]:
            common_count &= Counter(word)
        
        # Expand the characters to the required frequency
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result

        