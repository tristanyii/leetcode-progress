// Last updated: 1/12/2026, 3:12:43 PM
class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        boolean[] ret = new boolean[queries.length];
        int[] k = new int[n];
        int count = 0;
        
        k[0] = count; 
        for (int i = 1;i < n;i++) {
            if (nums[i] - nums[i-1] > maxDiff) {
                count++;
            }
            k[i] = count;

        }
        for (int i = 0;i < queries.length;i++) {
            if (k[queries[i][0]] != k[queries[i][1]]) {
                ret[i] = false;            }
                else {
                    ret[i] = true;
                }
        }
        return ret;
    }
}