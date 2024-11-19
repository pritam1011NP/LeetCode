class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        # Iterate over the characters in the string
        for char in s:
            rows[cur_row] += char
            # Change direction at the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        # Concatenate all rows to form the final string
        return ''.join(rows)

        