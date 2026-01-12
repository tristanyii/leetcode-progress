// Last updated: 1/12/2026, 3:13:40 PM
class Solution {
    // HashMap to memoize results and avoid redundant calculations
    private HashMap<String, Integer> memo;
    
    public int maxOperations(int[] nums) {
        memo = new HashMap<>();
        return findMaxOperations(nums, 0, 0, nums.length - 1);
    }
    
    /**
     * Recursively finds the maximum number of operations with the same score
     * 
     * @param nums The original array
     * @param targetSum The target sum for the operation (0 for first operation)
     * @param left Left pointer indicating start of current subarray
     * @param right Right pointer indicating end of current subarray
     * @return Maximum number of operations possible
     */
    private int findMaxOperations(int[] nums, int targetSum, int left, int right) {
        // Base case: can't perform any operation with less than 2 elements
        if (right - left + 1 < 2) {
            return 0;
        }
        
        // Create a unique key for memoization
        String memoKey = left + "," + right + "," + targetSum;
        
        // Check if we already computed this state
        if (memo.containsKey(memoKey)) {
            return memo.get(memoKey);
        }
        
        int maxOperations = 0;
        
        // Option 1: Take first two elements
        if (targetSum == 0 || nums[left] + nums[left + 1] == targetSum) {
            maxOperations = Math.max(maxOperations, 
                           findMaxOperations(nums, targetSum == 0 ? nums[left] + nums[left + 1] : targetSum, 
                                           left + 2, right) + 1);
        }
        
        // Option 2: Take last two elements
        if (targetSum == 0 || nums[right - 1] + nums[right] == targetSum) {
            maxOperations = Math.max(maxOperations, 
                           findMaxOperations(nums, targetSum == 0 ? nums[right - 1] + nums[right] : targetSum, 
                                           left, right - 2) + 1);
        }
        
        // Option 3: Take first and last elements
        if (targetSum == 0 || nums[left] + nums[right] == targetSum) {
            maxOperations = Math.max(maxOperations, 
                           findMaxOperations(nums, targetSum == 0 ? nums[left] + nums[right] : targetSum, 
                                           left + 1, right - 1) + 1);
        }
        
        // Cache the result
        memo.put(memoKey, maxOperations);
        return maxOperations;
    }
}