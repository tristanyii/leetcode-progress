// Last updated: 1/12/2026, 3:13:15 PM
class Solution {
    public int getLargestOutlier(int[] nums) {
        int sum = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i = 0;i < nums.length;i++) {
            sum += nums[i];
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        int remainingSum;
        int max = Integer.MIN_VALUE;
        for (int i = 0;i < nums.length;i++) {
            remainingSum = sum - nums[i];
            if (remainingSum % 2 == 0) {
                remainingSum = remainingSum / 2;
                if (remainingSum == nums[i]) {
                    if (map.containsKey(remainingSum) && map.get(remainingSum) > 1) {
                        max = Math.max(nums[i],max);
                    }
                }
                else {
                    if (map.containsKey(remainingSum)) {
                        max = Math.max(nums[i],max);
                    }
                }
            }

        }
        return max;
    }
}