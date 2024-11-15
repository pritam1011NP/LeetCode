class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for char in s:
            # Check the top of the stack and decide whether to remove "AB" or "CD"
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the matched pair
            else:
                stack.append(char)  # Push current character to stack
        
        # The length of the stack is the length of the minimized string
        return len(stack)
