class Solution {
    public int takeCharacters(String s, int k) {
        if (k == 0) return 0;

        int n = s.length();
        int[] totalCount = new int[3]; // Total count of 'a', 'b', 'c' in s

        for (char ch : s.toCharArray()) {
            totalCount[ch - 'a']++;
        }

        // If it is impossible to get k of each character, return -1
        if (totalCount[0] < k || totalCount[1] < k || totalCount[2] < k) return -1;

        int[] currentCount = new int[3]; // Current count of 'a', 'b', 'c' in the window
        int maxWindowSize = 0; // Maximum size of the valid window
        int left = 0;

        for (int right = 0; right < n; right++) {
            char ch = s.charAt(right);
            currentCount[ch - 'a']++;

            // Shrink the window if it contains more than `totalCount[i] - k` for any character
            while (currentCount[0] > totalCount[0] - k || 
                   currentCount[1] > totalCount[1] - k || 
                   currentCount[2] > totalCount[2] - k) {
                currentCount[s.charAt(left) - 'a']--;
                left++;
            }

            // Update the maximum valid window size
            maxWindowSize = Math.max(maxWindowSize, right - left + 1);
        }

        // Minimum minutes needed is the size of s minus the size of the largest valid window
        return n - maxWindowSize;
    }
}
