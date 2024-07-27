class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        
        // Fill the array using the relation discussed
        for (int i = 0; i <= n; i++) {
            // The number of 1's in i is 1 more than the number of 1's in i / 2 if i is odd
            // Otherwise, it's the same as in i / 2 if i is even
            ans[i] = ans[i >> 1] + (i & 1);
        }
        
        return ans;
    }
}